from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from datetime import datetime, timedelta


class DiasIndisponiveis(APIView):
    def get(self, request):
        dias = [ *self.__removeMondays(), ]
        
        return Response(dias, status=status.HTTP_200_OK)
    
    
    def __removeMondays(self) -> list[datetime]:
        hoje = datetime.today()
        primeiro_dia = datetime(year=hoje.year, month=hoje.month, day=1)
        primeira_segunda = primeiro_dia + timedelta(days=(7 - primeiro_dia.weekday()) % 7)
        
        return [primeira_segunda+timedelta(weeks=x) for x in range(9)] # cria um array com todas as segundas do mês atual e do subsequente
    

class HorariosDisponiveis(APIView):
    def get(self, request, dia: str):
        return Response([f"0{x}:00" for x in range(6, 10)], status=status.HTTP_200_OK)
    
    