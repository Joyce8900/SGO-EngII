from django.test import TestCase
from django.urls import reverse
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca

class CadastrarModeloViewTests(TestCase):
  def setUp(self):
    self.categoria = Categorias.objects.create(nome="Eletrônicos")
    self.marca = Marca.objects.create(nome="Samsung")
    self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)
  

  def test_cadastrar_modelo_view_post(self):
    print("test_cadastrar_modelo_view_post")
    ## Teste para o POST da view cadastrar_modelo
    data = {
        "nome": "Galaxy S23",
        "marca": self.marca.id,
    }
    
    response = self.client.post(reverse("cadastrar_modelo"), data)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Modelo.objects.count(), 2)
    self.assertTrue(Modelo.objects.filter(nome="Galaxy S23").exists())

  
  def test_cadastrar_modelo_view_get(self):
    print("test_cadastrar_modelo_view_get")
    ## Teste para o GET da view cadastrar_modelo
    response = self.client.get(reverse("cadastrar_modelo"))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "cadastrar_modelo.html")


  def test_cadastrar_modelo_view_post_invalido(self):
    print("test_cadastrar_modelo_view_post_invalido")
    ## Teste para o POST da view cadastrar_modelo com dados inválidos
    data = {
        "nome": "",
        "marca": self.marca.id,
    }
    response = self.client.post(reverse("cadastrar_modelo"), data)
    self.assertEqual(response.status_code, 200)
    form = response.context["form"]
    self.assertFalse(form.is_valid())
    self.assertIn("nome", form.errors)
    self.assertIn("Este campo é obrigatório.", form.errors["nome"])
    self.assertEqual(Modelo.objects.count(), 1)