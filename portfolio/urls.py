# portfolio/urls.py

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # Projetos
    path('', views.lista_projetos, name='lista_projetos'),
    path('projetos/', views.lista_projetos, name='projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:id>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:id>/apagar/', views.apagar_projeto, name='apagar_projeto'),

    # Tecnologias
    path('tecnologias/', views.lista_tecnologias, name='lista_tecnologias'),
    path('tecnologias/nova/', views.criar_tecnologia, name='criar_tecnologia'),
    path('tecnologias/<int:id>/editar/', views.editar_tecnologia, name='editar_tecnologia'),
    path('tecnologias/<int:id>/apagar/', views.apagar_tecnologia, name='apagar_tecnologia'),
]