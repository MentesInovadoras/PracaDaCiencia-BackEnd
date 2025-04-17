from rest_framework import status
from rest_framework.response import Response


class ErroTentandoMarcarAgendamentoAlem2Meses(Response):
    def __init__(self):
        Response.__init__(self, "Atenção, você tentou buscar informação para além de 2 meses no futuro.", status.HTTP_403_FORBIDDEN, None, None, None, None)
        

class ErroValorDeMesInvalido(Response):
    def __init__(self):
        Response.__init__(self, "Atenção, valores negativos e maiores que 11 não são permitidos. Considere que Janeiro inicia em 0.", status.HTTP_403_FORBIDDEN, None, None, None, None)
        
        