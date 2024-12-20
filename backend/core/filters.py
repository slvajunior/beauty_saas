# beauty_saas/core/filters.py

import django_filters
from .models import Salao


class SalaoFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains', label='Nome')
    cnpj = django_filters.CharFilter(lookup_expr='exact', label='CNPJ')
    telefone = django_filters.CharFilter(lookup_expr='icontains', label='Telefone')
    endereco = django_filters.CharFilter(lookup_expr='icontains', label='Endereço')

    class Meta:
        model = Salao
        fields = ['nome', 'cnpj', 'telefone', 'endereco']
