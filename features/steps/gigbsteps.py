from behave import *
from time import sleep

# @given('iniciar o navegador Chrome')
# def iniciarNavegador(context):
#     context.driver = webdriver.Chrome(executable_path='C:\drive\chromedriver.exe')

@given('Abrir pagina inicial do Gig B')
def abrirPaginaInicial(context):
    context.driver.get('https://sistema-gigb.web.app')
    
@then('devo verificar a presenca da logo na pagina')
def verificarLogo(context):
    status = context.driver.find_element_by_xpath('//img[@class="logo-gigb"]').is_displayed()
    assert status is True

@then('devo clicar em cadastro')
def click_in_registration(context):
    context.driver.find_element_by_xpath("//span[contains(text(), 'Cadastro')]").click()
    sleep(1)


@then('devo clicar em Colaborador')
def click_in_collaborator(context):
    context.driver.find_element_by_xpath("//button[contains(text(), 'Colaborador')]").click()
    sleep(1)


@then('preenche o campo com o CPF "{cpf}"')
def fill_cpf(context, cpf):
    context.driver.find_element_by_xpath("//input[@name = 'CPF']").send_keys(cpf)
    sleep(1)
    
    
@then('preenche o campo Nome Completo com o valor "{nome}"')
def fill_name(context, nome):
    context.driver.find_element_by_xpath("//input[@name = 'Nome completo']").send_keys(nome)
    sleep(1)

@then('preenche o grau de escolaridade "{escolaridade}"')
def fill_schooling(context, escolaridade):
    context.driver.find_element_by_xpath("//div[@class =  'mat-select-value ng-tns-c50-4']").click()
    context.driver.find_element_by_xpath(f"//span[contains(text(), '{escolaridade}')]").click()
    sleep(1)
    
@then('preenche a data de nascimento com "{data_nascimento}"')
def fill_date_birthday(context, data_nascimento):
    context.driver.find_element_by_xpath("//input[@name='data-nascimento']").send_keys(data_nascimento)
    sleep(1)

@then('preenche o campo de email com "{email}"')
def fill_email(context, email):
    context.driver.find_element_by_xpath("//input[@name='E-mail']").send_keys(email)
    sleep(1)
    
@then('preenche o campo de natarulidade com "{naturalidade}"')
def fill_naturalness(context, naturalidade):
    context.driver.find_element_by_xpath("//input[@name='naturalidade']").send_keys(naturalidade)
    sleep(1)
    
@then('preenche o campo de estado civil com "{estado_civil}"')
def fill_marital_status(context, estado_civil):
    context.driver.find_element_by_xpath("//div[@class = 'mat-form-field-infix ng-tns-c48-9']").click()
    context.driver.find_element_by_xpath(f"//span[contains(text(), '{estado_civil}')]").click()
    sleep(1)
    
@then('preenche o numero de dependentes com "{dependente}"')
def fill_dependents(context, dependente):
    context.driver.find_element_by_xpath("//input[@name='']").send_keys(dependente)
    sleep(1)
    
@then('preenche o campo de telefone com "{telefone}"')
def fill_fone(context, telefone):
    context.driver.find_element_by_xpath("//input[@name='Telefone']").send_keys(telefone)
    sleep(1)
    
@then('preenche o campo de cargo com "{cargo}"')
def fill_office(context, cargo):
    context.driver.find_element_by_xpath("//input[@name='Cargo']").send_keys(cargo)
    sleep(1)
    
@then('preenche o campo de CEP com "{cep}"')
def fill_cep(context, cep):
    context.driver.find_element_by_xpath("//input[@name='CEP']").send_keys(cep)
    
@then('preenche o campo do numero da casa com "{numero}"')
def fill_number(context, numero):
    context.driver.find_element_by_xpath("//input[@name='CEP']").send_keys(numero)
    
@then('preenche o campo de complemento com "{complementp}"')
def fill_complement(context, complemento):
    context.driver.find_element_by_xpath("//input[@name='Complemento']").send_keys(complemento)

@then('clicamos no botão de salvar')
def click_button_save(context):
    context.driver.find_element_by_xpath("//div[@class = 'mat-focus-indicator btn mat-stroked-button mat-button-base'").click()
                                         
@then('deveria aparecer a mensagem de sucesso')
def message_sucess(context):
    pass        