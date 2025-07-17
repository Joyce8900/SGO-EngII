from django.test import TestCase, Client
from django.urls import reverse
from modelo.models import Modelo
from marca.models import Marca
from django.contrib.auth.models import User # Mantenha esta importação

class ListarModeloViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.marca = Marca.objects.create(nome='Marca Teste')
        
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
        response = self.client.get(reverse("modelo:listar_modelos"))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "listar_modelos.html") # Corrigido: sem 'modelo/' prefixo
        
        self.assertIn('modelos', response.context)
        
        modelos_na_view = list(response.context['modelos'])
        self.assertEqual(len(modelos_na_view), 2)
        self.assertIn(self.modelo1, modelos_na_view)
        self.assertIn(self.modelo2, modelos_na_view)
        
        self.assertEqual(modelos_na_view[0].nome, 'Modelo A')
        self.assertEqual(modelos_na_view[1].nome, 'Modelo B')
        
        content = response.content.decode('utf-8')
        self.assertIn('Modelo A', content)
        self.assertIn('Modelo B', content) 
        
    def test_listar_modelos_sem_modelos(self):
        print("test_listar_modelos_sem_modelos")
        Modelo.objects.all().delete()
        response = self.client.get(reverse('modelo:listar_modelos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhum modelo encontrado.") # Corrigido: mensagem de texto