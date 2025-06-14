from django.test import TestCase
from django.urls import reverse
from marca.models import Marca

class ListarmarcaViewTests(TestCase):
    def setUp(self):
        # Cria uma marca primeiro (necessária para o marca)
        self.marca = Marca.objects.create(nome='Marca Teste')
        
        # Cria alguns marcas para teste
        self.marca1 = Marca.objects.create(
            nome='marca A', 

            # outros campos obrigatórios do seu marca
        )
        self.marca2 = Marca.objects.create(
            nome='marca B',
            
            # outros campos obrigatórios
        )
    
    def test_listar_marcas_view(self):
        """Testa se a view de listagem funciona corretamente"""
        # Chama a URL de listagem
        response = self.client.get(reverse("listar_marcas"))
        
        # Verificações básicas
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_marcas.html")
        
        # Verifica se os marcas estão no contexto
        self.assertIn('marcas', response.context)
        
        
        

        
        # Verifica se o HTML contém os nomes dos marcas
        content = response.content.decode('utf-8')
        self.assertIn('marca A', content)
        self.assertIn('marca B', content)                       
    
    def test_listar_marcas_sem_marcas(self):
       print("test_listar_marca_sem_marcas")
       ## Teste para o GET da view listar_marcas sem marcas
       Marca.objects.all().delete()
       response = self.client.get(reverse('listar_marcas'))
       self.assertEqual(response.status_code, 200)
       self.assertContains(response, "Nenhuma marca cadastrada.")  
  
