from rest_framework import viewsets
from rest_framework.response import Response
from .models import Tecnico, Visita, Roteiro, UnidadeDeEnsino, Guias, Municipio
from .serializers import TecnicoSerializer, VisitaSerializer, RoteiroSerializer, UnidadeDeEnsinoSerializer, GuiasSerializer, MunicipioSerializer

class TecnicoViewset(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class VisitaViewset(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class RoteiroViewset(viewsets.ModelViewSet):
    queryset = Roteiro.objects.all()
    serializer_class = RoteiroSerializer

class UnidadeDeEnsinoViewset(viewsets.ModelViewSet):
    queryset = UnidadeDeEnsino.objects.all()
    serializer_class = UnidadeDeEnsinoSerializer

class GuiasViewset(viewsets.ModelViewSet):
    queryset = Guias.objects.all()
    serializer_class = GuiasSerializer  

class MunicipioViewset(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer