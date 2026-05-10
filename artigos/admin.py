from django.contrib import admin
from .models import Artigo, Like, Comentario


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'data_criacao']
    list_filter = ['autor', 'data_criacao']
    search_fields = ['titulo', 'texto']
    readonly_fields = ['data_criacao']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['artigo', 'utilizador', 'session_key']
    list_filter = ['artigo']


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['artigo', 'autor', 'data_criacao']
    list_filter = ['artigo', 'autor']
    readonly_fields = ['data_criacao']
