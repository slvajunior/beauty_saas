from rest_framework import viewsets
from .models import Salao, Servico, Cliente, Agendamento
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .filters import SalaoFilter
from clientes.serializers import ClienteSerializer, AgendamentoSerializer
from .serializers import SalaoSerializer, ServicoSerializer
from rest_framework.test import APITestCase
from django.urls import reverse


class SalaoViewSet(viewsets.ModelViewSet):
    queryset = Salao.objects.all()
    serializer_class = SalaoSerializer


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer


class SalaoListCreate(APIView):
    def get(self, request):
        saloes = Salao.objects.all()
        serializer = SalaoSerializer(saloes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SalaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalaoDetail(APIView):
    def get(self, request, pk):
        try:
            salao = Salao.objects.get(pk=pk)
        except Salao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SalaoSerializer(salao)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            salao = Salao.objects.get(pk=pk)
        except Salao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SalaoSerializer(salao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            salao = Salao.objects.get(pk=pk)
        except Salao.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        salao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SalaoListView(generics.ListCreateAPIView):
    queryset = Salao.objects.all()
    serializer_class = SalaoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SalaoFilter


class SalaoViewTest(APITestCase):
    def test_create_salao_view(self):
        url = reverse('salao-list')
        data = {
            "nome": "Salão Teste",
            "endereco": "Rua Teste, 123",
            # outros campos necessários
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AgendamentoDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            agendamento = Agendamento.objects.get(pk=pk)
            serializer = AgendamentoSerializer(agendamento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Agendamento.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
