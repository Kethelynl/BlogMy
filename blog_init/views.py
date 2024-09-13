from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .forms import  NovaEntrada, NovoTopico, FotoForm
from .models import Topicos, Entrada, Perfil
from django.urls import reverse

# Create your views here.

def init(request):
    # Pagina iicial
    return render(request, 'index.html')

@login_required
def topics(request):
    return render(request, 'blog.html')

@login_required
def topicos(request):
    """ Lista todos os topicos """
    topicos = Topicos.objects.filter(owner=request.user).order_by('data_add')
    contexto = {'topicos': topicos}
    return render(request, 'topicos.html', contexto)

@login_required
def adicionarTopico(request):
    """ Registra novos tópicos"""
    if request.method != 'POST':
        form = NovoTopico()
    else:
        form = NovoTopico(request.POST)
        if form.is_valid():
            novo_topico = form.save(commit=False)
            novo_topico.owner = request.user
            novo_topico.save()
            return HttpResponseRedirect(reverse(topicos))
    contexto = {'form': form}
    return render(request, 'novotopico.html', contexto)


@login_required
def apagarTopico(request, topico_id):
    apagar = get_object_or_404(Topicos, id=topico_id)
    
    if request.method == 'POST':
        apagar.delete()
        return redirect('topicos')
    return render(request, 'topicos.html', {'apagar':apagar})

@login_required
def apagarEntrada(request, entrada_id):
    apagar = get_object_or_404(Entrada, id=entrada_id)
    topic_id = apagar.topic.id
    if request.method == 'POST':
        apagar.delete()
        return redirect('assuntos', topico_id=topic_id)
    return render(request, 'assuntos.html', {'apagar':apagar})

@login_required
def novaEntrada(request, topico_id):
    topico = Topicos.objects.get(id=topico_id)
    
    if topico.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = NovaEntrada()
    else:
        form = NovaEntrada(data=request.POST, files=request.FILES)
        if form.is_valid():
            nova_entrada = form.save(commit=False)
            nova_entrada.topic = topico 
            nova_entrada.save()
            return redirect(reverse('assuntos', args=[topico_id]))
    
    contexto = {'form': form, 'topico': topico}
    return render(request, 'novaentrada.html', contexto)

@login_required    
def assuntos(request, topico_id):
    topico = Topicos.objects.get(id=topico_id)
    
    if topico.owner != request.user:
        raise Http404
    
    entradas = topico.entrada_set.order_by('-data_add')
    contexto = {'topico':topico, 'entradas': entradas}
    return render(request, 'assuntos.html', contexto)

def assuntos2(request):
    topicos = Topicos.objects.filter(owner=request.user).order_by('data_add')
    contexto = {'topicos': topicos}
    return render(request, 'assuntos2.html', contexto)
    
@login_required
def upload_to_assunto(instance, filename):
    return f'assuntos/{instance.topic.id}/{filename}'


@login_required
def conteudo(request, entrada_id):
    entrada = get_object_or_404(Entrada, id=entrada_id)
    topic = entrada.topic
    
    
        # Requisição inicial, preenche previamente o formulárrio com a enrada atual
    form = NovaEntrada(instance=entrada)
        
    
    contexto = {'entrada':entrada, 'topico':topic, 'form': form}
    return render(request, 'conteudo.html', contexto)

@login_required
def atualizarEntrada(request, entrada_id):
    entrada = Entrada.objects.get(id=entrada_id)
    topic = entrada.topic
    
    if topic.owner != request.user:
        raise Http404
    
    
    if request.method == 'POST':
        form = NovaEntrada(instance=entrada, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('assuntos', args=[topic.id]))
    else:
        form = NovaEntrada(instance=entrada)
        
    context = {'entrada':entrada, 'form':form, 'topic':topic}
    return render(request, 'editartexto.html', context)


@login_required
def perfil(request):
    return render(request, 'perfil.html')

@login_required
def uploadImage(request):

    perfil, created = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()  
            return redirect(reverse('perfil'))
    else:
        form = FotoForm(instance=perfil)  # Exibir o formulário com a foto existente, se houver
    
    contexto = {'form': form}
    return render(request, 'perfilfoto.html', contexto)

@login_required
def blogall(request):
    entradas = Entrada.objects.all() 
    return render(request, 'blog2.html', {'entradas': entradas})