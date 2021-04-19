from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from musicas.models import Musica
from musicas.models import UserResps
from django.contrib import auth
# Create your views here.
@login_required(redirect_field_name='login')
def listajogos(request):
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    for li in lista:
        if li.acertou:
            pontuacao += 1
    return render(request, 'animes/listajogos.html', {'pontuacao': pontuacao})

@login_required(redirect_field_name='login')
def animefase1(request):
    musicas = Musica.objects.filter(fase='1')
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    for li in lista:
        if li.acertou:
            pontuacao += 1
    return render(request, 'animes/animefase1.html', {'musicas': musicas, 'lista': lista, 'pontuacao': pontuacao})

@login_required(redirect_field_name='login')
def validar(request, musica_id):
    musicas = get_object_or_404(UserResps, id=musica_id)
    texto = request.GET.get('escrito')
    texto = texto.lower()

    if musicas.respostas_lista.nome == texto:
        musicas.acertou = True
        musicas.save()
        return redirect('animefase1')
    else:
        musicas.acertou = False
        musicas.save()
        return redirect('animefase1')
