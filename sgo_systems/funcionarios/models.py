from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255, verbose_name="Nome do Funcionário", help_text="Campo obrigatório", unique=True, blank=False, null=False)
    cargo = models.CharField(
        max_length=255, verbose_name="Cargo", help_text="Campo obrigatório")
    telefone = models.CharField(
        max_length=11,
        validators=[RegexValidator(
            r'^\d{11}$', 'O número de telefone deve ter 11 dígitos númericos')],
        verbose_name="Telefone",
        help_text="Campo obrigatório", unique=True, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ['nome']
