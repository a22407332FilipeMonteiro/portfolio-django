# portfolio/urls.py

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [

    # Home
    path('', views.home, name='home'),

    # Projetos
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:id>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:id>/apagar/', views.apagar_projeto, name='apagar_projeto'),

    # Tecnologias
    path('tecnologias/', views.lista_tecnologias, name='lista_tecnologias'),
    path('tecnologias/nova/', views.criar_tecnologia, name='criar_tecnologia'),
    path('tecnologias/<int:id>/editar/', views.editar_tecnologia, name='editar_tecnologia'),
    path('tecnologias/<int:id>/apagar/', views.apagar_tecnologia, name='apagar_tecnologia'),

    # Competências
    path('competencias/', views.lista_competencias, name='lista_competencias'),
    path('competencias/nova/', views.criar_competencia, name='criar_competencia'),
    path('competencias/<int:id>/editar/', views.editar_competencia, name='editar_competencia'),
    path('competencias/<int:id>/apagar/', views.apagar_competencia, name='apagar_competencia'),

    # Formações
    path('formacoes/', views.lista_formacoes, name='lista_formacoes'),
    path('formacoes/nova/', views.criar_formacao, name='criar_formacao'),
    path('formacoes/<int:id>/editar/', views.editar_formacao, name='editar_formacao'),
    path('formacoes/<int:id>/apagar/', views.apagar_formacao, name='apagar_formacao'),
    
    # Making-Of
    path('makingof/', views.lista_makingof, name='lista_makingof'),

    # Sobre
    path('sobre/', views.sobre, name='sobre'),
]