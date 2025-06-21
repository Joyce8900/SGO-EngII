from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

# Constantes
TEXTO_CAMPO_OBRIGATORIO = "Campo obrigatório"


class Funcao(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name="Nome da Função",
        help_text=TEXTO_CAMPO_OBRIGATORIO,
        unique=True,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='O nome da função deve conter apenas letras e espaços.',
            )
        ]
    )
    salario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Salário",
        help_text=TEXTO_CAMPO_OBRIGATORIO,
        blank=False,
        null=False,
        validators=[MinValueValidator(0.01, message='O salário deve ser maior que zero.')]
    )

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"
        ordering = ['nome']