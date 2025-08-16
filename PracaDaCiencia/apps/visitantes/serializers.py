from rest_framework import serializers
from .models import *


class VisitanteSerializer(serializers.ModelSerializer):
    cep = serializers.CharField(max_length=10, source='pessoa.cep')

    class Meta:
        model = Visitante
        fields = ['id', 'nome', 'email', 'telefone', 'cep']

    def validate(self, attrs):
        if len(attrs.get('pessoa', {}).get('cep', '')) == 0:
            raise serializers.ValidationError("campo CEP não pode ser nulo")
        
        return attrs

    def create(self, validated_data):
        cep = validated_data.pop('pessoa').pop('cep')
        pessoa = Pessoa.objects.create(cep=cep)
        visitante = Visitante.objects.create(pessoa=pessoa, **validated_data)
        return visitante

    def update(self, instance: Visitante, validated_data):
        instance.pessoa.cep = validated_data.get('pessoa').get('cep')
        instance.pessoa.save()

        instance.nome = validated_data.get('nome', instance.nome)
        instance.email = validated_data.get('email', instance.email)
        instance.telefone = validated_data.get('telefone', instance.telefone)

        instance.save()
        return instance
    
    

class UnidadeDeEnsinoSerializer(serializers.ModelSerializer):   
    nome_instituicao = serializers.CharField(source='nome')
    email_instituicao = serializers.EmailField(source='email')
    telefone_instituicao = serializers.CharField(source='telefone')
    municipio = serializers.CharField(source='instituicao.municipio')
    nome_responsavel = serializers.CharField(source='instituicao.responsavel')
    tipo_instituicao = serializers.ChoiceField(choices=UnidadeDeEnsino.UnidadeDeEnsinoTipo.choices, source='instituicao.tipo')
    escolaridade = serializers.ChoiceField(choices=UnidadeDeEnsino.UnidadeDeEnsinoEscolaridade.choices, source='instituicao.escolaridade')
    
    class Meta:
        model = Visitante
        fields = ['id', 'nome_instituicao', 'email_instituicao', 'telefone_instituicao', 'municipio', 'nome_responsavel', 'tipo_instituicao', 'escolaridade']
    
    def create(self, validated_data):
        instituicao = UnidadeDeEnsino.objects.create(
            municipio=validated_data.get('municipio'),
            responsavel=validated_data.get('nome_responsavel'),
            tipo=validated_data.get('tipo_instituicao'),
            escolaridade=validated_data.get('escolaridade'),
        )

        visitante = Visitante.objects.create(
            nome=validated_data.get('nome_instituicao'),
            email=validated_data.get('email_instituicao'),
            telefone=validated_data.get('telefone_instituicao'),
            pessoa=None,
            instituicao=instituicao,
        )

        return visitante

    def update(self, instance: Visitante, validated_data):
        instance.nome = validated_data.get('nome_instituicao', instance.nome)
        instance.email = validated_data.get('email_instituicao', instance.email)
        instance.telefone = validated_data.get('telefone_instituicao', instance.telefone)

        instituicao = instance.instituicao
        instituicao.municipio = validated_data.get('municipio', instituicao.municipio)
        instituicao.responsavel = validated_data.get('nome_responsavel', instituicao.responsavel)
        instituicao.tipo = validated_data.get('tipo_instituicao', instituicao.tipo)
        instituicao.escolaridade = validated_data.get('escolaridade', instituicao.escolaridade)

        instituicao.save()
        instance.save()

        return instance
    
    