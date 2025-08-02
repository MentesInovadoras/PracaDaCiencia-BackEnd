from rest_framework import serializers
from .models import *


class UnidadeDeEnsinoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = UnidadeDeEnsino
        fields = '__all__'
        
        