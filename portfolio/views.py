# portfolio/views.py

from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm


def lista_projetos(request):
    projetos = (Projeto.objects
                .select_related('unidade_curricular')
                .prefetch_related('tecnologias', 'competencias')
                .all())
    return render(request, 'portfolio/lista_projetos.html', {'projetos': projetos})


def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_projetos')
    else:
        form = ProjetoForm()
    
    return render(request, 'portfolio/form_projeto.html', {
        'form': form,
        'titulo': 'Novo Projeto',
    })