from django.test import TestCase
from django.urls import reverse
from categorias.models import Categorias
from modelo.models import Modelo
from marca.models import Marca


class EditarModeloViewTests(TestCase):
  def setUp(self):
    self.categoria = Categorias.objects.create(nome="Eletrônicos")
    self.marca = Marca.objects.create(nome="Samsung")
    self.modelo = Modelo.objects.create(nome="Galaxy S22", marca=self.marca)
  

  def test_editar_modelo_view_post(self):
    print("test_editar_modelo_view_post")
    ## Teste para o POST da view editar_modelo
    data = {
        "nome": "Galaxy S23",
        "marca": self.marca.id,
    }
    response = self.client.post(reverse("editar_modelo", args=[self.modelo.id]), data)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Modelo.objects.count(), 1)
    self.assertTrue(Modelo.objects.filter(nome="Galaxy S23").exists())

  
  def test_editar_modelo_view_get(self):
        print("test_editar_p_view_get")
         ## Teste para o GET da view editar_modelo
        response = self.client.get(reverse("editar_modelo",args=[self.modelo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editar_modelo.html")

  # def test_editar_modelo_view_get(self):
  #    print("test_editar_modelo_view_get")
  #    ## Teste para o GET da view editar_modelo
  #    response = self.client.get(reverse("editar_modelo", args=[self.modelo.id]))
  #    print(f"minha response: {response}")
  #    self.assertEqual(response.status_code, 200)
  #    self.assertTemplateUsed(response, "editar_modelo.html")

  # def test_editar_modelo_view_post_invalido(self):
  #   print("test_editar_modelo_view_post_invalido")
  #   ## Teste para o POST da view editar_modelo com dados inválidos
  #   data = {
  #       "nome": "",
  #       "marca": self.marca.id,
  #   }
  #   response = self.client.post(reverse("editar_modelo", args=[self.modelo.id]), data)
  #   self.assertEqual(response.status_code, 200)
  #   form = response.context["form"]
  #   self.assertFalse(form.is_valid())
  #   self.assertIn("nome", form.errors)
  #   self.assertIn("Este campo é obrigatório.", form.errors["nome"])
  #   self.assertEqual(Modelo.objects.count(), 1)