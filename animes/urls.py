from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listajogos, name='listajogos'),
    path('listafilmes/', views.listafilmes, name='listafilmes'),
    path('animefase/<int:num>/<int:focus>', views.animefase, name='animefase'),
    path('<int:musica_id>', views.validar, name='validar'),
    path('listarmusicas/', views.listarmusicas, name='listarmusicas'),
    path('listajogos3e4/', views.listajogos3e4, name='listajogos3e4'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
