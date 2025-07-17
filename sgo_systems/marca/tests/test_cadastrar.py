from django.test import TestCase, Client # Garanta Client importado
from django.urls import reverse
from marca.models import Marca
from django.contrib.auth.models import User # Adicione esta importação

class CadastrarMarcaViewTests(TestCase):
    def setUp(self):
        self.client = Client() # Adicione esta linha
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword') # Adicione esta linha
        self.client.login(username='testuser', password='testpassword') # Adicione esta linha

        self.marca = Marca.objects.create(nome="Samsung")
    
    def test_cadastrar_marca_view_post(self):
        print("test_cadastrar_marca_view_post")
        ## Teste para o POST da view cadastrar_marca
        data = {
            "nome": "Asus", 
        }
        
        response = self.client.post(reverse("marca:cadastrar_marca"), data) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Marca.objects.count(), 2)
        self.assertTrue(Marca.objects.filter(nome="Asus").exists())

    def test_cadastrar_marca_view_get(self):
        print("test_cadastrar_marca_view_get")
        ## Teste para o GET da view cadastrar_marca
        response = self.client.get(reverse("marca:cadastrar_marca")) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "marca/cadastrar_marca.html") # Ajustado o nome do template, se necessário, para corresponder ao caminho real (marca/cadastrar_marca.html no seu sistema de arquivos)

    def test_cadastrar_marca_view_post_invalido(self):
        print("test_cadastrar_marca_view_post_invalido")
        ## Teste para o POST da view cadastrar_marca com dados inválidos
        data = {
            "nome": ""
        }
        response = self.client.post(reverse("marca:cadastrar_marca"), data) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)
        self.assertIn("Este campo é obrigatório.", form.errors["nome"])
        self.assertEqual(Marca.objects.count(), 1)