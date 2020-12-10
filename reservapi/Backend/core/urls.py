from django.contrib import admin
from django.urls import path, include
from api.views import UserViewSet, AgendamentoViewSet, HotelViewSet
from rest_framework import routers
from api import views

from django.conf import settings
from django.conf.urls.static import static

# Rotas da API
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'hotels', HotelViewSet)

# Cadastro de Rotas

urlpatterns = [
    # Rotas Admin
    path('admin/', admin.site.urls),

     # Rotas Api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    # Rotas FrontEnd

    #Rotas Static Files
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
