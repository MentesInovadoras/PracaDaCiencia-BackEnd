from rest_framework import serializers
from .models import *

from apps.visitantes.serializers import *


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'

class RoteiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roteiro
        fields = '__all__'

class GuiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guias
        fields = '__all__'

class VisitaReadSerializer(serializers.ModelSerializer):
    guia = GuiasSerializer(many=False)
    roteiro = RoteiroSerializer(many=False)
    visitante = serializers.SerializerMethodField()
    tipo_visitante = serializers.SerializerMethodField()
    
    class Meta:
        model = Visita
        fields = '__all__' 

    def get_visitante(self, obj: Visita):
        match (obj.visitante.visitante_tipo()):
            case Visitante.TipoVisitante.UnidadeDeEnsino:
                return UnidadeDeEnsinoSerializer(obj.visitante).data
            case Visitante.TipoVisitante.PessoaFisica:
                return VisitanteSerializer(obj.visitante).data
    def get_tipo_visitante(self, obj: Visita):
        return obj.visitante.visitante_tipo()
    
class VisitaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__' 

class VisitaSimplificadaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = ['nome_visitante']

