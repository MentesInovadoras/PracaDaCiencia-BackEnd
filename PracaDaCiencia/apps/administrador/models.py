from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat


class Tecnico(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    name = Concat('firstName', Value(' '), 'lastName')
    idade = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Guias(models.Model):
    nome = models.CharField(max_length=100)


class Visita(models.Model):
    class VisitaTipo(models.TextChoices):
        PessoaFisica = "Pessoa Física"
        UnidadeDeEnsino = "Unidade de Ensino"
    
    class StatusVisita(models.TextChoices):
        Agendado = "Agendado"
        Expirado = "Expirado"
        Cancelada = "Cancelada"
        Realizado = "Realizado"

    nome_visitante = models.CharField(max_length=100)
    CEP_visitante = models.CharField(max_length=10)
    email_visitante = models.EmailField()
    telefone_visitante = models.CharField(max_length=15)
    numero_visitantes = models.IntegerField()
    tipo_visita = models.CharField(choices=VisitaTipo.choices, max_length=50)
    data_visita = models.DateTimeField()
    observacao = models.CharField(max_length=255)
    status = models.CharField(choices=StatusVisita.choices, max_length=50, default=StatusVisita.Agendado)
    guia = models.ForeignKey(Guias, on_delete=models.CASCADE, null=True, blank=True)


class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    ensino = models.BooleanField(default=False)
    sataus = models.BooleanField(default=False)


class Municipio(models.Model):
    nome = models.CharField(max_length=100)


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

    email = models.EmailField()
    nome = models.CharField(max_length=100)
    tipo = models.CharField(choices=UnidadeDeEnsinoTipo.choices, max_length=50)
    escolaridade = models.CharField(choices=UnidadeDeEnsinoEscolaridade.choices, max_length=50)

