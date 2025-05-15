### User Story US03 - Manter Fornecedor

|               |                                                                                                                              |
| ------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente adicionar, editar, visualizar e excluir informações sobre os fornecedores, como nome e contato. |

#### Testes de Aceitação (TA)

| Código     | Descrição |
| ---------- | --------- |
| **TA03.01** | **Cadastrar Fornecedor com sucesso:** O gerente acessa o sistema, seleciona "Cadastrar Fornecedor", preenche corretamente os dados e clica em "Salvar". O sistema exibe: "Fornecedor cadastrado com sucesso". |
| **TA03.02** | **Cadastrar Fornecedor com erro:** O gerente tenta cadastrar um fornecedor com dados obrigatórios ausentes ou inválidos (ex: CNPJ mal formatado). O sistema exibe: "Cadastro não realizado, o campo ‘CNPJ’ não foi informado corretamente". |
| **TA03.03** | **Editar Fornecedor com sucesso:** O gerente acessa a lista de fornecedores, edita os dados e salva. O sistema atualiza e exibe: "Alterações salvas com sucesso". |
| **TA03.04** | **Editar Fornecedor com erro:** O gerente tenta editar um fornecedor com dados inválidos. O sistema exibe: "Alterações não salvas, o campo ‘E-mail’ não foi informado corretamente". |
| **TA03.05** | **Excluir Fornecedor com sucesso:** O gerente confirma a exclusão de um fornecedor. O sistema exibe: "Fornecedor excluído com sucesso". |
| **TA03.06** | **Excluir Fornecedor com erro:** O gerente tenta excluir um fornecedor inexistente. O sistema exibe: "Fornecedor não encontrado. Tente novamente". |
| **TA03.07** | **Pesquisar Fornecedor com sucesso:** O gerente busca um fornecedor por nome ou CNPJ válido. O sistema exibe: "Fornecedor encontrado: Nome do Fornecedor, CNPJ: XX.XXX.XXX/0001-XX". |
| **TA03.08** | **Pesquisar Fornecedor sem resultados:** O gerente realiza uma busca por dados inexistentes. O sistema exibe: "Nenhum fornecedor encontrado com os dados informados". |
| **TA03.09** | **Pesquisar Fornecedor com múltiplos resultados:** O sistema deve exibir: "Foram encontrados X fornecedores com o nome ‘Fornecedor X’. Selecione o fornecedor correto". |
| **TA03.10** | **Cancelar Cadastro de Fornecedor:** O gerente inicia o cadastro e decide cancelar. O sistema retorna à tela anterior sem salvar dados e sem mensagens. |
| **TA03.11** | **Cancelar Edição de Fornecedor:** O gerente inicia a edição de um fornecedor e cancela. O sistema retorna à tela anterior sem aplicar alterações. |

# Relatório de Testes – US03: Manter Fornecedor

## Legenda

- **Teste**: Código ou identificação do Teste.  
- **Descrição**: Descrição dos passos e detalhes do teste a ser executado.  
- **Especificação**: Informações sobre a função testada e se ela está de acordo com a especificação do caso de uso.  
- **Resultado**: Resultado do teste, modificações sugeridas ou descrição do erro.

---

### Teste 01 – Cadastrar Fornecedor com sucesso

**Descrição:**  
O gerente acessa a tela de cadastro (`fornecedor_form.html`), preenche corretamente os dados e clica em “Salvar”.

**Especificação:**  
Conforme TA03.01, o sistema deve cadastrar o fornecedor e exibir: `"Fornecedor cadastrado com sucesso"`.

**Resultado:**  
Fornecedor é salvo no banco de dados.  
Nenhuma mensagem de sucesso é exibida ao usuário após o cadastro.

---

### Teste 02 – Cadastrar Fornecedor com erro

**Descrição:**  
O gerente tenta salvar o formulário com dados inválidos, como CNPJ incorreto.

**Especificação:**  
Conforme TA03.02, o sistema deve exibir: `"Cadastro não realizado, o campo ‘CNPJ’ não foi informado corretamente"`.

**Resultado:**  
Campos incorretos são destacados (`.invalid-feedback`), mas **nenhuma mensagem geral de erro** é apresentada.

---

### Teste 03 – Editar Fornecedor com sucesso

**Descrição:**  
O gerente acessa a lista de fornecedores, edita os dados e clica em "Salvar".

**Especificação:**  
Conforme TA03.03, o sistema deve atualizar os dados e exibir: `"Alterações salvas com sucesso"`.

**Resultado:**  
Alterações são salvas com sucesso.  
**Nenhuma mensagem de confirmação** é exibida.

---

### Teste 04 – Editar Fornecedor com erro

**Descrição:**  
O gerente tenta salvar alterações com dados inválidos (ex: e-mail mal formatado).

**Especificação:**  
Conforme TA03.04, o sistema deve exibir: `"Alterações não salvas, o campo ‘E-mail’ não foi informado corretamente"`.

**Resultado:**  
Campos inválidos são destacados.  
**Mensagem geral de erro está ausente.**

---

### Teste 05 – Excluir Fornecedor com sucesso

**Descrição:**  
O gerente confirma a exclusão de um fornecedor na tela `fornecedor_delete.html`.

**Especificação:**  
Conforme TA03.05, o sistema deve exibir: `"Fornecedor excluído com sucesso"`.

**Resultado:**  
Fornecedor excluído corretamente.  
**Mensagem de confirmação não exibida.**

---

### Teste 06 – Excluir Fornecedor com erro

**Descrição:**  
O gerente tenta excluir um fornecedor inexistente.

**Especificação:**  
Conforme TA03.06, o sistema deve exibir: `"Fornecedor não encontrado. Tente novamente"`.

**Resultado:**  
A exclusão falha conforme esperado, mas **nenhuma mensagem de erro** é exibida ao usuário.

---

### Teste 07 – Pesquisar Fornecedor com sucesso

**Descrição:**  
O gerente realiza uma busca com nome ou CNPJ válidos.

**Especificação:**  
Conforme TA03.07, o sistema deve exibir: `"Fornecedor encontrado: Nome do Fornecedor, CNPJ: XX.XXX.XXX/0001-XX"`.

**Resultado:**  
Fornecedor encontrado corretamente.  
**Mensagem de confirmação está ausente.**

---

### Teste 08 – Pesquisar Fornecedor sem resultados

**Descrição:**  
Busca realizada com dados inexistentes.

**Especificação:**  
Conforme TA03.08, o sistema deve exibir: `"Nenhum fornecedor encontrado com os dados informados"`.

**Resultado:**  
Nenhum fornecedor retornado, mas **mensagem esperada não exibida**.

---

### Teste 09 – Pesquisar Fornecedor com múltiplos resultados

**Descrição:**  
Busca retorna vários fornecedores.

**Especificação:**  
Conforme TA03.09, o sistema deve exibir: `"Foram encontrados X fornecedores com o nome ‘Fornecedor X’. Selecione o fornecedor correto"`.

**Resultado:**  
Lista de fornecedores exibida.  
**Mensagem explicativa está ausente.**

---

### Teste 10 – Cancelar Cadastro de Fornecedor

**Descrição:**  
O gerente cancela o cadastro antes de salvar.

**Especificação:**  
Conforme TA03.10, o sistema deve retornar à tela anterior sem salvar dados e sem exibir mensagens.

**Resultado:**  
Cadastro não salvo.  
**Comportamento conforme esperado.**

---

### Teste 11 – Cancelar Edição de Fornecedor

**Descrição:**  
O gerente cancela a edição antes de salvar.

**Especificação:**  
Conforme TA03.11, o sistema deve retornar à tela anterior sem salvar alterações.

**Resultado:**  
Edição não aplicada.  
**Comportamento conforme esperado.**

---

# Relatório de Bugs e Providências

| Teste                          | Providência                                                                 | Tarefas/Tipo                          |
|-------------------------------|------------------------------------------------------------------------------|---------------------------------------|
| Teste 01 – Cadastrar Fornecedor  | Exibir mensagem: “Fornecedor cadastrado com sucesso”.                       | Bug de Feedback ao Usuário            |
| Teste 02 – Cadastro com erro     | Incluir mensagem geral de erro além do destaque por campo.                  | Melhoria de UX                        |
| Teste 03 – Editar Fornecedor     | Exibir mensagem: “Alterações salvas com sucesso”.                           | Bug de Feedback ao Usuário            |
| Teste 04 – Editar com erro       | Incluir mensagem geral de erro, não apenas por campo.                       | Melhoria de UX                        |
| Teste 05 – Excluir Fornecedor    | Exibir mensagem: “Fornecedor excluído com sucesso”.                         | Bug de Feedback ao Usuário            |
| Teste 06 – Excluir com erro      | Implementar mensagem: “Fornecedor não encontrado. Tente novamente”.         | Bug de Validação de Erro              |
| Teste 07 – Pesquisa com sucesso  | Incluir mensagem de sucesso ao exibir resultados.                           | Melhoria de Feedback                  |
| Teste 08 – Pesquisa sem retorno  | Exibir mensagem: “Nenhum fornecedor encontrado com os dados informados”.    | Bug de Feedback ao Usuário            |
| Teste 09 – Múltiplos resultados  | Exibir mensagem: “Foram encontrados X fornecedores com o nome...”.          | Bug de Feedback ao Usuário            |
