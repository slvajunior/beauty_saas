from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Salao, Servico, Cliente, Agendamento
from django.utils.timezone import make_aware
from datetime import datetime
from rest_framework.test import APITestCase


class SalaoModelTestCase(TestCase):
    def setUp(self):
        self.salao = Salao.objects.create(
            nome="Salão Beleza",
            endereco="Rua das Flores, 123",
            telefone="123456789",
            cnpj="12345678000123",
        )

    def test_salao_str(self):
        self.assertEqual(str(self.salao), "Salão Beleza")


class ServicoModelTestCase(TestCase):
    def setUp(self):
        self.salao = Salao.objects.create(
            nome="Salão Beleza",
            endereco="Rua das Flores, 123",
            telefone="123456789",
            cnpj="12345678000123",
        )
        self.servico = Servico.objects.create(
            salao=self.salao,
            nome="Corte de Cabelo",
            descricao="Corte de cabelo moderno",
            preco=50.00,
            duracao=30,
        )

    def test_servico_str(self):
        self.assertEqual(str(self.servico), "Corte de Cabelo")


class AgendamentoModelTestCase(TestCase):
    def setUp(self):
        self.salao = Salao.objects.create(
            nome="Salão Beleza",
            endereco="Rua das Flores, 123",
            telefone="123456789",
            cnpj="12345678000123",
        )
        self.cliente = Cliente.objects.create(
            nome="Cliente Teste",
            email="cliente@teste.com",
            telefone="987654321",
        )
        self.servico = Servico.objects.create(
            salao=self.salao,
            nome="Corte de Cabelo",
            descricao="Corte de cabelo moderno",
            preco=50.00,
            duracao=30,
        )
        self.agendamento = Agendamento.objects.create(
            cliente=self.cliente,
            servico=self.servico,
            salao=self.salao,
            data=make_aware(datetime(2024, 12, 21, 14, 0)),
            status="pendente",
        )

    def test_agendamento_str(self):
        # Formatar a data sem o fuso horário
        agendamento_str = f"Agendamento de {
            self.agendamento.servico.nome} para {
                self.agendamento.cliente.nome} no salão {
                    self.agendamento.salao.nome} em {
                        self.agendamento.data.strftime('%Y-%m-%d %H:%M:%S')}"
        self.assertEqual(str(self.agendamento), agendamento_str)


class SalaoAPITestCase(APITestCase):

    def setUp(self):
        # Instanciando o client da API para fazer requisições
        self.client = APIClient()

        # Dados de um salão para teste
        self.salao_data = {
            "nome": "Salão Teste",
            "endereco": "Rua Teste, 123",
            "telefone": "(11) 12345-6789",
            "cnpj": "48367987000103",  # Certifique-se que o CNPJ é válido
        }

        # URL para criar e listar os salões
        self.url = reverse("saloes-list-create")

    def test_list_saloes(self):
        """
        Testa a listagem de salões.
        """
        # Criação de um salão no banco de dados para testar a listagem
        Salao.objects.create(**self.salao_data)

        # Realiza a requisição GET para listar salões
        response = self.client.get(self.url, format="json")

        # Verifica se o status da resposta é OK (200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se o número de salões na resposta é 1
        self.assertEqual(len(response.data), 1)

        # Verifica se o nome do salão listado é "Salão Teste"
        self.assertEqual(response.data[0]["nome"], "Salão Teste")

    def test_create_salao(self):
        """
        Testa a criação de um novo salão.
        """
        response = self.client.post(self.url, self.salao_data, format="json")
        print(response.data)  # Imprime os erros detalhados
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], self.salao_data["nome"])
        self.assertEqual(response.data["cnpj"], self.salao_data["cnpj"])
