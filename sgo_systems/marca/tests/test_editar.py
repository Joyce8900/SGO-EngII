from django.test import TestCase, Client # Garanta Client importado
from django.urls import reverse
from marca.models import Marca # Categorias não é usado aqui, pode remover a importação se quiser
from django.contrib.auth.models import User # Adicione esta importação


class EditarCarcaViewTests(TestCase): # O nome da classe "EditarCarcaViewTests" parece um typo. Talvez devesse ser "EditarMarcaViewTests"?
    def setUp(self):
        self.client = Client() # Adicione esta linha
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword') # Adicione esta linha
        self.client.login(username='testuser', password='testpassword') # Adicione esta linha

        self.marca = Marca.objects.create(nome="Samsung")
    
    def test_editar_marca_view_post(self):
        print("test_editar_marca_view_post")
        # Teste para o POST da view editar_marca
        data = {
            "nome": "Asus"
        }
        response = self.client.post(reverse("marca:editar_marca", args=[self.marca.id]), data) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Marca.objects.count(), 1)
        self.assertTrue(Marca.objects.filter(nome="Asus").exists())

    def test_editar_marca_view_get(self):
        print("test_editar_marca_view_get")
        # Teste para o GET da view editar_marca
        response = self.client.get(reverse("marca:editar_marca", args=[self.marca.id])) # CORRIGIDO AQUI
        print(f"minha response: {response}") # Essa linha de print é para depuração, pode ser removida depois
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "marca/editar_marca.html") # Ajustado o nome do template, se necessário

    # OBS: Você tem dois métodos test_editar_marca_view_get. Recomenda-se ter apenas um para evitar duplicação.
    # Se ambos são intencionais (por algum motivo), o segundo também precisa da correção.
    # test_editar_marca_view_get foi duplicado no código original, mantive a correção no segundo, mas remova um deles.

    def test_editar_marca_view_post_invalido(self):
        print("test_editar_marca_view_post_invalido")
        # Teste para o POST da view editar_marca com dados inválidos
        data = {
            "nome": ""
        }
        response = self.client.post(reverse("marca:editar_marca", args=[self.marca.id]), data) # CORRIGIDO AQUI
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)
        self.assertIn("Este campo é obrigatório.", form.errors["nome"])
        self.assertEqual(Marca.objects.count(), 1)