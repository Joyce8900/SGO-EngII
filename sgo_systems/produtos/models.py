from django.db import models 
from django.core.validators import MinValueValidator
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from fornecedores.models import Fornecedor
  
class Produtos(models.Model):
  categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
  nome = models.CharField(max_length=100, blank=False, null=False, help_text='Este campo é obrigatório')
  fornecedor = models.ForeignKey('fornecedores.Fornecedor', on_delete=models.PROTECT, blank=True, null=True)
  cor = models.CharField(max_length=30)
  tamanho = models.FloatField(null=False, validators=[MinValueValidator(0.01)])
  modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
  marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
  descricao = models.CharField(max_length=1000)
  def __str__(self):
    return f'{self.nome} , {self.categoria.nome}'
