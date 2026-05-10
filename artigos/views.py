from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from .models import Artigo, Like, Comentario
from .forms import ArtigoForm


def is_autor(user):
    return user.is_authenticated and user.groups.filter(name='autores').exists()


def lista_artigos(request):
    artigos = Artigo.objects.select_related('autor').all()
    return render(request, 'artigos/lista_artigos.html', {
        'artigos': artigos,
        'is_autor': is_autor(request.user),
    })


def detalhe_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)
    comentarios = artigo.comentarios.select_related('autor').all()
    total_likes = artigo.likes.count()

    if request.user.is_authenticated:
        user_liked = artigo.likes.filter(utilizador=request.user).exists()
    else:
        sk = request.session.session_key or ''
        user_liked = artigo.likes.filter(session_key=sk).exists() if sk else False

    return render(request, 'artigos/detalhe_artigo.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'total_likes': total_likes,
        'user_liked': user_liked,
        'is_autor': is_autor(request.user),
        'e_o_autor': request.user == artigo.autor,
    })


def criar_artigo(request):
    if not is_autor(request.user):
        return redirect('accounts:login')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES)
        if form.is_valid():
            artigo = form.save(commit=False)
            artigo.autor = request.user
            artigo.save()
            return redirect('artigos:detalhe_artigo', id=artigo.id)
    else:
        form = ArtigoForm()

    return render(request, 'artigos/form_artigo.html', {
        'form': form,
        'titulo_pagina': 'Novo Artigo',
    })


def editar_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if not is_autor(request.user) or artigo.autor != request.user:
        return redirect('artigos:lista_artigos')

    if request.method == 'POST':
        form = ArtigoForm(request.POST, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('artigos:detalhe_artigo', id=artigo.id)
    else:
        form = ArtigoForm(instance=artigo)

    return render(request, 'artigos/form_artigo.html', {
        'form': form,
        'titulo_pagina': 'Editar Artigo',
        'artigo': artigo,
    })


def apagar_artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id)

    if not is_autor(request.user) or artigo.autor != request.user:
        return redirect('artigos:lista_artigos')

    if request.method == 'POST':
        artigo.delete()
        return redirect('artigos:lista_artigos')

    return render(request, 'artigos/confirmar_apagar.html', {'artigo': artigo})


def toggle_like(request, id):
    if request.method != 'POST':
        return redirect('artigos:detalhe_artigo', id=id)

    artigo = get_object_or_404(Artigo, id=id)

    if request.user.is_authenticated:
        like, criado = Like.objects.get_or_create(artigo=artigo, utilizador=request.user)
        if not criado:
            like.delete()
    else:
        if not request.session.session_key:
            request.session.create()
        sk = request.session.session_key
        like, criado = Like.objects.get_or_create(artigo=artigo, session_key=sk)
        if not criado:
            like.delete()

    return redirect('artigos:detalhe_artigo', id=id)


def adicionar_comentario(request, id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    artigo = get_object_or_404(Artigo, id=id)

    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        if texto:
            Comentario.objects.create(artigo=artigo, autor=request.user, texto=texto)

    return redirect('artigos:detalhe_artigo', id=id)
