from django.db import models
from marca.models import Marca

class Modelo(models.Model):
  nome = models.CharField(max_length=100, default=1, unique=True, 
                          error_messages={ 'unique': "Já existe um modelo com este nome"})
  marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

  def __str__(self):
    return self.nome 