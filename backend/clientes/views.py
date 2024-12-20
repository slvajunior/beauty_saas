from rest_framework import generics
from .models import Cliente, Agendamento
from .serializers import ClienteSerializer, AgendamentoSerializer


class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class AgendamentoListCreate(generics.ListCreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
