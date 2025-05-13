# Documento Lista de User Stories

## DESCRIÇÃO

Este documento de User Stories descreve os requisitos e funcionalidades essenciais para o desenvolvimento de um sistema de gerenciamento de estoque para uma ótica. O objetivo é atender às necessidades dos usuários (gerente e equipe da ótica), garantindo um controle eficiente e organizado dos produtos em estoque, bem como processos de vendas e geração de relatórios.


## HISTÓRICO DE REVISÕES

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 03/04/2025 | 0.0.1   | Template e descrição do documento  | Gustavo |
| 04/04/2025 | 0.0.2   | Adicionando US.01 US.02 US.03 US.04 US.05 US.06 US.07 US.08                 | Gabriel |
| 05/04/2025 | 0.0.3   | Correções de inconsistências nas descrições, requisitos envolvidos e testes de aceitação | Gabriel |


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



### User Story US06 - Visualizar Estoque

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao gerente ou ao funcionário da ótica visualizar o estoque atual no sistema. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| Não especificado no doc de visão                      | ?                                 |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
| **Estimativa**            | 5 h                                 |
| **Tempo Gasto (real):**   | -                                   |
| **Tamanho Funcional**     | 8 PF                                |
| **Analista**              | Pessoa 1                            |
| **Desenvolvedor**         | Pessoa 2                            |
| **Revisor**               | Pessoa 3                            |
| **Testador**              | Pessoa 1                            |

| Testes de Aceitação (TA)  |                                     |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA05.01** | **Visualizar Estoque com sucesso:** O gerente ou funcionário acessa o sistema com suas credenciais, seleciona a opção "Visualizar Estoque" e o sistema apresenta as informações atuais dos produtos em estoque. |
| **TA05.02** | **Filtrar Estoque com sucesso:** O gerente ou funcionário utiliza um filtro para buscar por categoria ou tipo de produto, e o sistema retorna apenas os itens correspondentes ao filtro aplicado. |
| **TA05.03** | **Estoque vazio ou sem resultados:** O gerente ou funcionário realiza uma busca ou aplica um filtro que não retorna resultados. O sistema exibe a mensagem: "Nenhum produto encontrado". |
| **TA05.04** | **Exibição em tempo real:** O gerente ou funcionário acessa o estoque, e o sistema garante que as informações apresentadas estejam atualizadas em tempo real. |
| **TA05.05** | **Cancelar Visualização de Estoque:** O gerente ou funcionário inicia o processo para visualizar o estoque, mas decide cancelar antes de confirmar ou aplicar filtros. O sistema retorna à tela anterior. |



### User Story US07 - Emitir Relatório de Estoque

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



### User Story US08 - Realizar Venda

|               |                                                                 |
| ------------- | :-------------------------------------------------------------- |
| **Descrição** | O sistema deve permitir ao funcionário realizar a venda de produtos, com atualização automática do estoque, emissão de comprovante e acesso ao histórico de vendas. |

| **Requisitos envolvidos** |                                                    |
| ------------------------- | -------------------------------------------------- |
| RF04.01                      | Registrar Venda                                 |
| RF04.02                      | Emitir Comprovante                              |
| RF04.03                      | Consultar Histórico de Vendas                                 |

|                           |                                     |
| ------------------------- | ----------------------------------- |
| **Prioridade**            | Essencial                           |
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
| **TA07.01** | **Realizar Venda com sucesso:** O funcionário acessa o sistema com suas credenciais, seleciona a opção "Realizar Venda", adiciona produtos ao carrinho, confirma os dados do cliente e clica em "Concluir Venda". O sistema exibe: "Venda realizada com sucesso" e gera automaticamente o comprovante de venda. |
| **TA07.02** | **Adicionar Produto ao Carrinho com erro:** O funcionário tenta adicionar um produto que não está disponível em estoque. O sistema exibe a mensagem: "Erro: Produto indisponível no estoque". |
| **TA07.03** | **Editar Carrinho de Compras:** Durante a venda, o funcionário altera a quantidade de produtos ou remove itens do carrinho. O sistema atualiza os valores totais e exibe: "Carrinho atualizado com sucesso". |
| **TA07.04** | **Finalizar Venda com erro:** O funcionário tenta finalizar uma venda sem selecionar todos os dados obrigatórios (como cliente ou forma de pagamento). O sistema exibe: "Erro: Preencha todas as informações obrigatórias". |
| **TA07.05** | **Cancelar Venda:** O funcionário inicia uma venda, mas decide cancelar antes de finalizar. O sistema limpa o carrinho e retorna à tela inicial de vendas sem salvar os dados. |
| **TA07.06** | **Consultar Histórico de Vendas:** O funcionário acessa o histórico de vendas, filtra por data ou produto, e o sistema exibe corretamente os resultados. |


### User Story US09 - Realizar Pagamento

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
