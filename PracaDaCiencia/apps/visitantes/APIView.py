from datetime import date
from rest_framework import status
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import TruncDay

from .Errors import *
from .models import Visita


# UC04 - Agendar Visita
class BuscarDiasIndisponiveis(APIView):
    def get(self, request, mes: int):
        if(mes > 11 or mes < 0):
            return ErroValorDeMesInvalido
        
        segundasFeiras: list[int] = self.__buildListaSegundasFeiras()
        
        # 1. Filtra objetos do mês e ano específicos
        objetos_mes = Visita.objects.filter(data__year=ano, data__month=mes)

        # 2. Agrupa por dia e conta quantos objetos tem em cada dia
        dias_com_contagem = objetos_mes.annotate(dia=TruncDay('data')) \
            .values('dia') \
            .annotate(qtd=Count('id')) \
            .filter(qtd__gt=4)

        # 3. Coleta os dias que têm mais de 4 objetos
        dias_validos = [d['dia'] for d in dias_com_contagem]

        # 4. Agora pega apenas UM objeto para cada dia desses
        from django.db.models import OuterRef, Subquery

        # Subquery para pegar o primeiro ID de cada dia válido
        sub = MeuModelo.objects.filter(
            data__date=OuterRef('data__date')
        ).order_by('id').values('id')[:1]

        # Objetos finais: do mês específico, nos dias válidos, um por dia
        objetos_finais = MeuModelo.objects.filter(
            data__date__in=dias_validos
        ).annotate(first_id=Subquery(sub)).filter(id=F('first_id'))
        

        
        listaDeAgendamentos = Visita.objects.filter(data_visita__month=mes)
        
        demaisDias: list[int] = [x for x in listaDeAgendamentos]
        
    
    def __buildListaSegundasFeiras(self, mesReferencia: int) -> list[int]:
        diaAtual = date()

        if(mesReferencia <= ((diaAtual.month+2) % 12)):
            return ErroTentandoMarcarAgendamentoAlem2Meses()

        anoBuscado = diaAtual.year
        if(mesReferencia < diaAtual.month): anoBuscado+=1
        
        busca = date(anoBuscado, mesReferencia, 7)
        
        return [x for x in range(busca.day - busca.weekday(), 31, 7)]