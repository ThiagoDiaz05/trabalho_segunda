from django import forms
from .models import Grupo, Postagem

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'descricao', 'imagem']

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['texto', 'imagem']
