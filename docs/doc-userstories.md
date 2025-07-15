# Documento Lista de User Stories

## DESCRIÇÃO

Este documento de User Stories descreve os requisitos e funcionalidades essenciais para o desenvolvimento de um sistema de gerenciamento de estoque para uma ótica. O objetivo é atender às necessidades dos usuários (gerente e equipe da ótica), garantindo um controle eficiente e organizado dos produtos em estoque, bem como processos de vendas e geração de relatórios.


## HISTÓRICO DE REVISÕES

| Data       | Versão  | Descrição                          | Autor    |
| :--------- | :-----: | :--------------------------------: | :-------- |
| 03/04/2025 | 0.0.1   | Template e descrição do documento  | Gustavo   |
| 04/04/2025 | 0.0.2   | Adicionando US.01 US.02 US.03 US.04 US.05 US.06 US.07 US.08 | Gabriel   |
| 05/04/2025 | 0.0.3   | Correções de inconsistências nas descrições, requisitos envolvidos e testes de aceitação | Gabriel   |
| 11/06/2025 | 0.0.4   | Adição da US06 - Manter Quantidade em Estoque e reordenação | Cayo      |
| 11/06/2025 | 0.0.5   | Adição da US11 Dashboard e ajustes na contagem de PF | Cayo      |
| 20/06/2025 | 0.0.6   | Criação da US função               | Gabriel   |
| 14/07/2025 | 0.0.7   | Adição das US13 - Manter Marca, US14 - Manter Modelo e US15 - Manter Usuário | Gabriel   |


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


### User Story US11 - Tela Home (Dashboard)

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | Como usuário do sistema, quero acessar uma tela inicial que mostre de forma organizada e intuitiva todas as rotas/funcionalidades disponíveis, para poder navegar eficientemente pelo sistema. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| RF11.01                   | Exibir menu de navegação principal                 |
| RF11.02                   | Agrupar funcionalidades por módulos                |
| RF11.03                   | Permitir acesso rápido às funções mais utilizadas  |
| RF11.04                   | Exibir informações resumidas do sistema            |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 3 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 5 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 3                            |
| **Testador**              | Pessoa 4                            |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **TA11.01** | **Acesso às rotas principais:** A tela deve exibir claramente os módulos: Cadastros, Estoque, Vendas e Relatórios, com ícones intuitivos. |
| **TA11.02** | **Navegação eficiente:** Cada item do menu deve redirecionar corretamente para a tela correspondente em até 2 cliques. |
| **TA11.03** | **Layout responsivo:** A tela deve se adaptar corretamente em desktop (1440px) e mobile (360px). |
| **TA11.04** | **Atalhos visíveis:** Deve exibir os 5 processos mais utilizados (ex: Nova Venda, Consultar Estoque) com destaque. |
| **TA11.05** | **Informações contextuais:** Deve mostrar resumo do dia (total de vendas, alertas de estoque baixo) quando aplicável. |
| **TA11.06** | **Personalização:** O gerente pode reorganizar os atalhos principais conforme necessidade. |


### User Story US12 - Manter Função

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao administrador cadastrar, editar, visualizar e excluir funções que serão atribuídas aos funcionários. Isso inclui informações como nome da função e salário base. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF04.01          | Inserir Função |
| RF04.02          | Listar Funções |
| RF04.03          | Atualizar Função |
| RF04.04          | Deletar Função |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 4 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 6 PF                                | 
| **Analista**              | Pessoa 1                            | 
| **Desenvolvedor**         | Pessoa 2                            | 
| **Revisor**               | Pessoa 3                            | 
| **Testador**              | Pessoa 4                            | 

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA04.01** | **Cadastrar Função com sucesso:** O administrador acessa a tela de cadastro de função, preenche os campos obrigatórios (como nome e salário base) e clica em "Salvar". O sistema exibe: "Função cadastrada com sucesso". |
| **TA04.02** | **Cadastrar Função com erro:** O administrador tenta cadastrar uma função com dados inválidos (por exemplo, nome em branco ou salário negativo). O sistema exibe: "Erro no cadastro. Verifique os campos obrigatórios". |
| **TA04.03** | **Editar Função com sucesso:** O administrador seleciona uma função existente, altera as informações e confirma. O sistema exibe: "Função atualizada com sucesso". |
| **TA04.04** | **Editar Função com erro:** O administrador tenta editar uma função, mas insere dados inválidos. O sistema exibe: "Alterações não salvas. Verifique os dados informados". |
| **TA04.05** | **Excluir Função com sucesso:** O administrador exclui uma função que não está vinculada a nenhum funcionário. O sistema exibe: "Função excluída com sucesso". |
| **TA04.06** | **Excluir Função com erro:** O administrador tenta excluir uma função que está vinculada a um ou mais funcionários. O sistema exibe: "Erro: esta função está associada a funcionários e não pode ser excluída". |
| **TA04.07** | **Pesquisar Função com sucesso:** O administrador realiza uma busca por nome de função e o sistema retorna os resultados esperados. |
| **TA04.08** | **Pesquisar Função sem resultados:** O administrador faz uma busca que não encontra funções. O sistema exibe: "Nenhuma função encontrada". |
| **TA04.09** | **Cancelar Cadastro de Função:** O administrador começa o cadastro, mas decide cancelar antes de salvar. O sistema retorna à tela anterior sem salvar os dados. |
| **TA04.10** | **Cancelar Edição de Função:** O administrador edita uma função, mas cancela antes de confirmar. O sistema descarta as alterações e retorna à tela anterior. |

### User Story US13 - Manter Marca

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente da ótica cadastrar, editar, visualizar e excluir informações sobre marcas de armações, lentes e outros produtos ópticos. Isso inclui o nome da marca, que deve ser único e obrigatório. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF13.01          | Inserir Marca |
| RF13.02          | Listar Marcas |
| RF13.03          | Atualizar Marca |
| RF13.04          | Deletar Marca |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 3 h                                 | 
| **Tempo Gasto (real):**   | -                                   | 
| **Tamanho Funcional**     | 5 PF                                | 
| **Analista**              | Pessoa 1                            | 
| **Desenvolvedor**         | Pessoa 2                            | 
| **Revisor**               | Pessoa 3                            | 
| **Testador**              | Pessoa 4                            | 

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **TA13.01** | **Cadastrar Marca com sucesso:** O gerente acessa "Cadastrar Marca", preenche o nome da marca corretamente (ex: Ray-Ban, Hoya) e clica em "Salvar". O sistema exibe: "✔ Marca cadastrada com sucesso!". |
| **TA13.02** | **Cadastrar Marca com erro:** O gerente tenta cadastrar uma marca sem preencher o nome ou com nome duplicado. O sistema exibe: "Erro: Este campo é obrigatório" ou "Já existe uma marca com este nome". |
| **TA13.03** | **Editar Marca com sucesso:** O gerente acessa a lista, seleciona uma marca, edita o nome e salva. O sistema exibe: "✔ Marca editada com sucesso!". |
| **TA13.04** | **Editar Marca com erro:** O gerente tenta editar a marca com um nome já existente. O sistema exibe: "Já existe uma marca com este nome". |
| **TA13.05** | **Excluir Marca com sucesso:** O gerente acessa a lista de marcas e clica em "Excluir" ao lado de uma marca. O sistema exibe: "Marca excluído com sucesso.". |
| **TA13.06** | **Listar Marcas:** O gerente acessa a tela de listagem de marcas e visualiza todas as marcas cadastradas no sistema. |
| **TA13.07** | **Cancelar Cadastro de Marca:** O gerente inicia o cadastro de uma marca, mas clica em "Cancelar". O sistema retorna à tela anterior sem salvar nada. |
| **TA13.08** | **Cancelar Edição de Marca:** O gerente inicia a edição de uma marca, mas clica em "Cancelar". O sistema volta à listagem sem aplicar mudanças. |

### User Story US14 - Manter Modelo

|               |                                                                                      |
| ------------- | :----------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente da ótica cadastrar, editar, visualizar e excluir modelos de armações ou lentes, associando cada modelo a uma marca. |

| **Requisitos envolvidos** |                |
| ------------------------- | :------------- |
| RF14.01                   | Inserir Modelo |
| RF14.02                   | Listar Modelos |
| RF14.03                   | Atualizar Modelo |
| RF14.04                   | Deletar Modelo |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 3 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 5 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 3                            |
| **Testador**              | Pessoa 4                            |

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **TA14.01** | **Cadastrar Modelo com sucesso:** O gerente preenche nome e marca e clica em "Salvar". O sistema exibe: "✔ Modelo cadastrado com sucesso!". |
| **TA14.02** | **Cadastrar Modelo com erro:** Nome em branco ou repetido. O sistema exibe mensagem de erro correspondente. |
| **TA14.03** | **Editar Modelo com sucesso:** O gerente altera nome ou marca e salva. O sistema exibe: "✔ Modelo editado com sucesso!". |
| **TA14.04** | **Editar Modelo com erro:** Nome duplicado. O sistema exibe: "Já existe um modelo com este nome". |
| **TA14.05** | **Excluir Modelo com sucesso:** O gerente clica em "Excluir". O sistema exibe: "Modelo excluído com sucesso.". |
| **TA14.06** | **Listar Modelos:** O gerente acessa a lista de modelos com nome e marca exibidos. |
| **TA14.07** | **Cancelar Cadastro de Modelo:** O gerente clica em "Cancelar". O sistema retorna sem salvar. |
| **TA14.08** | **Cancelar Edição de Modelo:** O gerente clica em "Cancelar". O sistema volta sem aplicar mudanças. |

### User Story US15 - Manter Usuário

|               |                                                                                     |
| ------------- | :---------------------------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir o cadastro e autenticação de usuários para acesso à plataforma da ótica, garantindo segurança e controle de acesso às funcionalidades do sistema. |

| **Requisitos envolvidos** |                |
| ------------------------- | :------------- |
| RF15.01                   | Cadastrar Usuário |
| RF15.02                   | Autenticar Usuário (Login) |
| RF15.03                   | Restringir Acesso à Plataforma para usuários autenticados |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 4 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 6 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 3                            |
| **Testador**              | Pessoa 4                            |

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **TA15.01** | **Cadastrar Usuário com sucesso:** O usuário preenche nome, e-mail e senha e clica em "Cadastrar". O sistema redireciona para a tela de login com sucesso. |
| **TA15.02** | **Cadastro com erro (username já existe):** O usuário tenta cadastrar com um nome de usuário já utilizado. O sistema exibe: "Já existe um usuário com esse username". |
| **TA15.03** | **Login com sucesso:** O usuário digita usuário e senha corretos e é redirecionado à plataforma. |
| **TA15.04** | **Login com erro:** O usuário informa dados inválidos. O sistema exibe: "usuário ou senha inválidos". |
| **TA15.05** | **Restringir acesso:** O usuário tenta acessar a plataforma sem login. O sistema redireciona para a tela de login. |
| **TA15.06** | **Campos obrigatórios:** Ao deixar algum campo vazio no cadastro ou login, o sistema impede o envio e exibe mensagem de erro. |
