from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'endereco', 'contato', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        contato = cleaned_data.get('contato')
        
        if not nome:
            self.add_error('nome', 'Este campo é obrigatório')
        if not contato:
            self.add_error('contato', 'Este campo é obrigatório')
        
        return cleaned_data

class FornecedorFilterForm(forms.Form):
    nome = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Filtrar por nome'})
    )
    contato = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Filtrar por contato'})
    )