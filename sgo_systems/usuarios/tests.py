from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class CadastroViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cadastro_url = reverse('cadastro')  
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'senha': 'testpassword123'
        }
        self.existing_user = User.objects.create_user(
            username='existinguser',
            email='existing@example.com',
            password='existingpass123'
        )

    def test_cadastro_get(self):
        response = self.client.get(self.cadastro_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_post_success(self):
        response = self.client.post(self.cadastro_url, self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_cadastro_post_existing_user(self):
        data = {'username': 'existinguser', 'email': 'test@example.com', 'senha': 'testpass'}
        response = self.client.post(self.cadastro_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Já existe um usuário com esse username')


class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')  # Substitua 'login' pelo nome da URL em urls.py
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_post_success(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'senha': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  


    def test_login_post_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'senha': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'usuario ou senha inválidos')


