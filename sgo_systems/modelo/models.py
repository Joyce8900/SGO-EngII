from django.db import models

class Modelo(models.Model):
  nome = models.CharField(max_length=100, default=1, unique=True, 
                          error_messages={ 'unique': "Já existe um modelo com este nome"})
  marca = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.nome} , {self.marca}'