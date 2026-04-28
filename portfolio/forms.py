# portfolio/forms.py

from django import forms
from .models import Projeto


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'nome',
            'descricao',
            'data_inicio',
            'data_fim',
            'github',
            'demo',
            'imagem',
            'video',
            'destaque',
            'unidade_curricular',
            'tecnologias',
            'competencias',
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }