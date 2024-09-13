from django.shortcuts import render
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as authlogin
from django.contrib.auth.forms import UserCreationForm
from .forms import FormUser
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def registrar(request):
    """ Faz o cadastrro de um novo usuário"""
    if request.method != 'POST':
        # exibi o formulário em branco
        form = UserCreationForm()
    else:
        #processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            
            new_authenticate = authenticate(username = new_user.username, password=request.POST['password1'])
            authlogin(request, new_authenticate)
            return HttpResponseRedirect(reverse('topics'))
        else:
            print("Formulário inválido:", form.errors)
    context = {'form': form}
    return render(request, 'users/cadastro.html', context)

def logout_views(request):
    """ Faz o logout do usuário """
    logout(request)
    return HttpResponseRedirect(reverse('init'))

def login(request):
    if request.method == 'POST':
        form = FormUser(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                authlogin(request, user)  # Faz o login do usuário
                return HttpResponseRedirect(reverse('topics'))  # Redireciona para 'topics'
            else:
                form.add_error(None, "Nome de usuário ou senha inválidos.")
    else:
        form = FormUser()

    contexto = {'form': form}
    return render(request, 'users/login.html', contexto)