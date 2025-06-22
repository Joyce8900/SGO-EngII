from django.test import TestCase, Client
from django.urls import reverse
from .models import Funcao

class FuncaoViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.funcao = Funcao.objects.create(nome="Gerente", salario=2000)

    def test_listar_funcoes(self):
        response = self.client.get(reverse('listar_funcoes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gerente")

    def test_cadastrar_funcao(self):
        response = self.client.post(reverse('cadastrar_funcao'), {
            'nome': 'Analista',
            'salario': 3000
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Funcao.objects.filter(nome='Analista').exists())

    def test_editar_funcao(self):
        response = self.client.post(reverse('editar_funcao', kwargs={'pk': self.funcao.pk}), {
            'nome': 'Gerente Atualizado',
            'salario': 2500
        })
        self.assertEqual(response.status_code, 302)
        self.funcao.refresh_from_db()
        self.assertEqual(self.funcao.nome, 'Gerente Atualizado')

    def test_deletar_funcao(self):
        response = self.client.post(reverse('deletar_funcao', kwargs={'pk': self.funcao.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Funcao.objects.filter(pk=self.funcao.pk).exists())
