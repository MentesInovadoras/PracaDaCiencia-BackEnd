from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.serializers import Serializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class TecnicoViewset(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class VisitaViewset(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    
    def get_serializer_class(self) -> type[Serializer]:
        if(self.request.method == "GET"):
            return VisitaReadSerializer
        return VisitaWriteSerializer
    
    @swagger_auto_schema(
        method='get',
        manual_parameters=[
            openapi.Parameter(
                name='dia',
                in_=openapi.IN_PATH,
                description='Data no formato AAAA-MM-DD',
                type=openapi.TYPE_STRING,
                pattern=r'\d{4}-\d{2}-\d{2}',
                required=True
            ),
        ],
        responses={200: VisitaReadSerializer(many=True)}
    )
    @action(methods=['GET'], detail=False, url_path=r"<str:dia>")
    def visitas_especificas(self, request):
        object_filtrado = Visita.objects.filter(data_visita__date=request.query_params.get('dia'))
        serializer = VisitaReadSerializer(many=True, data=object_filtrado)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

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