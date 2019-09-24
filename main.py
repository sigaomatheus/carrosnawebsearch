from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('browser.privatebrowsing.autostart', True)
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://www.carrosnaweb.com.br/avancada.asp')


def list_all_brands():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'fabricante'))
    )

    brand_select = driver.find_element_by_xpath('//select[@id="fabricante"]')
    all_brands = brand_select.find_elements_by_tag_name('option')
    print('Brands:')
    for each_brand in all_brands:
        print(each_brand.get_attribute('value'))


def select_brand(brand_name):
    brand_select = driver.find_element_by_xpath('//select[@id="fabricante"]')
    all_brands = brand_select.find_elements_by_tag_name('option')

    for each_brand in all_brands:
        each_brand_name = each_brand.get_attribute('value')
        if brand_name.lower() == str(each_brand_name).lower():
            each_brand.click()
            break


def list_all_models():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'varnome'))
    )

    model_select = driver.find_element_by_xpath('//select[@id="varnome"]')
    all_models = model_select.find_elements_by_tag_name('option')
    print('Models:')
    for each_model in all_models:
        print(each_model.get_attribute('value'))


def select_model(model_name):
    model_select = driver.find_element_by_xpath('//select[@id="varnome"]')
    all_models = model_select.find_elements_by_tag_name('option')

    for each_model in all_models:
        each_model_name = each_model.get_attribute('value')
        if model_name.lower() == str(each_model_name).lower():
            each_model.click()
            break


def select_year():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'anoini'))
    )

    year_select = driver.find_element_by_xpath('//select[@id="anoini"]')
    all_years = year_select.find_elements_by_tag_name('option')

    fab_year = str(input())

    for each_year in all_years:
        if fab_year == each_year.get_attribute('value'):
            each_year.click()
            break


def select_version(brand_name):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    )

    all_versions = driver.find_elements_by_xpath('//*[starts-with(@title, "' + brand_name.capitalize() + '")]')
    for each_version in all_versions:
        print('[' + str(all_versions.index(each_version)+1) + '] ' + each_version.get_attribute('title'))

    version_n = int(input())

    for each_version in all_versions:
        if version_n-1 == all_versions.index(each_version):
            each_version.click()
            break


if __name__ == '__main__':
    full_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
    )
    print('Ready')

    list_all_brands()
    brand_name = input()
    select_brand(brand_name)

    list_all_models()
    model_name = input()
    select_model(model_name)

    select_year()
    driver.find_element_by_id('submit1').click()

    select_version(brand_name)
