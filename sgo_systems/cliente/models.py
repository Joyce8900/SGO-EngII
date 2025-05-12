from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    contato = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

# Create your models here.
