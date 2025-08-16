from rest_framework import viewsets

from .models import *
from .serializers import *



class UnidadeDeEnsinoViewset(viewsets.ModelViewSet):
    queryset = UnidadeDeEnsino.objects.all()
    serializer_class = UnidadeDeEnsinoSerializer
    
class RoteiroViewset(viewsets.ModelViewSet):
    queryset = Roteiro.objects.all()
    serializer_class = RoteiroSerializer

class VisitanteViewset(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return VisitanteReadSerializer
        return VisitanteWriteSerializer
    
