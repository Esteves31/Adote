from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def signup(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmed_password = request.POST.get('confirmed_password')

        if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(confirmed_password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return render(request, 'signup.html')

        if password != confirmed_password:
            messages.add_message(request, constants.ERROR, 'Digite senhas iguais')
            return render(request, 'signup.html')

        try:
            user = User.objects.create_user(
                username = name,
                email = email,
                password = password,
            )
            messages.add_message(request, constants.SUCCESS, 'Seu usuário foi criado com sucesso!')
            return render(request, 'signup.html')
        except:
            messages.add_message(request, constants.ERROR, 'Desculpe, houve algum erro no sistema')
            return render(request, 'signup.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'signin.html')   
    elif request.method ==  "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username = name, password = password)

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else: 
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos!')
            return render(request, 'signin.html')

def log_out(request):
    logout(request)
    return redirect('/auth/login')


