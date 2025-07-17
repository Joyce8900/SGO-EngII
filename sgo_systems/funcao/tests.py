from django.test import TestCase, Client
from django.urls import reverse
from .models import Funcao
from django.contrib.auth.models import User # Mantenha esta importação

class FuncaoViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Crie um usuário de teste e faça login com ele
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.funcao = Funcao.objects.create(nome="Gerente", salario=2000)

    def test_listar_funcoes(self):
        response = self.client.get(reverse('funcao:listar_funcoes')) # Corrigido aqui
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gerente")

    def test_cadastrar_funcao(self):
        response = self.client.post(reverse('funcao:cadastrar_funcao'), { # Corrigido aqui
            'nome': 'Analista',
            'salario': 3000
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Funcao.objects.filter(nome='Analista').exists())

    def test_editar_funcao(self):
        response = self.client.post(reverse('funcao:editar_funcao', kwargs={'pk': self.funcao.pk}), { # Corrigido aqui
            'nome': 'Gerente Atualizado',
            'salario': 2500
        })
        self.assertEqual(response.status_code, 302)
        self.funcao.refresh_from_db()
        self.assertEqual(self.funcao.nome, 'Gerente Atualizado')

    def test_deletar_funcao(self):
        response = self.client.post(reverse('funcao:deletar_funcao', kwargs={'pk': self.funcao.pk})) # Corrigido aqui
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Funcao.objects.filter(pk=self.funcao.pk).exists())