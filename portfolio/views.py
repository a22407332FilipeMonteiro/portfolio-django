# portfolio/views.py

from django.shortcuts import get_object_or_404, render, redirect
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


def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    
    return render(request, 'portfolio/form_projeto.html', {
        'form': form,
        'titulo': f'Editar: {projeto.nome}',
    })

def apagar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)

    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:lista_projetos')
    
    return render(request, 'portfolio/apagar_projeto.html', {
        'projeto': projeto,
    })