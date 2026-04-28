from django.shortcuts import render
from .models import Projeto


def lista_projetos(request):
    projetos = (Projeto.objects
                .select_related('unidade_curricular')
                .prefetch_related('tecnologias', 'competencias')
                .all())
    return render(request, 'portfolio/lista_projetos.html', {'projetos': projetos})
