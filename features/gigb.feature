Feature: cadastro finalizado com sucesso
  
  Scenario: Verificar presenca de logo home page
    # Given iniciar o navegador Chrome
    Given Abrir pagina inicial do Gig B
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
    



# Dado , Quando , Então, E    