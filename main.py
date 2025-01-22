
from selenium import webdriver
# import time #time.sleep(1)
from time import sleep # sleep(1) mismo resultado de sleep en lina 2 y 3 diferente sintaxis
from selenium.webdriver.support.ui import Select
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
women_section_title = driver.find_element(By.XPATH, '//h1/span')
assert 'Collection:\nWomen' == women_section_title.text, 'te equivocaste'


delancy_sweater_item = driver.find_element(By.LINK_TEXT,'DELANCY CARDIGAN SWEATER')
delancy_sweater_item.click()
item_title = driver.find_element(By.TAG_NAME, 'h1')
assert 'delancy-cardigan-sweater' in driver.current_url
assert 'DELANCY CARDIGAN SWEATER' == item_title.text

sizes_dropdown = driver.find_element(By.ID,'SingleOptionSelector-0')
sizes_selector = Select(sizes_dropdown)
sizes_selector.select_by_value('M')
sold_out_button = driver.find_element(By.ID, 'AddToCartText-product-template')
assert 'SOLD OUT' == sold_out_button.text
sleep(2)
sizes_selector.select_by_value('L')
add_to_cart = driver.find_element(By.ID, 'AddToCartText-product-template')
assert 'ADD TO CART' == add_to_cart.text
add_to_cart.click()


shopping_cart_section_title = driver.find_element(By.XPATH, '//h1')
shopping_item_list_name = driver.find_element(By.CLASS_NAME, 'list-view-item__title')
quantity_box = driver.find_elements(By.CLASS_NAME,'cart__qty-input')
quantity_box_value = quantity_box[0].get_attribute("value")

assert 'DELANCY CARDIGAN SWEATER' == shopping_item_list_name.text
assert 'cart' in driver.current_url
assert 'Your cart' == shopping_cart_section_title.text
assert '1' == quantity_box_value

catalog = driver.find_element(By.XPATH, '//a[@href="collections/all"]')
catalog.click()

assert 'collections/all' in driver.current_url

sleep(2)
driver.quit()

