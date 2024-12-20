from rest_framework import serializers
from .models import Salao, Servico, Cliente, Agendamento
from .utils import validar_cnpj
from django.core.validators import RegexValidator


class SalaoSerializer(serializers.ModelSerializer):
    # Validação do telefone
    telefone = serializers.CharField(
        max_length=15,
        required=False,  # Se for opcional, senão remova
        validators=[
            RegexValidator(r"^\(\d{2}\)\s\d{5}-\d{4}$", "Formato de telefone inválido.")
        ],
    )

    cnpj = serializers.CharField(
        max_length=14,
        min_length=14,
    )

    class Meta:
        model = Salao
        fields = ["nome", "cnpj", "endereco", "telefone"]

    def validate_cnpj(self, value):
        if not validar_cnpj(value):
            raise serializers.ValidationError("CNPJ inválido.")
        return value


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = "__all__"
