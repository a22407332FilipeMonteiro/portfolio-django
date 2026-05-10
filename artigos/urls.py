from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.lista_artigos, name='lista_artigos'),
    path('novo/', views.criar_artigo, name='criar_artigo'),
    path('<int:id>/', views.detalhe_artigo, name='detalhe_artigo'),
    path('<int:id>/editar/', views.editar_artigo, name='editar_artigo'),
    path('<int:id>/apagar/', views.apagar_artigo, name='apagar_artigo'),
    path('<int:id>/like/', views.toggle_like, name='toggle_like'),
    path('<int:id>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
]
