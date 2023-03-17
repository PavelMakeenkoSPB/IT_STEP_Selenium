from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

 #================ GENERAL FUNCTIONS ==================#
  

#Откроем главную страницу в Chrome. Передадим в качестве аргумента адрес страницы.
@given('on Chrome website "{url}"')
def step(context, url):
#Измените строку, для выполнения теста в другом браузере
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
    
    context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(text)
    
  
#Теперь нажмем на кнопку "Поиск в Google"  
@when("push Google Search button with text '{text}'")
def step(context, text):

    context.browser.find_element(By.CSS_SELECTOR, '[name="btnK"]').click()
    
    
    
    
    
    
# #Проверяем количество выданных поиском результатов на странице
@when("count the number of results per page")
def step(context):
    
    c = 0
    context.browser.find_element(By.XPATH, '//*[@id="rso"]') 
    
    

#Проверяем общее количество найденных странице

#Проверяем правильность размещения картинок в результатах поиска


    
    # //*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[1]/div/a/div/span/div/img
    # //*[@id="rso"]/div[2]/div/div/div/div/div/div[1]/div/a/div/span/div/img    
    # //*[@id="rso"]/div[9]/div/div/div/div[1]/div/a/div/span/div/img
    
    # //*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/div[1]/div/a/div/span/div/img
    # //*[@id="rso"]/div[11]/div/div/div/div[1]/div/a/div/span/div/img
    
    
//*[@id="1_aeg5w01-00"]
//*[@id="1_aeg5w02-00"]
//*[@id="2_aeg5w0b-00"]
//*[@id="2_aeg5w0a-00"],
//*[@id="search-result"]/li[1]/div/div[1]/a/div/div
//*[@id="search-result"]/li[2]/div/div[1]/a/div/div


    