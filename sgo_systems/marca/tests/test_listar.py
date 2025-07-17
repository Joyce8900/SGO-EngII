from django.test import TestCase, Client # Garanta Client importado
from django.urls import reverse
from marca.models import Marca
from django.contrib.auth.models import User # Adicione esta importação

class ListarmarcaViewTests(TestCase): # O nome da classe "ListarmarcaViewTests" parece um typo. Talvez devesse ser "ListarMarcaViewTests"?
    def setUp(self):
        self.client = Client() # Adicione esta linha
        self.user = User.objects.create_user(username='testuser', password='testpassword') # Adicione esta linha
        self.client.login(username='testuser', password='testpassword') # Adicione esta linha

        self.marca = Marca.objects.create(nome='Marca Teste')
        
        self.marca1 = Marca.objects.create(
            nome='Marca A', # Mudado para 'Marca A' para evitar conflito com 'Marca Teste'
        )
        self.marca2 = Marca.objects.create(
            nome='Marca B',
        )
    
    def test_listar_marcas_view(self):
        """Testa se a view de listagem funciona corretamente"""
        response = self.client.get(reverse("marca:listar_marcas")) # CORRIGIDO AQUI
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "marca/listar_marcas.html") # Ajustado o nome do template, se necessário
        
        self.assertIn('marcas', response.context) # Verifique se o nome do contexto é 'marcas' ou 'funcoes' (como em funcao)
        
        content = response.content.decode('utf-8')
        self.assertIn('Marca A', content)
        self.assertIn('Marca B', content)
            
    def test_listar_marcas_sem_marcas(self):
        print("test_listar_marca_sem_marcas")
        Marca.objects.all().delete()
        response = self.client.get(reverse('marca:listar_marcas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhuma marca encontrada.") # Alterado para "encontrada."