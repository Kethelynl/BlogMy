from django.db import models
from django.contrib.auth.models import User


class Topicos(models.Model):
    """ Responsável por cadastrar os tópicos """
    text = models.CharField(max_length=200)
    data_add = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Devolve uma apresentação em string para o banco de dados"""
        return self.text
    
class Entrada(models.Model):
    """Responsável por cadastrar os textos dentro de cada topico"""
    topic = models.ForeignKey(Topicos, on_delete=models.CASCADE)
    text = models.TextField()
    imagem = models.ImageField(upload_to='upload_to_assunto', null=True, blank=True)
    data_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50]

class Perfil(models.Model):
    """Responsável pela foto do usuário"""
    foto = models.ImageField(upload_to='perfil_foto', blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Foto do usuário {self.usuario.username}"