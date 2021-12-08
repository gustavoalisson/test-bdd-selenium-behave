Feature: cadastro finalizado com sucesso
  
  Scenario: Verificar presenca de logo home page
    # Given iniciar o navegador Chrome
    Given Abrir pagina inicial do Gig B
    And fazer login com usuario cadastrado para logar
    Then devo verificar a presenca da logo na pagina
    # And fechar navegador

  Scenario: deveria criar um usuario
    # When abrir a pagina a pagina inicial do Gig B
    Then devo clicar em cadastro
    And devo clicar em Colaborador
    And preenche o campo com o CPF "113.688.124-73"
    And preenche o campo Nome Completo com o valor "Alisson Lindo"
    And preenche o grau de escolaridade "Ensino Superior Incompleto"
    And preenche a data de nascimento com "01/04/1997"
    And preenche o campo de email com "gustavoalisson@gmail.com"
    And preenche o campo de natarulidade com "Brasileiro"
    And preenche o campo de estado civil com "Solteiro"
    And preenche o numero de dependentes com "0"
    And preenche o campo de telefone com "81994789090"
    And preenche o campo de cargo com "Analista de Sistemas"
    And preenche o campo de CEP com "54330212"
    And preenche o campo do numero da casa com "655"
    And preenche o campo de complemento com "casa"

    And clicamos no botão de salvar
    # Then deveria aparecer a mensagem de sucesso 
