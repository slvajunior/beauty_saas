from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalaoViewSet, ServicoViewSet, ClienteViewSet, AgendamentoViewSet
from .views import SalaoListCreate, SalaoDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SalaoListView

router = DefaultRouter()
router.register(r'saloes', SalaoViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'agendamentos', AgendamentoViewSet)

urlpatterns = [
    path('salões/', SalaoListView.as_view(), name='salão-lista'),
    path('api/', include(router.urls)),
    path('saloes/', SalaoListCreate.as_view(), name='saloes-list-create'),
    path('saloes/<int:pk>/', SalaoDetail.as_view(), name='saloes-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
