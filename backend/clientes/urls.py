from django.urls import path
from .views import ClienteListCreate, AgendamentoListCreate
from clientes.views import ClienteDetailView

app_name = "clientes"

urlpatterns = [
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('agendamentos/', AgendamentoListCreate.as_view(), name='agendamento-list-create'),
    path("clientes/<int:pk>/", ClienteDetailView.as_view(), name="cliente-detail"),

]
