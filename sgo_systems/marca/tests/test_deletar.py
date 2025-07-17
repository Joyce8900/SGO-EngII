from django.test import TestCase, Client
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
from marca.models import Marca
from django.contrib.auth.models import User # Adicione esta importação


class MarcaDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword') # Adicione esta linha
        self.client.login(username='testuser', password='testpassword') # Adicione esta linha

        # Cria uma marca para teste
        self.marca = Marca.objects.create(nome='Marca Teste')
        self.delete_url = reverse('marca:deletar_marca', args=[self.marca.pk]) # CORRIGIDO AQUI
        self.list_url = reverse('marca:listar_marcas') # CORRIGIDO AQUI

    def test_delete_via_post_success(self):
        response = self.client.post(self.delete_url)
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Marca.objects.filter(pk=self.marca.pk).exists())
        storage = get_messages(response.wsgi_request)
        self.assertIn("Marca excluída com sucesso.", [str(m) for m in storage]) # Alterado para "excluída"

    def test_delete_via_get_success(self):
        response = self.client.get(self.delete_url)
        self.assertRedirects(response, self.list_url)
        self.assertFalse(Marca.objects.filter(pk=self.marca.pk).exists())

    def test_delete_non_existent_marca(self):
        invalid_url = reverse('marca:deletar_marca', args=[9999]) # CORRIGIDO AQUI
        response = self.client.post(invalid_url)
        self.assertEqual(response.status_code, 404)

    def test_message_not_present_on_get_request(self):
        response = self.client.get(self.delete_url, follow=True)
        storage = get_messages(response.wsgi_request)
        self.assertNotIn("Marca excluído com sucesso.", [str(m) for m in storage])