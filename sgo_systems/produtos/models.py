from django.db import models 
from django.core.validators import MinValueValidator
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
  
class Produtos(models.Model):
  categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
  nome = models.CharField(max_length=100, blank=False, null=False, help_text='Este campo é obrigatório')
  preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Valor padrão R$ 0.00
  quantidade = models.PositiveIntegerField(
    null=False,
    blank=False,
    default=1,  # Adicione esta linha
    help_text="Insira a quantidade.",
    validators=[MinValueValidator(1)]
)
  cor = models.CharField(max_length=30)
  tamanho = models.FloatField(null=False, validators=[MinValueValidator(0.01)])
  modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
  marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
  descricao = models.CharField(max_length=1000)
  def __str__(self):
    return f'{self.nome} , {self.categoria.nome}'
  
  class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'