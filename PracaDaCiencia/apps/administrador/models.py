from django.db import models
from django.contrib.auth.models import User

from django.db import models

from apps.visitantes.models import *


class Tecnico(models.Model):
    user = User


class Guias(models.Model):
    nome = models.CharField(max_length=100)


class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    ensino = models.BooleanField(default=False)
    ativo = models.BooleanField(default=False)
    

class Visita(models.Model):
    class StatusVisita(models.TextChoices):
        Agendado = "Agendado"
        Expirado = "Expirado"
        Cancelada = "Cancelada"
        Realizado = "Realizado"

    numero_visitantes = models.IntegerField()
    data_visita = models.DateTimeField()
    observacao = models.CharField(max_length=255)
    status = models.CharField(choices=StatusVisita.choices, max_length=50, default=StatusVisita.Agendado)

    roteiro = models.ForeignKey(Roteiro, on_delete=models.PROTECT)
    visitante = models.ForeignKey(Visitante, on_delete=models.PROTECT)
    guia = models.ForeignKey(Guias, on_delete=models.CASCADE, null=True, blank=True)

