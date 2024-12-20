from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgendamentoViewSet, SalaoViewSet, ServicoViewSet, ClienteViewSet
from .views import SalaoListCreate, SalaoDetail, SalaoListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AgendamentoDetailView
from . import views

# Definição do router
router = DefaultRouter()
router.register(r'saloes', SalaoViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'agendamentos', AgendamentoViewSet, basename='agendamento')

# Rotas
urlpatterns = [
    path('salões/', SalaoListView.as_view(), name='salão-lista'),
    path('api/', include(router.urls)),
    path('api/saloes/', SalaoListCreate.as_view(), name='saloes-list-create'),
    path('saloes/<int:pk>/', SalaoDetail.as_view(), name='saloes-detail'),
    path('api/saloes/', views.SalaoViewSet.as_view({'post': 'create'}), name='salao-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('agendamentos/<int:pk>/', AgendamentoDetailView.as_view(), name='agendamento-detail'),
]
