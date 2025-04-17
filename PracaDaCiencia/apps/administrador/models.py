from django.db import models
from django.contrib.auth.models import User


class Tecnico(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Guias(models.Model):
    nome = models.CharField(max_length=100)


class Municipio(models.Model):
    nome = models.CharField(max_length=100)


class Roteiro(models.Model):
    nome = models.CharField(max_length=100)
    ensino = models.BooleanField(default=False)
    sataus = models.BooleanField(default=False)
