from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from musicas.models import UserResps, Musica

# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        print('não logado')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        print('logado')
        return redirect('index')

    return render(request, 'accounts/login.html')


def register(request):
    print('entrou')
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Todos os campos precisam ser preenchidos')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email invalido')
        return render(request, 'accounts/register.html')
    if senha != senha2:
        messages.error(request, 'Senhas estão diferentes')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já cadastrado')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Registrado com sucesso')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)
    user.save()
    return redirect('login')

def logout(request):
    auth.logout(request)
    return render(request, 'accounts/login.html')

def convidado(request):
    userguest = User.objects.latest('id')
    usuario = 'guest' + str(userguest.id)
    email = usuario + '@' + usuario + '.com'
    senha = 'master'
    nome = usuario
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)
    user.save()
    user = auth.authenticate(request, username=usuario, password=senha)
    auth.login(request, user)
    return redirect('index')