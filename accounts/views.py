from django.contrib import auth
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
        # messages.error(request, 'Todos os campos precisam ser preenchidos')
        print('preencha todos os campos')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        # messages.error(request, 'Email invalido')
        print('email inválido')
        return render(request, 'accounts/register.html')
    if senha != senha2:
        # messages.error(request, 'Senhas estão diferentes')
        print('Senhas estão diferentes')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        # messages.error(request, 'Usuário já cadastrado')
        print('usuario já cadastrado')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        # messages.error(request, 'Email já cadastrado')
        print('email já existe')
        return render(request, 'accounts/register.html')
    # messages.success(request, 'Registrado com sucesso')
    print('registrado com sucesso')
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome)
    user.save()

    musica = Musica.objects.filter().all()
    cont = 0
    while cont < len(musica):
        resp = UserResps(usuario=user, respostas_lista=musica[cont], acertou=False)
        resp.save()
        cont += 1

    print(UserResps.objects.filter(usuario__username__iexact=user))
    return redirect('login')

def logout(request):
    auth.logout(request)
    return render(request, 'accounts/login.html')