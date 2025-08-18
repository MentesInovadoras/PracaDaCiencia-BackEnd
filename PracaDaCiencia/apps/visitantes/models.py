from django.db import models
from django.core.exceptions import ValidationError

"""
Aqui ficará todos os dados que são da 
competência do visitante decidir em primeiro caso.
Sem acesso a demais dados
"""
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

    municipio = models.CharField(max_length=100)
    nome_responsavel = models.CharField(max_length=100)
    tipo = models.CharField(choices=UnidadeDeEnsinoTipo.choices, max_length=50)
    escolaridade = models.CharField(choices=UnidadeDeEnsinoEscolaridade.choices, max_length=50)

class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    ensino = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

class Visitante(models.Model):
    class VisitaTipo(models.TextChoices):
            PessoaFisica = "Pessoa Física"
            UnidadeDeEnsino = "Unidade de Ensino"

    tipo_visita = models.CharField(choices=VisitaTipo.choices, max_length=50)
    data_visita = models.DateTimeField()
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=10, null=True, default=None, blank=True)
    quantidade = models.CharField(max_length=50, null=True, blank=True)
    roteiro = models.ForeignKey(Roteiro, on_delete=models.SET_NULL, null=True, blank=True)
    instituicao = models.ForeignKey(UnidadeDeEnsino, on_delete=models.CASCADE, null=True, blank=True)

    def clean(self):
         super().clean()
         if self.tipo_visita == self.VisitaTipo.UnidadeDeEnsino and not self.instituicao_id:
              raise ValidationError("Se o tipo da visita for 'Unidade de Ensino', é obrigatório informar a instituição.")
         
    def __str__(self):
         return (f"{self.nome} {self.tipo_visita}")