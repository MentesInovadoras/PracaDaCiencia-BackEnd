from django.db import models


class Pessoa(models.Model):
    cep = models.CharField(max_length=10)


class UnidadeDeEnsino(models.Model):
    class UnidadeDeEnsinoTipo(models.TextChoices):
        Publica = "Pública"
        Privada = "Privada"
        ONG = "ONG"

    class UnidadeDeEnsinoEscolaridade(models.TextChoices):
        Fundamental1 = "Fundamental 1"
        Fundamental2 = "Fundamental 2"
        Medio = "Médio"
        Superior = "Superior"
        Profissionais = "Profissionais"
        Educacao = "Educação"
        Outro = "Outro"

    municipio = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    tipo = models.CharField(choices=UnidadeDeEnsinoTipo.choices, max_length=50)
    escolaridade = models.CharField(choices=UnidadeDeEnsinoEscolaridade.choices, max_length=50)


class Visitante(models.Model):
    class TipoVisitante(models.TextChoices):
        UnidadeDeEnsino = "Unidade de Ensino"
        PessoaFisica = "Pessoa Física"
    nome = models.CharField(max_length=50)
    email = models.EmailField(null=True, default=True)
    telefone = models.CharField(max_length=11)
    
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    instituicao = models.ForeignKey(UnidadeDeEnsino, on_delete=models.CASCADE, null=True, blank=True)

    def visitante_tipo(self) -> TipoVisitante:
        if(self.pessoa == None):
            return Visitante.TipoVisitante.UnidadeDeEnsino
        return Visitante.TipoVisitante.PessoaFisica

