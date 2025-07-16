from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import DeleteView # Importar DeleteView
from django.urls import reverse_lazy # Importar reverse_lazy para redirecionamento após exclusão

from .models import Funcionario, Funcao

# Definir o URL de redirecionamento para a lista de funcionários
URL_FUNCIONARIOS = 'funcionarios:listar_funcionario'


class ListarFuncionarioView(View):
    """
    View para listar funcionários com funcionalidade de filtro por nome ou telefone.
    """
    template_name = 'funcionario/listar_funcionario.html'

    def get(self, request, *args, **kwargs):
        """
        Lida com requisições GET para exibir a lista de funcionários.
        Aplica filtro se um termo de busca for fornecido.
        """
        filtro = request.GET.get('filtro', '')
        if filtro:
            # Filtra funcionários cujo nome ou telefone contenha o termo de busca
            funcionarios = Funcionario.objects.filter(
                Q(nome__icontains=filtro) | Q(telefone__icontains=filtro)
            )
        else:
            # Se nenhum filtro for fornecido, lista todos os funcionários
            funcionarios = Funcionario.objects.all()
        return render(request, self.template_name, {'funcionarios': funcionarios})


class CadastrarFuncionarioView(View):
    """
    View para cadastrar novos funcionários.
    """
    template_name = 'funcionario/form_funcionario.html'

    def get(self, request, *args, **kwargs):
        """
        Lida com requisições GET para exibir o formulário de cadastro de funcionário.
        """
        funcoes = Funcao.objects.all() # Obtém todas as funções disponíveis
        return render(request, self.template_name, {'funcoes': funcoes, 'is_edit': False})

    def post(self, request, *args, **kwargs):
        """
        Lida com requisições POST para processar o envio do formulário de cadastro.
        Valida os dados e cria um novo funcionário.
        """
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        funcao_id = request.POST.get('funcao')

        # Valida se uma função foi selecionada
        if not funcao_id:
            messages.error(request, "Selecione uma função.")
            return render(request, self.template_name, {
                'funcionario': {'nome': nome, 'telefone': telefone},
                'funcoes': Funcao.objects.all(),
                'is_edit': False
            })

        # Valida se o telefone já está cadastrado
        if Funcionario.objects.filter(telefone=telefone).exists():
            messages.error(request, "Telefone já cadastrado.")
            return render(request, self.template_name, {
                'funcionario': {'nome': nome, 'telefone': telefone},
                'funcoes': Funcao.objects.all(),
                'is_edit': False
            })

        # Obtém o objeto Funcao com base no ID fornecido
        funcao = get_object_or_404(Funcao, id=funcao_id)
        # Cria um novo objeto Funcionario
        Funcionario.objects.create(nome=nome, telefone=telefone, funcao=funcao)
        messages.success(request, "Funcionário cadastrado com sucesso!")
        return redirect(URL_FUNCIONARIOS)


class EditarFuncionarioView(View):
    """
    View para editar informações de funcionários existentes.
    """
    template_name = 'funcionario/form_funcionario.html'

    def get(self, request, pk, *args, **kwargs):
        """
        Lida com requisições GET para exibir o formulário de edição de funcionário.
        Pré-preenche o formulário com os dados do funcionário existente.
        """
        funcionario = get_object_or_404(Funcionario, id=pk) # Obtém o funcionário a ser editado
        funcoes = Funcao.objects.all() # Obtém todas as funções disponíveis
        return render(request, self.template_name, {
            'funcionario': funcionario,
            'funcoes': funcoes,
            'is_edit': True
        })

    def post(self, request, pk, *args, **kwargs):
        """
        Lida com requisições POST para processar o envio do formulário de edição.
        Atualiza os dados do funcionário existente.
        """
        funcionario = get_object_or_404(Funcionario, id=pk)
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        funcao_id = request.POST.get('funcao')

        # Valida se uma função foi selecionada
        if not funcao_id:
            messages.error(request, "Selecione uma função.")
            return render(request, self.template_name, {
                'funcionario': {'id': funcionario.id, 'nome': nome, 'telefone': telefone},
                'funcoes': Funcao.objects.all(),
                'is_edit': True
            })

        # Valida se o telefone já está cadastrado por outro funcionário
        if Funcionario.objects.filter(telefone=telefone).exclude(id=funcionario.id).exists():
            messages.error(request, "Telefone já cadastrado.")
            return render(request, self.template_name, {
                'funcionario': {'id': funcionario.id, 'nome': nome, 'telefone': telefone},
                'funcoes': Funcao.objects.all(),
                'is_edit': True
            })

        # Obtém o objeto Funcao com base no ID fornecido
        funcao = get_object_or_404(Funcao, id=funcao_id)
        # Atualiza os campos do funcionário
        funcionario.nome = nome
        funcionario.telefone = telefone
        funcionario.funcao = funcao
        funcionario.save() # Salva as alterações no banco de dados
        messages.success(request, "Funcionário atualizado com sucesso!")
        return redirect(URL_FUNCIONARIOS)


class DeletarFuncionarioView(DeleteView):
    """
    View para deletar um funcionário diretamente via POST sem confirmação.
    """
    model = Funcionario
    # We will still set a template_name, but it won't be used for confirmation.
    # It will be rendered only if a GET request reaches here,
    # which we'll handle by redirecting.
    template_name = 'funcionario/listar_funcionario.html'
    success_url = reverse_lazy(URL_FUNCIONARIOS)

    def get(self, request, *args, **kwargs):
        """
        Redireciona para a lista de funcionários se for acessado via GET.
        A exclusão deve ser feita via POST.
        """
        # It's good practice to redirect if someone tries to access /delete/pk/ via GET
        # without a confirmation page. This prevents accidental deletion.
        messages.info(request, "Use o botão de exclusão na lista de funcionários para deletar.")
        return redirect(self.success_url)

    def delete(self, request, *args, **kwargs):
        """
        Sobrescreve o método delete para adicionar uma mensagem de sucesso.
        """
        messages.success(request, "Funcionário deletado com sucesso!")
        return super().delete(request, *args, **kwargs)
