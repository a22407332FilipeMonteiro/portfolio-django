# portfolio/views.py

from django.shortcuts import get_object_or_404, render, redirect
from .models import Formacao, Projeto , Tecnologia , Competencia
from .forms import FormacaoForm, ProjetoForm , TecnologiaForm , CompetenciaForm




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


# ============ TECNOLOGIAS ============

def lista_tecnologias(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portfolio/lista_tecnologias.html', {'tecnologias': tecnologias})


def criar_tecnologia(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_tecnologias')
    else:
        form = TecnologiaForm()
    
    return render(request, 'portfolio/form_generico.html', {
        'form': form,
        'titulo': 'Nova Tecnologia',
        'voltar_url': 'portfolio:lista_tecnologias',
    })


def editar_tecnologia(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)
    
    return render(request, 'portfolio/form_generico.html', {
        'form': form,
        'titulo': f'Editar: {tecnologia.nome}',
        'voltar_url': 'portfolio:lista_tecnologias',
    })


def apagar_tecnologia(request, id):
    tecnologia = get_object_or_404(Tecnologia, id=id)

    if request.method == 'POST':
        tecnologia.delete()
        return redirect('portfolio:lista_tecnologias')
    
    return render(request, 'portfolio/apagar_generico.html', {
        'objeto': tecnologia,
        'tipo': 'tecnologia',
        'voltar_url': 'portfolio:lista_tecnologias',
    })



# ============ COMPETÊNCIAS ============

def lista_competencias(request):
    competencias = Competencia.objects.all()
    return render(request, 'portfolio/lista_competencias.html', {'competencias': competencias})


def criar_competencia(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_competencias')
    else:
        form = CompetenciaForm()
    
    return render(request, 'portfolio/form_generico.html', {
        'form': form,
        'titulo': 'Nova Competência',
        'voltar_url': 'portfolio:lista_competencias',
    })


def editar_competencia(request, id):
    competencia = get_object_or_404(Competencia, id=id)

    if request.method == 'POST':
        form = CompetenciaForm(request.POST, instance=competencia)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_competencias')
    else:
        form = CompetenciaForm(instance=competencia)
    
    return render(request, 'portfolio/form_generico.html', {
        'form': form,
        'titulo': f'Editar: {competencia.nome}',
        'voltar_url': 'portfolio:lista_competencias',
    })


def apagar_competencia(request, id):
    competencia = get_object_or_404(Competencia, id=id)

    if request.method == 'POST':
        competencia.delete()
        return redirect('portfolio:lista_competencias')
    
    return render(request, 'portfolio/apagar_generico.html', {
        'objeto': competencia,
        'tipo': 'competência',
        'voltar_url': 'portfolio:lista_competencias',
    })


    # ============ FORMAÇÕES ============

def lista_formacoes(request):
    formacoes = (Formacao.objects
                 .prefetch_related('competencias', 'tecnologias')
                 .all())
    return render(request, 'portfolio/lista_formacoes.html', {'formacoes': formacoes})


def criar_formacao(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_formacoes')
    else:
        form = FormacaoForm()
    
    return render(request, 'portfolio/form_generico.html', {
        'form': form,
        'titulo': 'Nova Formação',
        'voltar_url': 'portfolio:lista_formacoes',
    })


def editar_formacao(request, id):
    formacao = get_object_or_404(Formacao, id=id)

    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('portfolio:lista_formacoes')
    else:
        form = FormacaoForm(instance=formacao)
    
    return render(request, 'portfolio/form_generico.html', {
        'form': form,
        'titulo': f'Editar: {formacao.nome}',
        'voltar_url': 'portfolio:lista_formacoes',
    })


def apagar_formacao(request, id):
    formacao = get_object_or_404(Formacao, id=id)

    if request.method == 'POST':
        formacao.delete()
        return redirect('portfolio:lista_formacoes')
    
    return render(request, 'portfolio/apagar_generico.html', {
        'objeto': formacao,
        'tipo': 'formação',
        'voltar_url': 'portfolio:lista_formacoes',
    })