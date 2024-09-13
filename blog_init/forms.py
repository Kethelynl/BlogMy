from django import forms
from .models import Topicos, Entrada, Perfil

    
class NovoTopico(forms.ModelForm):
    class Meta:
        model = Topicos
        fields = ['text']
        labels = {'text': ''}

class NovaEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['text', 'imagem']
        labels = {'text': 'Escreva o assunto', 'imagem': 'Upload de imagem (não obrigatório)'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class FotoForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']
        labels = {'foto': 'Upload de imagem (não obrigatório)'}
        