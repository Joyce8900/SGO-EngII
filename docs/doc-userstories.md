# Documento Lista de User Stories

## DESCRIÇÃO

Este documento de User Stories descreve os requisitos e funcionalidades essenciais para o desenvolvimento de um sistema de gerenciamento de estoque para uma ótica. O objetivo é atender às necessidades dos usuários (gerente e equipe da ótica), garantindo um controle eficiente e organizado dos produtos em estoque, bem como processos de vendas e geração de relatórios.


## HISTÓRICO DE REVISÕES

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 03/04/2025 | 0.0.1   | Template e descrição do documento  | Gustavo |
| 04/04/2025 | 0.0.2   | Adicionando US.01 US.02 US.03 US.04 US.05 US.06 US.07 US.08                 | Gabriel |
| 05/04/2025 | 0.0.3   | Correções de inconsistências nas descrições, requisitos envolvidos e testes de aceitação | Gabriel |
| 11/06/2025 | 0.0.4   | Adição da US06 - Manter Quantidade em Estoque e reordenação | Cayo |


### User Story US01 - Manter Funcionário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permetir ao gerente cadastrar, editar, visualizar, e excluir informações sobre os funcionários. Isso inclui detalhes como nome, cargo e contato |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01.01          | Inserir Funcionário |
| RF01.02          | Listar Funcionários |
| RF01.03          | Atualizar Funcionário |
| RF01.04          | Deletar Funcionário |


|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 5 h                                 | 
| **Tempo Gasto (real):**   | -                                   | 
| **Tamanho Funcional**     | 8 PF                                | 
| **Analista**              | Pessoa 1                            | 
| **Desenvolvedor**         | Pessoa 2                            | 
| **Revisor**               | Pessoa 3                            | 
| **Testador**              | Pessoa 4                            | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | **Cadastrar Funcionário com sucesso:** O gerente acessa o sistema, seleciona a opção "Cadastrar Funcionário", preenche corretamente todos os campos obrigatórios (nome, cargo, contato, etc.) e clica em "Salvar". O sistema exibe: "Funcionário cadastrado com sucesso |
| **TA01.02** | **Cadastrar Funcionário com erro:** O gerente tenta cadastrar um funcionário, mas deixa campos obrigatórios em branco ou preenche com dados inválidos. O sistema exibe: "Erro: Verifique os campos obrigatórios e tente novamente". |
| **TA01.03** | **Editar Funcionário com sucesso:** O gerente acessa o sistema, seleciona um funcionário existente na lista, altera informações (como cargo ou telefone) e clica em "Salvar". O sistema atualiza os dados e exibe: "Alterações salvas com sucesso". |
| **TA01.04** | **Editar Funcionário com erro:** O gerente tenta editar um funcionário, mas insere valores inválidos (como e-mail incorreto). O sistema exibe: "Erro: Dados inválidos. Verifique as informações e tente novamente". |
| **TA01.05** | **Excluir Funcionário com sucesso:** O gerente acessa o sistema, seleciona um funcionário da lista e confirma a exclusão. O sistema remove o funcionário e exibe: "Funcionário excluído com sucesso". |
| **TA01.06** | **Excluir Funcionário com erro:** O gerente tenta excluir um funcionário que não existe ou que está associado a outros registros no sistema. O sistema exibe: "Erro: Não foi possível excluir o funcionário. Verifique as dependências". |
| **TA01.07** | **Pesquisar Funcionário com sucesso:** O gerente utiliza o campo de busca para localizar um funcionário pelo nome ou cargo. O sistema exibe os resultados correspondentes com a mensagem: "Funcionário(s) encontrado(s): {lista de funcionários}". |
| **TA01.08** | **Pesquisar Funcionário sem resultados:** O gerente realiza uma busca por um funcionário que não está cadastrado no sistema. O sistema exibe: "Nenhum funcionário encontrado". |
| **TA01.09** | **Cancelar Cadastro de Funcionário:** O gerente inicia o processo de cadastro, mas decide cancelar antes de salvar. O sistema retorna à tela anterior sem salvar os dados e sem exibir mensagens de erro. |
| **TA01.10** | **Cancelar Edição de Funcionário:** O gerente edita informações de um funcionário, mas decide cancelar antes de salvar. O sistema retorna à tela anterior sem aplicar as alterações e sem exibir mensagens de erro. |


### User Story US02 - Manter Cliente

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente e aos funcionários cadastrar, editar, visualizar e excluir informações sobre os clientes. Isso inclui dados como nome, CPF, telefone de contato e endereço. |

#### Requisitos envolvidos

| Código        | Descrição              |
| ------------- | ---------------------- |
| RF02.01       | Inserir Cliente        |
| RF02.02       | Listar Clientes        |
| RF02.03       | Atualizar Cliente      |
| RF02.04       | Deletar Cliente        |

#### Detalhes

| Campo                     | Valor                               |
| ------------------------ | ----------------------------------- |
| **Prioridade**           | Essencial                           |
| **Estimativa**           | 5 h                                 |
| **Tempo Gasto (real)**   | -                                   |
| **Tamanho Funcional**    | 8 PF                                |
| **Analista**             | Pessoa 1                            |
| **Desenvolvedor**        | Pessoa 2                            |
| **Revisor**              | Pessoa 3                            |
| **Testador**             | Pessoa 4                            |

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



### User Story US03 - Manter Fornecedor

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente adicionar, editar, visualizar e excluir informações sobre os fornecedores. Isso inclui detalhes como nome e contato |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF02.01          | Inserir Fornecedor |
| RF02.02          | Listar Fornecedores |
| RF02.03          | Atualizar Fornecedor |
| RF02.04          | Deletar Fornecedor |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 5 h                                 | 
| **Tempo Gasto (real):**   | -                                   | 
| **Tamanho Funcional**     | 8 PF                                | 
| **Analista**              | Pessoa 1                            | 
| **Desenvolvedor**         | Pessoa 2                            | 
| **Revisor**               | Pessoa 3                            | 
| **Testador**              | Pessoa 4                            | 

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA02.01** | **Cadastrar Fornecedor com sucesso:** O gerente acessa o sistema com suas credenciais, preenche corretamente todos os dados obrigatórios do fornecedor e clica em "Salvar". O sistema valida as informações, armazena os dados e exibe a mensagem: "Fornecedor cadastrado com sucesso". |
| **TA02.02** | **Cadastrar Fornecedor com erro:** O gerente acessa o sistema e preenche dados incorretos (por exemplo, um CNPJ inválido ou um campo obrigatório não preenchido) e clica em "Salvar". O sistema valida os dados, exibe uma mensagem de erro: "Cadastro não realizado, o campo ‘CNPJ’ não foi informado corretamente". |
| **TA02.03** | **Editar Fornecedor com sucesso:** O gerente acessa o sistema com suas credenciais, seleciona um fornecedor da lista, edita as informações (por exemplo, telefone ou endereço), e confirma as alterações. O sistema atualiza as informações do fornecedor e exibe a mensagem: "Alterações salvas com sucesso". |
| **TA02.04** | **Editar Fornecedor com erro:** O gerente tenta editar o fornecedor, mas insere um valor inválido (por exemplo, um e-mail com formato incorreto) e tenta salvar. O sistema exibe a mensagem: "Alterações não salvas, o campo ‘E-mail’ não foi informado corretamente". |
| **TA02.05** | **Excluir Fornecedor com sucesso:** O gerente acessa o sistema, pesquisa e seleciona o fornecedor para excluir, confirma a ação e o sistema exclui o fornecedor. Exibição da mensagem: "Fornecedor excluído com sucesso". |
| **TA02.06** | **Excluir Fornecedor com erro:** O gerente tenta excluir um fornecedor que não existe ou que possui dados incorretos. O sistema exibe a mensagem: "Fornecedor não encontrado. Tente novamente". |
| **TA02.07** | **Pesquisar Fornecedor com sucesso:** O gerente pesquisa por um fornecedor fornecendo o nome ou CNPJ correto. O sistema retorna os dados do fornecedor, exibindo a mensagem: "Fornecedor encontrado: Nome do Fornecedor, CNPJ: 12.345.678/0001-99". |
| **TA02.08** | **Pesquisar Fornecedor - Nenhum resultado encontrado:** O gerente pesquisa por um fornecedor, mas o sistema não encontra nenhum resultado. O sistema exibe a mensagem: "Nenhum fornecedor encontrado com os dados informados". |
| **TA02.09** | **Pesquisar Fornecedor - Múltiplos resultados encontrados:** O gerente pesquisa um nome que corresponde a mais de um fornecedor. O sistema exibe uma lista de resultados e o gerente seleciona o fornecedor correto. A mensagem exibida será: "Foram encontrados 3 fornecedores com o nome ‘Fornecedor X’. Selecione o fornecedor correto". |
| **TA02.10** | **Cancelar Cadastro de Fornecedor:** O gerente acessa a tela de cadastro de fornecedor, preenche alguns dados e decide cancelar o cadastro antes de salvar. O sistema retorna à tela anterior sem salvar os dados e sem apresentar mensagens de erro. |
| **TA02.11** | **Cancelar Edição de Fornecedor:** O gerente acessa a tela de edição de fornecedor, faz alterações e decide cancelar antes de salvar. O sistema retorna à tela anterior sem salvar as alterações e sem apresentar mensagens de erro. |



### User Story US04 - Manter Produto

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente adicionar, editar, visualizar e excluir informações sobre os produtos. Isso inclui detalhes como nome e preço |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF03.01          | Inserir Produto |
| RF03.02          | Listar Produtos |
| RF03.03          | Atualizar Produto |
| RF03.04          | Deletar Produto |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 5 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 8 PF                                | 
| **Analista**              | Pessoa 1                            | 
| **Desenvolvedor**         | Pessoa 2                            | 
| **Revisor**               | Pessoa 1                            | 
| **Testador**              | Pessoa 3                            | 

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA03.01** | **Cadastrar Produto com sucesso:** O gerente acessa o sistema, preenche corretamente todos os dados obrigatórios do produto (como nome, categoria, preço e quantidade) e clica em "Salvar". O sistema exibe: "Produto cadastrado com sucesso". |
| **TA03.02** | **Cadastrar Produto com erro:** O gerente tenta cadastrar um produto com dados inválidos ou campos obrigatórios não preenchidos (por exemplo, preço negativo). O sistema exibe a mensagem: "Erro no cadastro. Verifique os campos obrigatórios". |
| **TA03.03** | **Editar Produto com sucesso:** O gerente acessa o sistema, seleciona um produto existente, altera informações (como preço ou descrição) e confirma as alterações. O sistema exibe: "Produto alterado com sucesso". |
| **TA03.04** | **Editar Produto com erro:** O gerente tenta editar um produto, mas insere um valor inválido (por exemplo, texto em um campo numérico). O sistema exibe a mensagem: "Alterações não salvas. Verifique os dados informados". |
| **TA03.05** | **Excluir Produto com sucesso:** O gerente acessa o sistema, seleciona um produto existente e confirma a exclusão. O sistema remove o produto e exibe: "Produto excluído com sucesso". |
| **TA03.06** | **Excluir Produto com erro:** O gerente tenta excluir um produto que não existe. O sistema exibe a mensagem: "Erro ao excluir. Produto não encontrado". |
| **TA03.07** | **Pesquisar Produto com sucesso:** O gerente realiza uma busca por nome, categoria ou código do produto e o sistema exibe os resultados correspondentes. Mensagem: "Produto(s) encontrado(s): {lista de produtos}". |
| **TA03.08** | **Pesquisar Produto sem resultados:** O gerente realiza uma busca que não retorna produtos. O sistema exibe: "Nenhum produto encontrado". |
| **TA03.09** | **Cancelar Cadastro de Produto:** O gerente acessa a tela de cadastro, preenche alguns dados e decide cancelar antes de salvar. O sistema retorna à tela anterior sem salvar os dados e sem exibir mensagens de erro. |
| **TA03.10** | **Cancelar Edição de Produto:** O gerente acessa a tela de edição, faz alterações, mas decide cancelar antes de salvar. O sistema retorna à tela anterior sem aplicar alterações e sem exibir mensagens de erro. |



### User Story US05 - Entrar Produto

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente registrar a entrada de novos produtos no estoque do sistema, incluindo a data da entrada, a quantidade do produto e os detalhes do fornecedor. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| Não especificado no doc de visão                   | ?                       |


|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 5 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 8 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 1                            |
| **Testador**              | Pessoa 3                            |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA04.01** | **Registrar Entrada de Produto com sucesso:** O gerente acessa o sistema, seleciona um produto existente, insere a quantidade a ser adicionada ao estoque e confirma. O sistema exibe: "Entrada registrada com sucesso". |
| **TA04.02** | **Registrar Entrada de Produto com erro:** O gerente tenta registrar a entrada de um produto inexistente ou insere uma quantidade inválida (por exemplo, valor negativo). O sistema exibe: "Erro ao registrar entrada". |
| **TA04.03** | **Visualizar Histórico de Entradas:** O gerente acessa o histórico de entradas e o sistema exibe uma lista com detalhes como data, quantidade e produto correspondente. |
| **TA04.04** | **Cancelar Registro de Entrada:** O gerente inicia o processo de entrada de produto, mas decide cancelar antes de confirmar. O sistema retorna à tela anterior sem salvar as alterações. |
| **TA04.05** | **Filtrar Histórico de Entradas:** O gerente utiliza um filtro para buscar entradas de um produto específico ou por um intervalo de datas. O sistema exibe os resultados filtrados corretamente. |
| **TA04.06** | **Nenhum Resultado no Histórico:** O gerente realiza uma busca no histórico que não retorna resultados. O sistema exibe: "Nenhuma entrada encontrada para os critérios especificados". |

### User Story US06 - Manter Quantidade em Estoque

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve atualizar automaticamente a quantidade em estoque quando ocorrerem: entradas de produtos, vendas realizadas, cancelamentos de venda/entrada e correções manuais pelo gerente. Deve garantir a integridade e consistência dos dados do estoque. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| RF09.01                   | Atualizar estoque na entrada de produtos          |
| RF09.02                   | Atualizar estoque na venda                        |
| RF09.03                   | Atualizar estoque no cancelamento                 |
| RF09.04                   | Ajuste manual de estoque                          |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 10 PF                               |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 3                            |
| **Testador**              | Pessoa 4                            |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **TA09.01** | **Atualização automática na entrada:** Ao registrar uma entrada de produto, o sistema incrementa automaticamente a quantidade em estoque e exibe "Estoque atualizado com sucesso". |
| **TA09.02** | **Atualização automática na venda:** Ao confirmar uma venda, o sistema decrementa automaticamente a quantidade vendida de cada produto e exibe "Estoque atualizado com sucesso". |
| **TA09.03** | **Cancelamento de venda:** Ao cancelar uma venda, o sistema restaura automaticamente as quantidades dos produtos ao estoque e exibe "Estoque reestabelecido". |
| **TA09.04** | **Ajuste manual pelo gerente:** O gerente pode fazer ajustes manuais no estoque (incluindo zerar) e o sistema registra a alteração com log de quem fez a modificação. |
| **TA09.05** | **Tentativa de venda sem estoque:** Ao tentar vender produto com estoque insuficiente, o sistema impede a venda e exibe "Quantidade indisponível em estoque". |
| **TA09.06** | **Consistência de dados:** O sistema garante que operações concorrentes não causem inconsistência nos valores de estoque. |

### Impacto nas User Stories Existentes

#### US04 - Manter Produto
- Adicionar campo "quantidade_estoque" no formulário de produto
- Atualizar TA03.01 e TA03.03 para incluir validação do campo quantidade
- Adicionar visualização da quantidade em estoque na listagem de produtos

#### US05 - Entrar Produto
- Modificar para chamar automaticamente a atualização de estoque (RF09.01)
- Atualizar TA04.01 para verificar se o estoque foi atualizado

#### US06 - Visualizar Estoque
- Atualizar descrição para refletir a nova estrutura de estoque
- Adicionar verificação de consistência nos dados exibidos

#### US08 - Realizar Venda
- Modificar para chamar automaticamente a atualização de estoque (RF09.02)
- Atualizar TA07.01 e TA07.02 para verificar atualização do estoque
- Adicionar caso de teste para cancelamento de venda (RF09.03)

#### US09 - Realizar Pagamento (renumerar para US10)
- Adicionar verificação de consistência entre itens vendidos e estoque

### Observações para Implementação Futura

1. Após implementação, modificar a relação estoque-produto para tabela separada
2. Implementar histórico de movimentação de estoque
3. Adicionar alertas para estoque baixo
4. Implementar conciliação periódica de estoque

### User Story US07 - Visualizar Estoque

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir a visualização consultiva do estoque atual, com dados em tempo real sincronizados com o módulo de controle de estoque (US06). |

| **Requisitos envolvidos** |                                                    |
|--------------------------|---------------------------------------------------|
| RF07.01                  | Consultar estoque atual (integrado com US06)      |
| RF07.02                  | Filtrar por categoria/produto                     |
| RF07.03                  | Visualizar histórico de movimentações             |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 6 h (+1h para integração com US06)  |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 8 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 2                            |
| **Testador**              | Pessoa 3                            |


| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **TA07.01** | **Visualização integrada:** Verificar se os dados exibidos refletem exatamente o estoque gerenciado pela US06 |
| **TA07.02** | **Atualização em tempo real:** Alterações feitas via US06 devem aparecer imediatamente na visualização |
| **TA07.03** | **Filtros avançados:** Deve permitir filtrar por: produtos com estoque crítico, produtos ausentes, etc. |
| **TA07.04** | **Dados consistentes:** A soma de entradas-saídas deve bater com o saldo atual |



### User Story US08 - Emitir Relatório de Estoque

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente da ótica gerar um relatório detalhado do estoque mais atual no sistema. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| Não especificado no doc de visão                      | ?                        |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Desejável                          |
| **Estimativa**            | 5 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 8 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 3                            |
| **Testador**              | Pessoa 3                            |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA06.01** | **Gerar Relatório com sucesso:** O gerente acessa o sistema, seleciona a opção "Emitir Relatório de Estoque" e o sistema gera um relatório detalhado com todas as informações do estoque atual. |
| **TA06.02** | **Filtrar Relatório com sucesso:** O gerente aplica filtros (como categoria, quantidade ou intervalo de datas) para o relatório, e o sistema retorna o relatório filtrado corretamente. |
| **TA06.03** | **Relatório vazio:** O gerente tenta emitir um relatório com filtros que não correspondem a nenhum produto no estoque. O sistema exibe a mensagem: "Nenhum produto encontrado para os critérios especificados". |
| **TA06.04** | **Relatório exportado com sucesso:** O gerente solicita a exportação do relatório (em formatos como PDF ou Excel), e o sistema salva o arquivo no formato solicitado. |
| **TA06.05** | **Cancelar Emissão de Relatório:** O gerente inicia o processo para emitir um relatório, mas decide cancelar antes de finalizar. O sistema retorna à tela anterior sem gerar o relatório. |



### User Story US09 - Realizar Venda

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir realizar vendas com integração total com o módulo de estoque (US06), garantindo atualização automática e consistência dos dados. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| RF09.01                   | Registrar Venda (com validação de estoque)        |
| RF09.02                   | Emitir Comprovante                                |
| RF09.03                   | Consultar Histórico                               |
| RF09.04                   | Cancelar Venda (com reversão de estoque - US06)   |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Importante                          |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 7 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 2                            |
| **Testador**              | Pessoa 3                            |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **TA09.01** | **Validação de estoque:** Impedir venda se quantidade > estoque disponível |
| **TA09.02** | **Atualização automática:** Verificar redução no estoque após venda |
| **TA09.03** | **Reversão no cancelamento:** Estoque deve ser restaurado se venda cancelada |
| **TA09.04** | **Log de movimentação:** Registrar relação venda-estoque |

### User Story US10 - Realizar Pagamento

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente e ao funcionário realizar o pagamento usando as informações de pagamento fornecidas pelo cliente. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| Não especificado no doc de visão                      | ?                                 |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Importante                          |
| **Estimativa**            | 8 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 7 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 2                            |
| **Testador**              | Pessoa 3                            |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA08.01** | **Realizar Pagamento com sucesso:** O gerente ou  funcionário, ao finalizar a venda, seleciona a forma de pagamento (como cartão, dinheiro ou Pix), insere os dados necessários e clica em "Confirmar Pagamento". O sistema exibe: "Pagamento concluído com sucesso". e gera automaticamente o comprovante de pagamento |
| **TA08.02** | **Realizar Pagamento com erro:** O gerente ou  funcionário tenta processar o pagamento, mas insere informações inválidas (como número de cartão incorreto). O sistema exibe: "Erro: Dados de pagamento inválidos. Verifique as informações". |
| **TA08.03** | **Pagamento Parcial:** O cliente solicita um pagamento parcial da compra. O gerente ou funcionário insere o valor pago, e o sistema calcula o saldo restante. O sistema exibe: "Pagamento parcial registrado. Saldo restante: {valor}". |
| **TA08.04** | **Cancelar Pagamento:** O gerente ou funcionário inicia o processo de pagamento, mas decide cancelar antes de finalizar. O sistema retorna à tela de vendas sem salvar as informações do pagamento. |
