from rest_framework import generics
from .models import Cliente, Agendamento
from .serializers import ClienteSerializer, AgendamentoSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ClienteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class AgendamentoListCreate(generics.ListCreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated]  # Garantir que apenas usuários autenticados possam acessar

    def perform_create(self, serializer):
        """
        Método para sobrescrever a criação do agendamento, associando automaticamente o cliente
        logado ao agendamento.
        """
        # Obtém o cliente do usuário autenticado
        cliente = self.request.user.cliente  # Supondo que você tenha um modelo `Cliente` relacionado ao usuário

        # Cria o agendamento e associa o cliente automaticamente
        serializer.save(cliente=cliente)
        
        # Retorna uma resposta com o agendamento criado
        return Response(serializer.data, status=201)
