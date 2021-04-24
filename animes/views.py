from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
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
def animefase(request, num, focus):
    musicas = Musica.objects.filter(fase=num)
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    music = Musica.objects.filter(fase__lte=num)
    if num == 1 or 2 or 3 or 4:
        tema = "anime"

    for li in lista:
        for mu in music:
            if li.respostas_lista == mu:
                if mu.tipo == tema:
                    if mu.fase == num:
                        if li.acertou:
                            pontuacao += 1
    return render(request, 'animes/animefase.html', {'musicas': musicas, 'lista': lista, 'pontuacao': pontuacao, 'focus': focus})

def validar(request, musica_id):
    musicas = get_object_or_404(UserResps, id=musica_id)
    texto = request.GET.get('escrito')
    texto = texto.lower()
    focus = musica_id

    # Esse num é a fase, para poder passar o id que ficará com o focus
    num = musicas.respostas_lista.fase
    if texto == "":
        return redirect('animefase', num, focus)
    if musicas.respostas_lista.nome == texto:
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
        # return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    elif musicas.respostas_lista.nome2 == texto:
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
    elif musicas.respostas_lista.nome3 == texto:
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
    elif musicas.respostas_lista.nome4 == texto:
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
    else:
        musicas.acertou = False
        musicas.save()
        return redirect('animefase', num, focus)
        # return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

