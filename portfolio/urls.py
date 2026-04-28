from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('projetos/', views.lista_projetos, name='projetos'),
]