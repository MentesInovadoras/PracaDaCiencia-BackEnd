from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from django.db import models
from django.db.models import Value
from django.db.models.functions import Concat

from apps.visitantes.models import Visitante
"""
Aqui ficará todos os dados que são competência do administrador
decidir em primeiro caso, contudo, também terá que ter acesso à 
tudo, para realizar alterações.
"""

class Tecnico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Guias(models.Model):
    nome = models.CharField(max_length=100)

class StatusVisita(models.TextChoices):
        Agendado = "Agendado"
        Expirado = "Expirado"
        Cancelada = "Cancelada"
        Realizado = "Realizado"

class Visita(models.Model):
    observacao = models.CharField(max_length=255)
    status = models.CharField(choices=StatusVisita.choices, max_length=20, default=StatusVisita.Agendado)
    guia = models.ForeignKey(Guias, on_delete=models.CASCADE, null=True, blank=True)
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        if self.status == StatusVisita.Realizado and not self.guia:
            raise ValidationError("Uma visita realizada precisa ter um guia definido.")

    def __str__(self):
         return self.visitante.__str__