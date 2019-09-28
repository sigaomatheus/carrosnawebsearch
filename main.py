from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from bs4 import SoupStrainer


# Configura o perfil do Firefox para iniciar o navegador em navegação privada
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('browser.privatebrowsing.autostart', True)

# Inicia o browser carregando o perfil definido anteriormente
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://www.carrosnaweb.com.br/avancada.asp')


# Função para listar todas as marcas disponíveis
def lista_todas_marcas():
    # Aguarda até que o elemento de select das marcas esteja clicável
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'fabricante'))
    )

    # Pega o elemento select que contém as marcas disponíveis
    select_marcas = driver.find_element_by_xpath('//select[@id="fabricante"]')

    # Pega todas as opções do select de marcas
    todas_marcas = select_marcas.find_elements_by_tag_name('option')

    # Imprime todas as marcas que estão como opção no select de marcas
    print('Marcas:')
    for cada_marca in todas_marcas:
        print(cada_marca.get_attribute('value'))


# Função para selecionar a marca escolhida
def seleciona_marca(nome_marca):
    # Pega o elemento select que contém as marcas disponíveis
    select_marcas = driver.find_element_by_xpath('//select[@id="fabricante"]')

    # Pega todas as opções do select de marcas
    todas_marcas = select_marcas.find_elements_by_tag_name('option')

    # Percorre todas as opções do select de marcas até encontrar a marca escolhida para clicar
    for cada_marca in todas_marcas:
        cada_nome_marca = cada_marca.get_attribute('value')
        if nome_marca.lower() == str(cada_nome_marca).lower():
            cada_marca.click()
            break


# Função para listar todos os modelos disponíveis da marca
def lista_todos_modelos():
    # Aguarda até que o elemento de select dos modelos esteja clicável
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'varnome'))
    )

    # Pega o elemento de select que contém os modelos disponíveis
    select_modelos = driver.find_element_by_xpath('//select[@id="varnome"]')

    # Pega todas as opções do select de modelos
    todos_modelos = select_modelos.find_elements_by_tag_name('option')

    # Imprime todos os modelos que estão como opção no select de modelos
    print('Modelos:')
    for cada_modelo in todos_modelos:
        print(cada_modelo.get_attribute('value'))


# Função para selecionar o modelo escolhido
def seleciona_modelo(nome_modelo):
    # Pega o elemento de select que contém os modelos disponíveis
    select_modelo = driver.find_element_by_xpath('//select[@id="varnome"]')

    # Pega todas as opções do select de modelos
    todos_modelos = select_modelo.find_elements_by_tag_name('option')

    # Percorre todas as opções do select de modelos até encontrar o modelo escolhido para clicar
    for cada_modelo in todos_modelos:
        cada_nome_modelo = cada_modelo.get_attribute('value')
        if nome_modelo.lower() == str(cada_nome_modelo).lower():
            cada_modelo.click()
            break


# Função para selecionar o ano do modelo
def seleciona_ano(ano_fabricacao):
    # Aguarda até que o elemento de select do ano esteja clicável
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'anoini'))
    )

    # Pega o elemento de select que contém os anos disponíveis
    select_ano = driver.find_element_by_xpath('//select[@id="anoini"]')

    # Pega todas as opções do select de anos
    todos_anos = select_ano.find_elements_by_tag_name('option')

    # Percorre todas as opções do select de ano até encontrar o ano escolhido para clicar
    for cada_ano in todos_anos:
        if ano_fabricacao == cada_ano.get_attribute('value'):
            cada_ano.click()
            break


# Função para listar todas as versões disponíveis do modelo
def lista_versoes(nome_marca):
    # Aguarda até que o elemento que contém todas as versões esteja disponível
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    )

    # Pega todos os elementos que contém o nome de uma versão
    todas_versoes = driver.find_elements_by_xpath(f'//*[starts-with(@title, "{nome_marca.capitalize()}")]')

    # Percorre todos os elementos que contém o nome de uma versão para imprimir cada uma
    print('\nVersões:')
    for cada_versao in todas_versoes:
        print('[' + str(todas_versoes.index(cada_versao) + 1) + '] ' + cada_versao.get_attribute('title'))


# Função para selecionar a versão do modelo
def seleciona_versao(nome_marca, escolha_versao):
    # Aguarda até que o elemento que contém todas as versões esteja disponível
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    )

    # Pega todos os elementos que contém o nome de uma versão
    todas_versoes = driver.find_elements_by_xpath(f'//*[starts-with(@title, "{nome_marca.capitalize()}")]')

    for cada_versao in todas_versoes:
        if escolha_versao-1 == todas_versoes.index(cada_versao):
            cada_versao.click()
            break


# Função para BeautifulSoup
def soup_pagina_versao(pagina_versao):
    # Aguarda até que o elemento que contém todas as informações esteja disponível
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    )

    # all_info_name = SoupStrainer(color='darkred', face='arial', size=2)
    # soup = (BeautifulSoup(pagina_versao, 'html.parser', parse_only=all_info_name))
    # for string in soup.stripped_strings:
    #     print(repr(string))

    all_info_value = SoupStrainer('font', face='arial', size=2)
    soup = (BeautifulSoup(pagina_versao, 'html.parser', parse_only=all_info_value))
    for string in soup.stripped_strings:
        print(repr(string))


if __name__ == '__main__':
    pagina_completa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
    )
    print('Ready\n')

    lista_todas_marcas()
    nome_marca = input('\nEscolha a marca: ')
    seleciona_marca(nome_marca)

    lista_todos_modelos()
    nome_modelo = input('\nEscolha o modelo: ')
    seleciona_modelo(nome_modelo)

    ano_fabricacao = input(str('Escolha o ano de fabricação: '))
    seleciona_ano(ano_fabricacao)

    driver.find_element_by_id('submit1').click()

    lista_versoes(nome_marca)
    escolha_versao = input('\nEscolha a versão: ')
    seleciona_versao(nome_marca, int(escolha_versao))

    pagina_versao = driver.page_source
    soup_pagina_versao(pagina_versao)
