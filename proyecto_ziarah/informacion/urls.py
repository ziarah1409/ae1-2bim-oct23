"""
    Manejo de urls para la aplicación
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('listarPaises', views.listarPaises, name='listarPaises'),
        path('', views.listarPaises, name='listarPaises'),
        path('listarBarrios', views.listarBarrios, name='listarBarrios'),
 ]