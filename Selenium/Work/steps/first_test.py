from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('"{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get(url)

#Теперь нажмем на кнопку "Найти"
@when("push button with '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//button'))
    )
    context.browser.find_element(By.NAME, 'text').send_keys(text, Keys.ENTER)
    #context.browser.find_element(By.NAME, 'text').send_keys(Keys.ENTER)


#Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element(By.XPATH,'//*[contains(text(), "%s")]' % text)
        
    #context.browser.quit()

@then("counter '{text}'")
def step(context, text):
    # WebDriverWait(context.browser, 120).until(
        # EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    # )
    assert context.browser.find_element(By.CSS_SELECTOR, '//*[@id="search-result"]')

# count(//element/Element1[namespace-uri()='mynamespace'])

# //*[@id="search-result"]/li[1]/div/div[1]/a/div/div
# //*[@id="search-result"]/li[3]/div/div[1]/a/div/div