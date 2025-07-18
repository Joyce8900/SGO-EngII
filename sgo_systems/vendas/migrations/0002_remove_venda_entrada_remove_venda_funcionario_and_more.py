# Generated by Django 5.2 on 2025-07-15 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_options'),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='funcionario',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='preco',
        ),
        migrations.AddField(
            model_name='venda',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venda',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente'),
        ),
    ]
