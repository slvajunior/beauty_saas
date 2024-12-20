from django.urls import path
from .views import ClienteListCreate, AgendamentoListCreate

urlpatterns = [
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('agendamentos/', AgendamentoListCreate.as_view(), name='agendamento-list-create'),
]
