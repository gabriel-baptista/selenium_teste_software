from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome('C:/testes/selenium/chromedriver.exe')

navegador.get('https://www.google.com.br')

navegador.find_element_by_name('q').send_keys('gabrieloliveira.dev' + Keys.ENTER)
# navegador.find_element_by_name('q').send_keys(Keys.RETURN)
