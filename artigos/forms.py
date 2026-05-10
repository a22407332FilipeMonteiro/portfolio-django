from django import forms
from .models import Artigo

_input_style = 'width:100%; padding:10px 12px; border:1px solid #d2d2d7; border-radius:8px; font-size:1em; font-family:inherit;'


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'texto', 'fotografia', 'link_externo']
        labels = {
            'titulo': 'Título',
            'texto': 'Texto (suporta Markdown)',
            'fotografia': 'Fotografia',
            'link_externo': 'Link externo (opcional)',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'style': _input_style}),
            'texto': forms.Textarea(attrs={'rows': 15, 'style': _input_style}),
            'link_externo': forms.URLInput(attrs={'style': _input_style, 'placeholder': 'https://'}),
        }
