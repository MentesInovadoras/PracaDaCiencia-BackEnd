from rest_framework import viewsets

from .models import *
from .serializers import *


class UnidadeDeEnsinoViewset(viewsets.ModelViewSet):
    queryset = Visitante.objects.filter(instituicao__isnull=False)
    serializer_class = UnidadeDeEnsinoSerializer
    
    
class VisitanteViewset(viewsets.ModelViewSet):
    queryset = Visitante.objects.filter(pessoa__isnull=False)
    serializer_class = VisitanteSerializer
    
    