from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Venda(models.Model):
  data = models.DateField(auto_now_add=True)
  funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.PROTECT)
  cliente = models.ForeignKey('cliente.Cliente', on_delete=models.PROTECT)
  entrada = models.ForeignKey('entrada.Entrada', on_delete=models.PROTECT)
  preco = models.FloatField(validators=[MinValueValidator(1.0)], null=False, blank=False)
