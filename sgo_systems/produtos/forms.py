from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'quantidade', 'cor', 'tamanho', 'marca', 'descricao']
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição'
        }