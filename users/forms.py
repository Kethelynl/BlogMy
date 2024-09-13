from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class FormUser(forms.Form):
    username = forms.CharField(max_length=150, label='Nome de usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')