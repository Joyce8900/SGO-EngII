### User Story US02 - Manter Cliente

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente e aos funcionários cadastrar, editar, visualizar e excluir informações sobre os clientes. Isso inclui dados como nome, CPF, telefone de contato e endereço. |

#### Testes de Aceitação (TA)

| Código     | Descrição |
| ---------- | --------- |
| **TA02.01** | **Cadastrar Cliente com sucesso:** O gerente ou funcionário acessa o sistema, seleciona "Cadastrar Cliente", preenche corretamente todos os campos obrigatórios (nome, CPF, telefone, endereço) e clica em "Salvar". O sistema exibe: "Cliente cadastrado com sucesso". |
| **TA02.02** | **Cadastrar Cliente com erro:** O gerente ou funcionário tenta cadastrar um cliente, mas deixa campos obrigatórios em branco ou insere dados inválidos (ex: CPF mal formatado). O sistema exibe: "Erro: Verifique os campos obrigatórios e tente novamente". |
| **TA02.03** | **Editar Cliente com sucesso:** O gerente ou funcionário acessa a lista de clientes, edita as informações de um cliente e clica em "Salvar". O sistema atualiza os dados e exibe: "Alterações salvas com sucesso". |
| **TA02.04** | **Editar Cliente com erro:** O gerente ou funcionário tenta editar um cliente com dados inválidos (ex: número de telefone incorreto). O sistema exibe: "Erro: Dados inválidos. Verifique as informações e tente novamente". |
| **TA02.05** | **Excluir Cliente com sucesso:** O gerente ou funcionário seleciona um cliente da lista e confirma a exclusão. O sistema remove o cliente e exibe: "Cliente excluído com sucesso". |
| **TA02.06** | **Excluir Cliente com erro:** O gerente ou funcionário tenta excluir um cliente que está vinculado a outros registros (ex: vendas). O sistema exibe: "Erro: Não foi possível excluir o cliente. Verifique as dependências". |
| **TA02.07** | **Pesquisar Cliente com sucesso:** O gerente ou funcionário utiliza o campo de busca para localizar um cliente pelo nome ou CPF. O sistema exibe os resultados com a mensagem: "Cliente(s) encontrado(s): {lista de clientes}". |
| **TA02.08** | **Pesquisar Cliente sem resultados:** O gerente ou funcionário realiza uma busca por um cliente que não está cadastrado. O sistema exibe: "Nenhum cliente encontrado". |
| **TA02.09** | **Cancelar Cadastro de Cliente:** O gerente ou funcionário inicia o cadastro, mas decide cancelar antes de salvar. O sistema retorna à tela anterior sem salvar dados e sem mensagens de erro. |
| **TA02.10** | **Cancelar Edição de Cliente:** O gerente ou funcionário edita um cliente, mas decide cancelar antes de salvar. O sistema retorna à tela anterior sem aplicar as alterações e sem mensagens de erro. |


# Relatório de Testes – US02: Manter Cliente

## Legenda

- **Teste**: Código ou identificação do Teste.  
- **Descrição**: Descrição dos passos e detalhes do teste a ser executado.  
- **Especificação**: Informações sobre a função testada e se ela está de acordo com a especificação do caso de uso.  
- **Resultado**: Resultado do teste, modificações sugeridas ou descrição do erro.

---

### Teste 01 – Cadastrar Cliente com sucesso

**Descrição:**  
O ator acessa a tela de cadastro (`cliente_form.html`), preenche todos os campos corretamente e clica em “Salvar”.

**Especificação:**  
Conforme o TA02.01, o sistema deve cadastrar o cliente e exibir a mensagem: `"Cliente cadastrado com sucesso"`.

**Resultado:**  
Cliente é salvo no banco de dados.  
Nenhuma mensagem de sucesso é exibida após o cadastro. O sistema redireciona para a lista sem feedback ao usuário.

---

### Teste 02 – Cadastrar Cliente com erro

**Descrição:**  
O ator acessa a tela de cadastro e tenta salvar o formulário com campos obrigatórios vazios (ex: CPF e endereço).

**Especificação:**  
O sistema deve impedir o cadastro e exibir a mensagem: `"Erro: Verifique os campos obrigatórios e tente novamente"`.

**Resultado:**  
O formulário não é enviado e os campos com erro são destacados com a `div.text-danger`.  
A mensagem genérica esperada não aparece. Apenas erros nos campos individuais.

---

### Teste 03 – Editar Cliente com sucesso

**Descrição:**  
O ator acessa a lista (`cliente_list.html`), clica em “Editar” e altera os dados de um cliente, depois clica em “Salvar”.

**Especificação:**  
Conforme TA02.03, o sistema deve atualizar os dados e exibir: `"Alterações salvas com sucesso"`.

**Resultado:**  
Alteração é salva corretamente.  
Nenhuma mensagem de sucesso é exibida.

---

### Teste 04 – Excluir Cliente com sucesso

**Descrição:**  
O ator acessa a lista de clientes, clica em “Excluir”, é redirecionado para `cliente_delete.html`, confirma a exclusão.

**Especificação:**  
Conforme TA02.05, o sistema deve excluir o cliente e exibir: `"Cliente excluído com sucesso"`.

**Resultado:**  
Cliente excluído com sucesso.  
Nenhuma mensagem de confirmação é exibida ao usuário.

---

### Teste 05 – Excluir Cliente sem verificação de dependência

**Descrição:**  
O ator acessa a lista de clientes, clica em “Excluir”, é redirecionado para `cliente_delete.html`, confirma a exclusão e o cliente é removido do sistema.

**Especificação:**  
Embora o TA02.06 preveja a exibição de uma mensagem de erro ao tentar excluir um cliente vinculado a outros registros (ex: vendas), essa funcionalidade ainda **não foi implementada**.

**Resultado:**  
O cliente é excluído com sucesso.  
A exclusão é feita **sem qualquer verificação de dependência**, o que pode causar inconsistências futuras quando relacionamentos (como vendas ou ordens de serviço) forem implementados.  
**Observação:** Nenhuma restrição ou mensagem é exibida, mesmo que no futuro esse cliente possa estar vinculado a registros importantes.

---

# Relatório de Bugs e Providências

| Teste                          | Providência                                                                 | Tarefas/Tipo                         |
|-------------------------------|------------------------------------------------------------------------------|--------------------------------------|
| Teste 01 – Cadastrar Cliente  | Adicionar mensagem de sucesso após redirecionamento.                        | Bug de Feedback ao Usuário           |
| Teste 02 – Cadastro com erro  | Exibir mensagem geral de erro além da validação por campo.                  | Melhoria de UX                       |
| Teste 03 – Editar Cliente     | Exibir mensagem “Alterações salvas com sucesso”.                            | Bug de Feedback ao Usuário           |
| Teste 04 – Excluir Cliente    | Exibir mensagem “Cliente excluído com sucesso”.                             | Bug de Feedback ao Usuário           |
| Teste 05 – Exclusão sem verificação | Implementar verificação de vínculos futuros (ex: vendas) antes da exclusão de clientes. | Melhoria preventiva / Planejamento futuro |
