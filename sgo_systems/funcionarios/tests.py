from django.test import TestCase, Client
from django.urls import reverse
from .models import Funcionario

class FuncionarioModelTest(TestCase):
    def test_criacao_funcionario(self):
        funcionario = Funcionario.objects.create(
            nome="João Silva",
            cargo="Gerente",
            telefone="83999998888"
        )
        self.assertEqual(funcionario.nome, "João Silva")
        self.assertEqual(funcionario.cargo, "Gerente")
        self.assertEqual(funcionario.telefone, "83999998888")

class FuncionarioViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.funcionario = Funcionario.objects.create(
            nome="Maria Souza",
            cargo="Vendedora",
            telefone="83999997777"
        )

    def test_listar_funcionario(self):
        response = self.client.get(reverse('listar_funcionario'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Maria Souza")

    def test_cadastrar_funcionario(self):
        response = self.client.post(reverse('cadastrar_funcionario'), {
            'nome': 'Carlos Lima',
            'cargo': 'Supervisor',
            'telefone': '83988886666'
        })
        self.assertEqual(response.status_code, 302)  # redireciona após cadastro
        self.assertTrue(Funcionario.objects.filter(nome="Carlos Lima").exists())

    def test_editar_funcionario(self):
        url = reverse('editar_funcionario', args=[self.funcionario.id])
        response = self.client.post(url, {
            'nome': 'Maria Silva',
            'cargo': 'Vendedora',
            'telefone': '83999997777'
        })
        self.assertEqual(response.status_code, 302)
        self.funcionario.refresh_from_db()
        self.assertEqual(self.funcionario.nome, 'Maria Silva')

    def test_excluir_funcionario(self):
        url = reverse('deletar_funcionario', args=[self.funcionario.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Funcionario.objects.filter(id=self.funcionario.id).exists())
