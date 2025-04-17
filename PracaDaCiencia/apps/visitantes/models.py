from django.db import models

from ..administrador.models import Guias


class Pessoa(models.Model):
    cep = models.CharField(max_length=10)


class UnidadeDeEnsino(models.Model):
    class UnidadeDeEnsinoTipo(models.TextChoices):
        Publica = "Pública"
        Privada = "Privada"
        ONG = "ONG"

    class UnidadeDeEnsinoEscolaridade(models.TextChoices):
        Fundamental1 = "Fundamental1"
        Fundamental2 = "Fundamental2"
        Medio = "Médio"
        Superior = "Superior"
        Profissionais = "Profissionais"
        Educacao = "Educação"
        Outros = "Outros"

    tipo = models.CharField(choices=UnidadeDeEnsinoTipo.choices, max_length=50)
    escolaridade = models.CharField(choices=UnidadeDeEnsinoEscolaridade.choices, max_length=50)


class Visitante(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    instituicao = models.ForeignKey(UnidadeDeEnsino, on_delete=models.CASCADE, null=True, blank=True)


class Visita(models.Model):
    class VisitaTipo(models.TextChoices):
        PessoaFisica = "Pessoa Física"
        UnidadeDeEnsino = "Unidade de Ensino"
    
    class StatusVisita(models.TextChoices):
        Agendado = "Agendado"
        Expirado = "Expirado"
        Cancelada = "Cancelada"
        Realizado = "Realizado"

    tipo_visita = models.CharField(choices=VisitaTipo.choices, max_length=40)
    data_visita = models.DateField()
    numero_visitantes = models.IntegerField()
    
    status = models.CharField(choices=StatusVisita.choices, max_length=50, default=StatusVisita.Agendado)
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE, null=False)
    guia = models.ForeignKey(Guias, on_delete=models.PROTECT, null=True, blank=True)

