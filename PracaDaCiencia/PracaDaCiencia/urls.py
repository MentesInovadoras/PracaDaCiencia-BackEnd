"""
URL configuration for PracaDaCiencia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import routers
from .viewsets import TecnicoViewset, VisitaViewset, RoteiroViewset, UnidadeDeEnsinoViewset, GuiasViewset, MunicipioViewset

schema_view = get_schema_view(
    openapi.Info(
        title="API?", #Nome
        default_version="v1", #Versão
        description="Documentação (aparentemente) usando Swagger (aparentemente)",
        terms_of_service="https://www.google.com/policies/terms/", #Termos
        contact=openapi.Contact(email=""), #Contato ?
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r"tecnicos", TecnicoViewset, basename="Tecnico") #Registra o modelo Tecnico no router
router.register(r"visitas", VisitaViewset, basename="Visita") #Registra o modelo Visita no router
router.register(r"roteiros", RoteiroViewset, basename="Roteiro") #Registra o modelo Roteiro no router
router.register(r"unidades", UnidadeDeEnsinoViewset, basename="UnidadeDeEnsino") #Registra o modelo UnidadeDeEnsino no router
router.register(r"guias", GuiasViewset, basename="Guias") #Registra o modelo Guias no router
router.register(r"municipios", MunicipioViewset, basename="Municipio") #Registra o modelo Municipio no router

urlpatterns = [
    path("", include(router.urls)), #Inclui as urls do app PracaDaCiencia
    path('', lambda request: redirect('/swagger/')), #Redireciona para o Swagger
    path('admin/', admin.site.urls),
     # Rotas do Swagger (Especificações)
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger\.json$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
