from django.test import TestCase
from django.urls import reverse
from marca.models import Marca

class CadastrarMarcaViewTests(TestCase):
  def setUp(self):
    self.marca = Marca.objects.create(nome="Samsung")
    

  def test_cadastrar_marca_view_post(self):
    print("test_cadastrar_marca_view_post")
    ## Teste para o POST da view cadastrar_marca
    data = {
        "nome": "Asus", 
    }
    
    response = self.client.post(reverse("cadastrar_marca"), data)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Marca.objects.count(), 2)
    self.assertTrue(Marca.objects.filter(nome="Asus").exists())

  
  def test_cadastrar_marca_view_get(self):
    print("test_cadastrar_marca_view_get")
    ## Teste para o GET da view cadastrar_marca
    response = self.client.get(reverse("cadastrar_marca"))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "cadastrar_marca.html")


  def test_cadastrar_marca_view_post_invalido(self):
    print("test_cadastrar_marca_view_post_invalido")
    ## Teste para o POST da view cadastrar_marca com dados inválidos
    data = {
        "nome": ""
    }
    response = self.client.post(reverse("cadastrar_marca"), data)
    self.assertEqual(response.status_code, 200)
    form = response.context["form"]
    self.assertFalse(form.is_valid())
    self.assertIn("nome", form.errors)
    self.assertIn("Este campo é obrigatório.", form.errors["nome"])
    self.assertEqual(Marca.objects.count(), 1)