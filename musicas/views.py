from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Musica
from .models import UserResps
from django.contrib import auth

@login_required(redirect_field_name='login')
def index(request):
    musicas = Musica.objects.filter().all()
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    for li in lista:
        if li.acertou:
            pontuacao += 1
    return render(request, 'musicas/index.html', {'musicas': musicas, 'lista': lista, 'pontuacao': pontuacao})