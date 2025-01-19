from locale import currency
from os.path import curdir

from selenium import webdriver
# import time #time.sleep(1)
from time import sleep # sleep(1) mismo resultado de sleep en lina 2 y 3 diferente sintaxis
from selenium.webdriver.common.by import By

base_url = 'https://madison-island.com/'
categories = {
    'women':0,
    'men':1,
    'accesories':2,
    'home and decor':3
}

driver = webdriver.Chrome()

driver.get(base_url)
current_url = driver.current_url
assert base_url in driver.current_url, 'No estas en Madison-Island'
sections = driver.find_elements(By.CLASS_NAME,'collection-grid-item')
sections[categories['women']].click()
assert 'women' in driver.current_url, 'No estas en la seccion women'


sleep(2)
driver.quit()

