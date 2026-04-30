# portfolio/forms.py

from django import forms
from .models import Competencia, Formacao, Projeto, Tecnologia


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
            'unidade_curricular',
            'tecnologias',
            'competencias',
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows' : 4}),
            'tecnologias': forms.CheckboxSelectMultiple(),
            'competencias': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['video'].required = False
        self.fields['demo'].required = False
        self.fields['data_fim'].required = False
        self.fields['imagem'].required = False
        self.fields['descricao'].required = False
        self.fields['tecnologias'].required = False
        self.fields['competencias'].required = False


class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = [
            'nome',
            'tipo',
            'descricao',
            'logo',
            'website',
            'nivel_interesse',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].required = False
        self.fields['logo'].required = False


class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'nivel', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].required = False


class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = [
            'nome',
            'instituicao',
            'data_inicio',
            'data_fim',
            'descricao',
            'competencias',
            'tecnologias',
        ]
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'competencias': forms.CheckboxSelectMultiple(),
            'tecnologias': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].required = False
        self.fields['competencias'].required = False
        self.fields['tecnologias'].required = False