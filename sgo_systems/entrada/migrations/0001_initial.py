# Generated by Django 5.2 on 2025-05-17 23:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('funcionarios', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField()),
                ('quantidade', models.PositiveIntegerField()),
                ('valor', models.FloatField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedores.fornecedor')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.funcionario')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produtos')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['data_entrada'],
            },
        ),
    ]
