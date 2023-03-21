from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import parse

 #================ GENERAL FUNCTIONS ==================#
  

#Откроем главную страницу в Chrome. Передадим в качестве аргумента адрес страницы.
@given('on Chrome website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    chrome_options = Options()
    
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get(url)
    
#Откроем главную страницу в Edge. Передадим в качестве аргумента адрес страницы.    
@given('on Edge website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
    context.browser = webdriver.Edge()
    context.browser.maximize_window()
    context.browser.get(url)
 
 #Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    assert context.browser.find_element(By.XPATH,'//*[contains(text(), "%s")]' % text)
    
  
 #====================== GOOGLE ===========================#
 
#Теперь введём запрос в Google
@when("insert to field text '{text}'")
def step(context, text):
    context.browser.implicitly_wait(4)
    context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(text)
    
  
#Теперь нажмем на кнопку "Поиск в Google"  
@when("push Google Search button with text '{text}'")
def step(context, text):

    context.browser.find_element(By.CSS_SELECTOR, '[name="btnK"]').click()
   
    
# #Проверяем, что количество выданных поиском результатов на странице равно 9
@when("count the number of results per page is 9")
def step(context):
    
    counter_array = context.browser.find_elements(By.XPATH, '//*[@id="rso"]/div') 
    
    assert int(len(counter_array)) == 9
    
    
#Проверяем наличие отчёта о найденных результатах
@when ("amount of search results exists '{text}'")
def step(context, text):
   
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    )
    result_exists = context.browser.find_element(By.XPATH, '//*[@id="result-stats"]').is_displayed()
    
    assert result_exists == True and context.browser.find_element(By.XPATH,'//*[contains(text(), "%s")]' % text)

#Проверяем правильность размещения картинок в результатах поиска
@when ("image is displayed in results")
def step(context):
    context.browser.implicitly_wait(20)
    result_image = context.browser.find_element(By.TAG_NAME,'img').is_displayed()

    assert result_image is True
    
