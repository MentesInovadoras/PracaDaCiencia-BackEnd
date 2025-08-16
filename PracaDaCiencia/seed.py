from django.contrib.auth.models import User
from apps.administrador.models import Tecnico, Guias, Visita, StatusVisita
from apps.visitantes.models import UnidadeDeEnsino, Roteiro, Visitante
from django.utils import timezone

# Usuários
u1, _ = User.objects.get_or_create(username='tecnico1', defaults={'email':'tec1@example.com'})
u1.set_password('123456'); u1.save()

u2, _ = User.objects.get_or_create(username='tecnico2', defaults={'email':'tec2@example.com'})
u2.set_password('123456'); u2.save()

# Técnicos
Tecnico.objects.get_or_create(user=u1)
Tecnico.objects.get_or_create(user=u2)

# Guias
g1, _ = Guias.objects.get_or_create(nome='Guia Histórico')
g2, _ = Guias.objects.get_or_create(nome='Guia Científico')

# Unidades de Ensino
ue1, _ = UnidadeDeEnsino.objects.get_or_create(municipio='Serra/ES', nome_responsavel='Maria Silva', tipo='Pública', escolaridade='Fundamental1')
ue2, _ = UnidadeDeEnsino.objects.get_or_create(municipio='Vitória/ES', nome_responsavel='João Santos', tipo='Privada', escolaridade='Médio')

# Roteiros
r1, _ = Roteiro.objects.get_or_create(nome='Roteiro Cultural', ensino=False, status=True)
r2, _ = Roteiro.objects.get_or_create(nome='Roteiro Educacional', ensino=True, status=True)

# Visitantes
v1, _ = Visitante.objects.get_or_create(tipo_visita='Pessoa Física', data_visita=timezone.now(), nome='Carlos Oliveira', email='carlos@example.com', telefone='27999990001', roteiro=r1)
v2, _ = Visitante.objects.get_or_create(tipo_visita='Unidade de Ensino', data_visita=timezone.now(), nome='Escola Municipal ABC', email='contato@abc.com', telefone='27999990002', roteiro=r2, instituicao=ue1)

# Visitas
Visita.objects.get_or_create(observacao='Visita para estudo de campo', status=StatusVisita.Agendado, guia=g1, visitante=v1)
Visita.objects.get_or_create(observacao='Visita realizada com sucesso', status=StatusVisita.Realizado, guia=g2, visitante=v2)

print("✅ Seeds inseridas com sucesso.")
