import time
import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
actions = ActionChains(browser)
browser.maximize_window()
browser.get('https://journal.top-academy.ru/ru/auth/login/index')
actions = ActionChains(browser)


waitingPage = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))

typeLogin = browser.find_element(By.XPATH, '//*[@id="username"]').send_keys("Makee_jv78")

typePass = browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("0Cf5Lt41")

pushEnter = browser.find_element(By.XPATH, '//*[@id="1"]/form/button').click()

waitingBar = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//ng-component/ng-component/div/div[1]'))).click()


waitingMaterials = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Учебные материалы")]'))).click()

getMaterials = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//div/a[contains(@download, "null")]')))

#downloadMat =  WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '(//img[contains(@src, "material-picture.png")])[1]'))).click()

html = browser.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.END)
time.sleep(2)
html.send_keys(Keys.END)
time.sleep(2)
html.send_keys(Keys.END)
time.sleep(2)
html.send_keys(Keys.END)
time.sleep(2)
html.send_keys(Keys.END)
html.send_keys(Keys.HOME)


arr = []
for i in range(1, 58):

    st = str(i)
    xpathUpdate = "(" + '//img[contains(@src, "material-picture.png")]' + ')' + '[' + st + "]"
    arr.append(xpathUpdate)
    
time.sleep(2)
for k in range(len(arr)):
    downloadMat = browser.find_element(By.XPATH, arr[k]).click()


# Makee_jv78
# 0Cf5Lt41
# //div/a[contains(@download, "null")] их 57
# '(//img[contains(@src, "material-picture.png")])[1]' ih 1 iz 57
