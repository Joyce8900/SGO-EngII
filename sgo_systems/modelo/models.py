from django.db import models

# Create your models here.

class Modelo(models.Model):
  nome = models.CharField(max_length=100)
  marca = models.CharField(max_length=100)

  def __str__(self):
    return f'{self.nome} , {self.marca}'