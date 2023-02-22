from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
        return redirect('/auth/cadastro')

    if len(username.strip()) == 0 or len(senha.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
        return redirect('/auth/cadastro')

    user = User.objects.filter(username=username)
    if user.exists():
        messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
        
    try:
        user = User.objects.create_user(username=username, password=senha)
        user.save()
        return redirect('/auth/logar')
    except:        
        return redirect('/auth/cadastro')


def logar(request):    
    if request.method == "GET":
        return render(request, 'login.html')