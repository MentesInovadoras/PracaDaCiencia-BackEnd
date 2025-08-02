from rest_framework import viewsets

from .models import *
from .serializers import *


class UnidadeDeEnsinoViewset(viewsets.ModelViewSet):
    queryset = UnidadeDeEnsino.objects.all()
    serializer_class = UnidadeDeEnsinoSerializer
    
    