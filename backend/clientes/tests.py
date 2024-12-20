from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from clientes.models import Cliente, Salao


class ClienteTests(TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.client = APIClient()

        # Criação de um salão
        self.salao = Salao.objects.create(
            nome="Salão Exemplo",
            endereco="Rua Teste, 123",
            telefone="123456789"
        )

        # Dados de exemplo para um cliente
        self.cliente_data = {
            "nome": "Cliente Teste",
            "telefone": "987654321",
            "email": "cliente@teste.com",
            "salao": self.salao.id,  # Use o ID do salão, não a instância
        }

        # Criação de um cliente no banco
        self.cliente = Cliente.objects.create(
            nome="Cliente Existente",
            telefone="123456789",
            email="existente@teste.com",
            salao=self.salao
        )

    def test_list_clientes(self):
        """
        Testa se a API retorna a lista de clientes.
        """
        url = reverse("clientes:cliente-list-create")
        response = self.client.get(url, format="json")

        # Verifica se a resposta está correta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Cliente.objects.count())

    def test_create_cliente(self):
        """
        Testa a criação de um novo cliente.
        """
        url = reverse("clientes:cliente-list-create")
        response = self.client.post(url, self.cliente_data, format="json")

        # Verifica se o cliente foi criado corretamente
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)  # Deve haver dois clientes agora
        self.assertEqual(response.data["nome"], self.cliente_data["nome"])

    def test_retrieve_cliente(self):
        """
        Testa se é possível recuperar os detalhes de um cliente específico.
        """
        url = reverse("clientes:cliente-detail", args=[self.cliente.id])
        response = self.client.get(url, format="json")

        # Verifica se a resposta está correta
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["nome"], self.cliente.nome)

    def test_update_cliente(self):
        """
        Testa a atualização dos dados de um cliente.
        """
        url = reverse("clientes:cliente-detail", args=[self.cliente.id])
        updated_data = {
            "nome": "Cliente Atualizado",
            "telefone": "987654321",
            "email": "atualizado@teste.com",
            "salao": self.salao.id,  # Ainda referenciando o salão existente
        }
        response = self.client.put(url, updated_data, format="json")

        # Verifica se o cliente foi atualizado corretamente
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nome, updated_data["nome"])

    def test_delete_cliente(self):
        """
        Testa a exclusão de um cliente.
        """
        url = reverse("clientes:cliente-detail", args=[self.cliente.id])
        response = self.client.delete(url, format="json")

        # Verifica se o cliente foi deletado corretamente
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)
