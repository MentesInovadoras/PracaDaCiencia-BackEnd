from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.serializers import Serializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *

from django.utils import timezone


class TecnicoViewset(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class VisitaViewset(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return VisitaReadSerializer
        return VisitaWriteSerializer
    
    @swagger_auto_schema(
        method='get',
        manual_parameters=[
            openapi.Parameter(
                name='dia',
                in_=openapi.IN_QUERY,
                description='Data no formato AAAA-MM-DD',
                type=openapi.TYPE_STRING,
                pattern=r'\d{4}-\d{2}-\d{2}',
                required=True
            ),
        ],
        responses={200: VisitaReadSerializer(many=True)}
    )
    @action(methods=['GET'], detail=False, url_path='visitas_especificas')
    def visitas_especificas(self, request):
        dia = request.query_params.get('dia')
        if not dia:
            return Response({"erro": "Parâmetro 'dia' obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        visitas = Visita.objects.filter(visitante__data_visita__date=dia)
        serializer = VisitaReadSerializer(visitas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GuiasViewset(viewsets.ModelViewSet):
    queryset = Guias.objects.all()
    serializer_class = GuiasSerializer


class VisitanteViewsetToday(viewsets.ModelViewSet):
    queryset = Visitante.objects.all()
    serializer_class = VisitanteReadSerializer

    @action(detail=False)
    def hoje(self, request):
        hoje = timezone.now().date()
        visitantes_hoje = Visitante.objects.filter(data_visita__date=hoje)
        visitantes_hoje = visitantes_hoje.order_by('data_visita')
        serializers = self.get_serializer(visitantes_hoje, many=True)

        return Response(serializers.data)