from django.db import models
from django.core.validators import RegexValidator

# Constantes
TEXTO_CAMPO_OBRIGATORIO = "Campo obrigatório"
MSG_ERRO_TELEFONE = "O número de telefone deve ter 11 dígitos numéricos"

class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255, 
        verbose_name="Nome do Funcionário", 
        help_text=TEXTO_CAMPO_OBRIGATORIO, 
        unique=False,
        blank=False, 
        null=False
    )
    cargo = models.CharField(
        max_length=255, 
        verbose_name="Cargo", 
        help_text=TEXTO_CAMPO_OBRIGATORIO
    )
    telefone = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^\d{11}$', MSG_ERRO_TELEFONE)],
        verbose_name="Telefone",
        help_text=TEXTO_CAMPO_OBRIGATORIO,
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"
        ordering = ['nome']