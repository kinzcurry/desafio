from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from accounts import admin
from musicas.models import Musica
from musicas.models import UserDicas
from musicas.models import UserResps
from django.contrib import auth, messages


# Create your views here.

# Cria o banco de dados do usuario quando ele clicar em jogar naquele tema
def criarbd(request, tipolista):
    user = auth.get_user(request)
    musica = Musica.objects.filter(tipo=tipolista)
    dicasuser = UserDicas.objects.filter(usuario__username__iexact=user, fase=tipolista)
    if not dicasuser:
        dicas = UserDicas(usuario=user, fase=tipolista, qtd_dicas=5, pontuacaotema=0)
        dicas.save()
    cont = 0
    while cont < len(musica):
        resp = UserResps(usuario=user, respostas_lista=musica[cont], acertou=False)
        resp.save()
        cont += 1


# Lista os 4 niveis do jogo dos animes
@login_required(redirect_field_name='login')
def listajogos(request):
    # acertartudo()
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    cont = 0
    for li in lista:
        if li.respostas_lista.tipo == 'anime':
            cont += 1
            if li.acertou:
                pontuacao += 1
    if cont == 0:
        tipolista = 'anime'
        criarbd(request, tipolista)
    return render(request, 'animes/listajogos.html', {'pontuacao': pontuacao})


# Lista os 4 niveis do jogo dos filmes
@login_required(redirect_field_name='login')
def listafilmes(request):
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    cont = 0
    for li in lista:
        if li.respostas_lista.tipo == 'filme':
            cont += 1
            if li.acertou:
                pontuacao += 1
    if cont == 0:
        tipolista = 'filme'
        criarbd(request, tipolista)
    return render(request, 'animes/listafilmes.html', {'pontuacao': pontuacao})


def listajogos3e4(request):
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    cont = 0
    for li in lista:
        if li.respostas_lista.tipo == 'jogos3e4':
            cont += 1
            if li.acertou:
                pontuacao += 1
    if cont == 0:
        tipolista = 'jogos3e4'
        criarbd(request, tipolista)
    return render(request, 'animes/listajogos3e4.html', {'pontuacao': pontuacao})

def listajogos5(request):
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    cont = 0
    for li in lista:
        if li.respostas_lista.tipo == 'jogos5':
            cont += 1
            if li.acertou:
                pontuacao += 1
    if cont == 0:
        tipolista = 'jogos5'
        criarbd(request, tipolista)
    return render(request, 'animes/listajogos5.html', {'pontuacao': pontuacao})

def listaseries(request):
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontuacao = 0
    cont = 0
    for li in lista:
        if li.respostas_lista.tipo == 'series':
            cont += 1
            if li.acertou:
                pontuacao += 1
    if cont == 0:
        tipolista = 'series'
        criarbd(request, tipolista)
    return render(request, 'animes/listaseries.html', {'pontuacao': pontuacao})

# Acha o tema escolhido pelo jogador
def achartema(request, num):
    if num <= 4:
        tema = "anime"
        return tema
    elif 4 < num <= 8:
        tema = "filme"
        return tema
    elif 8 < num <= 12:
        tema = 'jogos3e4'
        return tema
    elif 12 < num <= 16:
        tema = 'series'
        return tema
    elif 16 < num <= 20:
        tema = 'jogos5'
        return tema


# Define a proxima fase e a anterior
def valfase(request, tema, num):
    ante = 0
    prox = 0
    if tema == "anime":
        if num == 1:
            ante = 1
            prox = num + 1
        elif num == 4:
            prox = 4
            ante = num - 1
        else:
            ante = num - 1
            prox = num + 1

    elif tema == "filme":
        if num == 5:
            ante = 5
            prox = num + 1
        elif num == 8:
            ante = num - 1
            prox = 8
        else:
            ante = num - 1
            prox = num + 1

    elif tema == "jogos3e4":
        if num == 9:
            ante = 9
            prox = num + 1
        elif num == 12:
            ante = num - 1
            prox = 12
        else:
            ante = num - 1
            prox = num + 1

    elif tema == "series":
        if num == 13:
            ante = 13
            prox = num + 1
        elif num == 16:
            ante = num - 1
            prox = 16
        else:
            ante = num - 1
            prox = num + 1

    elif tema == "jogos5":
        if num == 17:
            ante = 17
            prox = num + 1
        elif num == 20:
            ante = num - 1
            prox = 20
        else:
            ante = num - 1
            prox = num + 1

    return ante, prox


# Calcula os pontos do jogador
def pontosjogador(request, num, tema):
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    pontofase = 0
    pontotema = 0
    for li in lista:
        if li.respostas_lista.tipo == tema:
            if li.acertou:
                pontotema += 1
                if li.respostas_lista.fase == num:
                    pontofase += 1
    return pontotema, pontofase


# Calcula se o jogador pode ir pra proxima fase
def proxfase(request, pontotema, num):
    podepassar = False
    if pontotema >= 45:
        podepassar = True
        return podepassar
    elif pontotema >= 30:
        if num == 1 or num == 2 or num == 5 or num == 6 or num == 9 or num == 10 or num == 13 or num == 14 or num == 17 or num == 18:
            podepassar = True
            return podepassar
    elif pontotema >= 15:
        if num == 1 or num == 5 or num == 9 or num == 13 or num == 17:
            podepassar = True
            return podepassar
    else:
        return podepassar


# Calcula a quantidade de dicas do jogador
def qtddica(request, user, tema):
    dicas = UserDicas.objects.filter(usuario__username__iexact=user, fase=tema)
    for dica in dicas:
        return dica.qtd_dicas

# Gera a fase de jogo
@login_required(redirect_field_name='login')
def animefase(request, num, focus):
    musicas = Musica.objects.filter(fase=num)
    user = auth.get_user(request)
    lista = UserResps.objects.filter(usuario__username__iexact=user)
    # music = Musica.objects.filter(fase__lte=num)
    tema = achartema(request, num)
    temamaisculo = tema.capitalize()
    ante, prox = valfase(request, tema, num)
    pontotema, pontofase = pontosjogador(request, num, tema)
    podepassar = proxfase(request, pontotema, num)
    achardica = qtddica(request, user, tema)
    return render(request, 'animes/animefase.html',
                  {'musicas': musicas, 'lista': lista, 'pontofase': pontofase, 'pontotema': pontotema,
                   'podepassar': podepassar,
                   'focus': focus, 'prox': prox, 'ante': ante, 'temamaisculo': temamaisculo, 'achardica': achardica})


# Valida se o jogador acertou a musica
def validar(request, musica_id):
    user = auth.get_user(request)
    musicas = get_object_or_404(UserResps, id=musica_id)
    pontosdicas = UserDicas.objects.filter(usuario__username=user, fase=musicas.respostas_lista.tipo)
    texto = request.GET.get('escrito')
    texto = texto.lower()
    focus = musica_id

    # Esse num é a fase, para poder passar o id que ficará com o focus
    num = musicas.respostas_lista.fase
    if texto == "":
        return redirect('animefase', num, focus)
    if musicas.respostas_lista.nome == texto:
        for pontos in pontosdicas:
            pontos.pontuacaotema += 1
            if pontos.pontuacaotema == 15:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 30:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 45:
                pontos.qtd_dicas += 3
            pontos.save()
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
        # return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    elif musicas.respostas_lista.nome2 == texto:
        for pontos in pontosdicas:
            pontos.pontuacaotema += 1
            if pontos.pontuacaotema == 15:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 30:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 45:
                pontos.qtd_dicas += 3
            pontos.save()
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
    elif musicas.respostas_lista.nome3 == texto:
        for pontos in pontosdicas:
            pontos.pontuacaotema += 1
            if pontos.pontuacaotema == 15:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 30:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 45:
                pontos.qtd_dicas += 3
            pontos.save()
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
    elif musicas.respostas_lista.nome4 == texto:
        for pontos in pontosdicas:
            pontos.pontuacaotema += 1
            if pontos.pontuacaotema == 15:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 30:
                pontos.qtd_dicas += 3
            elif pontos.pontuacaotema == 45:
                pontos.qtd_dicas += 3
            pontos.save()
        musicas.acertou = True
        musicas.save()
        return redirect('animefase', num, focus)
    else:
        musicas.acertou = False
        musicas.save()
        return redirect('animefase', num, focus)
        # return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@user_passes_test(lambda u: u.is_superuser)
def listarmusicas(request):
    musicas = Musica.objects.filter().all()
    return render(request, 'animes/listarmusicas.html', {'musicas': musicas})


def geracaodegames(request):
    return render(request, 'animes/geracaodegames.html')


def geracaodefilmes(request):
    return render(request, 'animes/geracaodefilmes.html')


def geracaodeseries(request):
    return render(request, 'animes/geracaodeseries.html')


def geracaodeanimes(request):
    return render(request, 'animes/geracaodeanimes.html')


def buscarusuario (request):
    nome = request.GET.get('usuario')
    usu = UserResps.objects.filter(usuario__username=nome)
    for us in usu:
        us.acertou = True
        us.save()

    return redirect('listarmusicas')