from django import forms
from .models import Produtos

class ProdutoForm(forms.ModelForm):
    def clean_preco(self):
        preco = self.cleaned_data['preco']
        if preco <= 0:
            raise forms.ValidationError("O preço deve ser maior que zero.")
        return round(preco, 2) 


    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser maior que zero.")
        return quantidade   
    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'quantidade', 'cor', 'tamanho', 'marca', 'descricao', 'categoria' ]
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'preco': 'Preço',
        }