from rest_framework import serializers
from .models import Tecnico, Visita, Roteiro, UnidadeDeEnsino, Guias, Municipio


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'

class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__' 

class RoteiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roteiro
        fields = '__all__'

class UnidadeDeEnsinoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = UnidadeDeEnsino
        fields = '__all__'

class GuiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guias
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'