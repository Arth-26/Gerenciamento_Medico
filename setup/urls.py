"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from gerenciamento.views import *

router = routers.DefaultRouter()
router.register('coordenadores', CoordenadorViewSet, basename= 'Coordenadores')
router.register('pacientes', PacienteViewSet, basename= 'Pacientes')
router.register('medicos', MedicoViewSet, basename= 'Medicos')
router.register('agendas', AgendaViewSet, basename= 'Agendas')
router.register('consultas', AgendaViewSet, basename= 'Consultas')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view())
]
