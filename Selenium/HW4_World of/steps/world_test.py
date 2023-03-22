from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

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
   
    
#Проверяем, что количество выданных поиском результатов на странице равно 9
@when("number of search results per page is 9")
def step(context):
    CounterOfResultOnPage = context.browser.find_elements(By.XPATH, '//*[@id="rso"]/div') 
    
    assert int(len(CounterOfResultOnPage)) == 9
    
    
#Проверяем наличие отчёта о найденных результатах и его содержание
@when ("counter of search contains number of results")
def step(context, ):
    TextOfResault = context.browser.find_element(By.XPATH, '//*[@id="result-stats"]').is_displayed()
    context.browser.find_element(By.XPATH,'//*[contains(text(), "Результатов: примерно 777")]')
    
       
#Проверяем правильность размещения картинок в результатах поиска
@when ("all of 4 images are displayed in results correctly")
def step(context):
    context.browser.implicitly_wait(20)
    ImageInResult = context.browser.find_element(By.XPATH,'//*[@alt = "Бернский зенненхунд, источник: ru.wikipedia.org"]').is_displayed()
    StyleCorrect = context.browser.find_elements(By.XPATH,"//*[contains(@style,'border-radius:8px;height:92px;width:92px')]")

    assert ImageInResult == True and int(len(StyleCorrect)) == 4
    

 
 
# =======================  World of ================================ 

# Кликаем повторно на поле поиска, чтобы получить выпадающий список
@when ('click into search field')
def step(context):
    context.browser.find_element(By.CSS_SELECTOR, '[name="q"]').click()
    
# Ищем картинку первого выпадающего элемента списка строки поиска    
@when ('first falling object in field')
def step(context):
   s = context.browser.find_element("By.xpath(//div[@class='sbic vYOkbe' and style='background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCKjfMoEu9i-j5v2RNUJcXFQl9UHQ3zhme63IhreRHwmAOkiK8EhaRiQJL&s=10');")
   assert s is True 

@when ('the number of options in the drop-down list')
def step(context):
    OptionsInList = context.browser.find_elements("By.XPATH(
    
