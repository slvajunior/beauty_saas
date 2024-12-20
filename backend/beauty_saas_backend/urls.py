# beauty_saas_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Definindo o esquema da documentação da API
schema_view = get_schema_view(
    openapi.Info(
        title="Beauty SaaS API",
        default_version='v1',
        description="Documentação da API do Beauty SaaS",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@beautysaas.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Rotas da API do app core
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
