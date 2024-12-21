from django.db import models
from core.models import Salao  # Usando "Salao" sem acento


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, null=True, blank=True)  # Opcional
    salao = models.ForeignKey(Salao, on_delete=models.CASCADE, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.CharField(max_length=255)  # Sem acento
    data_hora = models.DateTimeField()
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f'Agendamento para {self.cliente.nome} no {self.data_hora}'
