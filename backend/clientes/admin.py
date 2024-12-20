from django.contrib import admin
from .models import Cliente, Agendamento


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')  # Exiba os campos mais relevantes
    search_fields = ('nome', 'email')            # Permita busca por nome e email
    list_filter = ('criado_em',)              # Filtro por data de criação


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'data_hora', 'confirmado')
    search_fields = ('cliente',)
    list_filter = ('data_hora', 'confirmado')
