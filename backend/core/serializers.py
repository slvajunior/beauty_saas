from rest_framework import serializers
from .utils import validar_cnpj
from django.core.validators import RegexValidator
from .models import Salao, Servico


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
