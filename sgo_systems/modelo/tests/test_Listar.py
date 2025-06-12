from django.test import TestCase
from django.urls import reverse
from modelo.models import Modelo
from marca.models import Marca

class ListarModeloViewTests(TestCase):
    def setUp(self):
        # Cria uma marca primeiro (necessária para o modelo)
        self.marca = Marca.objects.create(nome='Marca Teste')
        
        # Cria alguns modelos para teste
        self.modelo1 = Modelo.objects.create(
            nome='Modelo A', 
            marca=self.marca,
            # outros campos obrigatórios do seu modelo
        )
        self.modelo2 = Modelo.objects.create(
            nome='Modelo B',
            marca=self.marca,
            # outros campos obrigatórios
        )
    
    def test_listar_modelos_view(self):
        """Testa se a view de listagem funciona corretamente"""
        # Chama a URL de listagem
        response = self.client.get(reverse("listar_modelos"))
        
        # Verificações básicas
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_modelos.html")
        
        # Verifica se os modelos estão no contexto
        self.assertIn('modelos', response.context)
        
        # Verifica se todos os modelos criados estão na listagem
        modelos_na_view = list(response.context['modelos'])
        self.assertEqual(len(modelos_na_view), 2)
        self.assertIn(self.modelo1, modelos_na_view)
        self.assertIn(self.modelo2, modelos_na_view)
        
        # Verifica se estão ordenados por nome
        self.assertEqual(modelos_na_view[0].nome, 'Modelo A')
        self.assertEqual(modelos_na_view[1].nome, 'Modelo B')
        
        # Verifica se o HTML contém os nomes dos modelos
        content = response.content.decode('utf-8')
        self.assertIn('Modelo A', content)
        self.assertIn('Modelo B', content)                       
    
    def test_listar_modelos_sem_modelos(self):
       print("test_listar_modelos_sem_modelos")
       ## Teste para o GET da view listar_modelos sem modelos
       Modelo.objects.all().delete()
       response = self.client.get(reverse('listar_modelos'))
       self.assertEqual(response.status_code, 200)
       self.assertContains(response, "Nenhum modelo cadastrado")  
  
