from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'contato', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'contato': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        cpf = cleaned_data.get('cpf')

        if not nome:
            self.add_error('nome', 'O nome é obrigatório.')
        if not cpf:
            self.add_error('cpf', 'O CPF é obrigatório.')

        return cleaned_data

class ClienteFilterForm(forms.Form):
    termo = forms.CharField(
        label="Buscar",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite nome, cpf, contato ou endereço...',
            'class': 'form-control'
        })
    )