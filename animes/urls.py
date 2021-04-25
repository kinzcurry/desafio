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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
