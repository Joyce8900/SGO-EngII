from django import forms
from .models import Produtos
from .models import Categorias

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ['nome', 'fornecedor',  'cor', 'tamanho', 'marca', 'descricao', 'categoria', 'modelo' ]
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
        }

class PesquisaProdutoForm(forms.Form):
    termo = forms.CharField(
        label="Buscar",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite nome, marca ou descrição...',
            'class': 'form-control'
        })
    )
    categoria = forms.ModelChoiceField(
        queryset=Categorias.objects.all(),
        required=False,
        label="Categoria",
        empty_label="Todas as categorias"
    )
