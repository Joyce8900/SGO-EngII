from django.db import migrations

def criar_categorias(apps, schema_editor):
    Categoria = apps.get_model('categorias', 'Categorias')
    categorias = [
        ('GRAU', 'Óculos de Grau'),
        ('SOL', 'Óculos de Sol'),
        ('LENTES', 'Lentes de Contato'),
        ('ACESSORIOS', 'Acessórios'),
        ('SAUDE', 'Saúde Ocular'),
        ('INFANTIL', 'Óculos Infantis'),
        ('ESPORTE', 'Óculos Esportivos'),
    ]
    
    for codigo, nome in categorias:
        Categoria.objects.get_or_create(nome=codigo)

class Migration(migrations.Migration):
    dependencies = [
    
        ('categorias', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(criar_categorias),
    ]