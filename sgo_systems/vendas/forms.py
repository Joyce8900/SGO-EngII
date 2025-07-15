# vendas/forms.py
from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'funcionario', 'produto', 'valor_total']
        labels = {
            'cliente': 'Cliente',
            'funcionario': 'Funcionário',
            'produto': 'Produto',
            'valor_total': 'Valor Total',
        }
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'valor_total': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o valor total da venda',
                'step': '0.01' # Ensures two decimal places input for currency
            }),
        }

    # You can add custom __init__ method here if you need to filter querysets for ForeignKeys
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cliente'].queryset = Cliente.objects.filter(is_active=True)
    #     self.fields['funcionario'].queryset = Funcionario.objects.filter(is_active=True)
    #     self.fields['produto'].queryset = Produto.objects.filter(is_active=True)