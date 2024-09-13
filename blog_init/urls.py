
from django.urls import path
from . import views


urlpatterns = [
    path('', views.init, name='init'),
    path('myBG/', views.topics, name='topics'),
    path('topicos/', views.topicos, name='topicos'),
    path('adicionar_topico/', views.adicionarTopico, name='adicionarTopico'),
    path('apagarTopico/<int:topico_id>/', views.apagarTopico, name='apagarTopico'),
    path('assuntos/<int:topico_id>/', views.assuntos, name='assuntos'),
    path('assuntos2/', views.assuntos2, name='assuntos2'),
    path('anotações/<int:topico_id>', views.novaEntrada, name='novaEntrada'),
    path('upload_to_assunto/<int:topico_id>', views.upload_to_assunto, name='upload_to_assunto'),
    path('conteudo/<int:entrada_id>/', views.conteudo, name='conteudo'),
    path('pagarentrada/<int:entrada_id>/', views.apagarEntrada, name='apagarEntrada'),
    path('editar/<int:entrada_id>/', views.atualizarEntrada, name='atualizarEntrada'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfilfoto/', views.uploadImage, name='uploadImage'),
    path('blogMy/', views.blogall, name='blogall'),
]
