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
        