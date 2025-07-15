from django import forms
from .models import Marca

class MarcaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona 'form-control' a todos os campos do formulário
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Marca
        fields = ['nome']
        labels = {
            'nome': 'Nome da Marca'   
        }
