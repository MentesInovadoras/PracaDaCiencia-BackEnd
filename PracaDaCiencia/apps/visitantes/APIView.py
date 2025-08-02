from datetime import date
from rest_framework import status
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import TruncDay

from .Errors import *
from .models import *

# UC04 - Agendar Visita
class BuscarDiasIndisponiveis(APIView):
    def get(self, request, mes: int):
        if(mes > 11 or mes < 0):
            return ErroValorDeMesInvalido
        
        segundasFeiras: list[int] = self.__buildListaSegundasFeiras()
        
        return Response([*segundasFeiras], status=status.HTTP_200_OK)
    
    def __buildListaSegundasFeiras(self, mesReferencia: int) -> list[int]:
        diaAtual = date()

        if(mesReferencia <= ((diaAtual.month+2) % 12)):
            return ErroTentandoMarcarAgendamentoAlem2Meses()

        anoBuscado = diaAtual.year
        if(mesReferencia < diaAtual.month): anoBuscado+=1
        
        busca = date(anoBuscado, mesReferencia, 7)
        
        return [x for x in range(busca.day - busca.weekday(), 31, 7)]
    
    