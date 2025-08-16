from rest_framework import serializers
from .models import *

from apps.visitantes.serializers import *

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'


class GuiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guias
        fields = '__all__'

class VisitaReadSerializer(serializers.ModelSerializer):
    guia = GuiasSerializer(read_only=True)
    visitante = VisitanteReadSerializer(read_only=True)
    tipo_visita = VisitanteReadSerializer(read_only=True)

    class Meta:
        model = Visita
        fields = '__all__' 


class VisitaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__' 


class VisitaSimplificadaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = ['nome_visitante']

class VisitanteReadSerializer(serializers.ModelSerializer):
    instituicao = UnidadeDeEnsinoSerializer(read_only=True)
    roteiro = RoteiroSerializer(read_only=True)

    class Meta:
        model = Visitante
        fields = '__all__'