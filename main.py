from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer as SS
import unicodecsv
import decode

# Configura o Firefox para iniciar em modo headless e em navegação privada
firefox_opt = Options()
firefox_opt.headless = True
firefox_prof = webdriver.FirefoxProfile()
firefox_prof.set_preference('browser.privatebrowsing.autostart', True)

# Inicia o browser carregando as configurações definidas anteriormente
driver = webdriver.Firefox(options=firefox_opt, firefox_profile=firefox_prof)
driver.get('https://www.carrosnaweb.com.br/avancada.asp')


# Função para buscar todas as marcas
def busca_todas_marcas():
    # Aguarda até que o elemento de select das marcas esteja clicável
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'fabricante'))
    )

    # Pega o elemento select que contém as marcas disponíveis
    select_marcas = driver.find_element_by_xpath('//select[@id="fabricante"]')

    # Pega todas as opções do select de marcas
    todas_marcas = select_marcas.find_elements_by_tag_name('option')

    return todas_marcas


# Função para listar todas as marcas disponíveis
def lista_todas_marcas():
    # Imprime todas as marcas que estão como opção no select de marcas
    print('Marcas:')
    for cada_marca in busca_todas_marcas():
        print(cada_marca.get_attribute('value'))


# Função para selecionar a marca escolhida
def seleciona_marca(nome_marca):
    # Percorre todas as opções do select de marcas até encontrar a marca escolhida para clicar
    for cada_marca in busca_todas_marcas():
        if nome_marca.lower() == cada_marca.get_attribute('value').lower():
            cada_marca.click()
            break


def busca_todos_modelos():
    # Aguarda até que o elemento de select dos modelos esteja clicável
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'varnome'))
    )

    # Pega o elemento de select que contém os modelos disponíveis
    select_modelos = driver.find_element_by_xpath('//select[@id="varnome"]')

    # Pega todas as opções do select de modelos
    todos_modelos = select_modelos.find_elements_by_tag_name('option')

    return todos_modelos


# Função para listar todos os modelos disponíveis da marca
def lista_todos_modelos():
    # Imprime todos os modelos que estão como opção no select de modelos
    print('Modelos:')
    for cada_modelo in busca_todos_modelos():
        print(cada_modelo.get_attribute('value'))


# Função para selecionar o modelo escolhido
def seleciona_modelo(nome_modelo):
    # Percorre todas as opções do select de modelos até encontrar o modelo escolhido para clicar
    for cada_modelo in busca_todos_modelos():
        if nome_modelo.lower() == cada_modelo.get_attribute('value').lower():
            cada_modelo.click()
            break


# Função para buscar os anos de fabricação e modelo
def busca_anos():
    # Aguarda até que o elemento de select do ano esteja clicável
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'anoini'))
    )

    # Pega o elemento de select que contém os anos disponíveis
    select_ano_fab = driver.find_element_by_xpath('//select[@id="anoini"]')
    select_ano_mod = driver.find_element_by_xpath('//select[@id="anofim"]')

    # Pega todas as opções dos select de anos
    todos_anos_fab = select_ano_fab.find_elements_by_tag_name('option')
    todos_anos_mod = select_ano_mod.find_elements_by_tag_name('option')

    return todos_anos_fab, todos_anos_mod


# Função para selecionar o ano
def seleciona_ano(escolha_ano):
    ano_fab, ano_mod = busca_anos()
    # Percorre todas as opções do select de ano de fabricação até encontrar o ano escolhido para clicar
    for cada_ano_fab in ano_fab:
        if escolha_ano == cada_ano_fab.get_attribute('value'):
            cada_ano_fab.click()
            break

    # Percorre todas as opções do select de ano de modelo até encontrar o ano escolhido para clicar
    for cada_ano_mod in ano_mod:
        if escolha_ano == cada_ano_mod.get_attribute('value'):
            cada_ano_mod.click()
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

    # Pega os títulos das informações da página da versão e imprime
    # titulo_info = SS('font', color='darkred', face='arial', size=2)
    # titulo__info_soup = (BS(pagina_versao, 'html.parser', parse_only=titulo_info))
    # for cada_titulo_info in titulo_info_soup.stripped_strings:
    #     print(cada_titulo_info)

    titulo_info = SS('font', color='darkred', face='arial', size=2)
    titulo_info_soup = (BS(pagina_versao, 'html.parser', parse_only=titulo_info))
    titulo = [cada_titulo.decode('utf-8') for cada_titulo in titulo_info_soup.stripped_strings]

    with open('info.csv', 'a') as csv_file:
        w = unicodecsv.writer(csv_file)
        for p in range(len(titulo)):
            w.writerow([titulo[p]])
        w.writerow([])

    # Pega os valores das informações da página da versão e imprime
    # valor_info = SS('font', face='arial', size=2)
    # valor_soup = (BS(pagina_versao, 'html.parser', parse_only=valor_info))
    # for cada_valor_info in valor_soup.stripped_strings:
    #     print(cada_valor_info)


def main():
    pagina_completa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
    )
    print('Ready\n')

    busca_todas_marcas()
    lista_todas_marcas()
    nome_marca = input('\nEscolha a marca: ')
    seleciona_marca(nome_marca)

    busca_todos_modelos()
    lista_todos_modelos()
    nome_modelo = input('\nEscolha o modelo: ')
    seleciona_modelo(nome_modelo)

    escolha_ano = input(str('Escolha o ano do modelo (1954-2020): '))
    seleciona_ano(escolha_ano)

    driver.find_element_by_id('submit1').click()

    lista_versoes(nome_marca)
    escolha_versao = input('\nEscolha a versão: ')
    seleciona_versao(nome_marca, int(escolha_versao))

    pagina_versao = driver.page_source
    soup_pagina_versao(pagina_versao)
    driver.quit()


if __name__ == '__main__':
    main()