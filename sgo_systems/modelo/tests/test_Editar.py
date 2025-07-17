from django.test import TestCase, Client
from django.urls import reverse
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca
from django.contrib.auth.models import User # Mantenha esta importação


class EditarModeloViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.categoria = Categorias.objects.create(nome="Eletrônicos")
        self.marca = Marca.objects.create(nome="Samsung")
        self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)
    
    def test_editar_modelo_view_post(self):
        print("test_editar_modelo_view_post")
        data = {
            "nome": "Galaxy S23",
            "marca": self.marca.id,
        }
        response = self.client.post(reverse("modelo:editar_modelo", args=[self.modelo.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Modelo.objects.count(), 1)
        self.modelo.refresh_from_db() 
        self.assertEqual(self.modelo.nome, "Galaxy S23")

    def test_editar_modelo_view_get(self):
        print("test_editar_modelo_view_get")
        response = self.client.get(reverse("modelo:editar_modelo", args=[self.modelo.id]))
        print(f"minha response: {response}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editar_modelo.html") # Corrigido: sem 'modelo/' prefixo

    def test_editar_modelo_view_post_invalido(self):
        print("test_editar_modelo_view_post_invalido")
        data = {
            "nome": "",
            "marca": self.marca.id,
        }
        response = self.client.post(reverse("modelo:editar_modelo", args=[self.modelo.id]), data)
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)
        self.assertIn("Este campo é obrigatório.", form.errors["nome"])
        self.assertEqual(Modelo.objects.count(), 1)