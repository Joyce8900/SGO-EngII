from django.test import TestCase
from django.urls import reverse
from categorias.models import Categorias
from marca.models import Marca


class EditarCarcaViewTests(TestCase):
   def setUp(self):
     self.marca = Marca.objects.create(nome="Samsung")
  

   def test_editar_marca_view_post(self):
     print("test_editar_marca_view_post")
      #Teste para o POST da view editar_marca
     data = {
         "nome": "Asus"
     }
     response = self.client.post(reverse("editar_marca", args=[self.marca.id]), data)
     self.assertEqual(response.status_code, 302)
     self.assertEqual(Marca.objects.count(), 1)
     self.assertTrue(Marca.objects.filter(nome="Asus").exists())

  
   def test_editar_marca_view_get(self):
         print("test_editar_p_view_get")
           #Teste para o GET da view editar_marca
         response = self.client.get(reverse("editar_marca",args=[self.marca.id]))
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, "editar_marca.html")

   def test_editar_marca_view_get(self):
       print("test_editar_marca_view_get")
        #Teste para o GET da view editar_marca
       response = self.client.get(reverse("editar_marca", args=[self.marca.id]))
       print(f"minha response: {response}")
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, "editar_marca.html")



   def test_editar_marca_view_post_invalido(self):
     print("test_editar_marca_view_post_invalido")
      #Teste para o POST da view editar_marca com dados inválidos
     data = {
         "nome": ""
     }
     response = self.client.post(reverse("editar_marca", args=[self.marca.id]), data)
     self.assertEqual(response.status_code, 200)
     form = response.context["form"]
     self.assertFalse(form.is_valid())
     self.assertIn("nome", form.errors)
     self.assertIn("Este campo é obrigatório.", form.errors["nome"])
     self.assertEqual(Marca.objects.count(), 1)