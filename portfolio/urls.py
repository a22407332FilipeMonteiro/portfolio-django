# portfolio/urls.py

from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('projetos/', views.lista_projetos, name='projetos'),
    path('projetos/novo/', views.criar_projeto, name='criar_projeto'),  # NOVO
]