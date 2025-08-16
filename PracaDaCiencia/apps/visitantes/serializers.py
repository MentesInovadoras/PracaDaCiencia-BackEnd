from rest_framework import serializers
from .models import *


class UnidadeDeEnsinoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = UnidadeDeEnsino
        fields = '__all__'
        
class RoteiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roteiro
        fields = '__all__'


class VisitanteReadSerializer(serializers.ModelSerializer):
    instituicao = UnidadeDeEnsinoSerializer(read_only=True)
    roteiro = RoteiroSerializer(read_only=True)

    class Meta:
        model = Visitante
        fields = '__all__'

class VisitanteWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitante
        fields = '__all__'

