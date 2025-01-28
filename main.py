from create_account import CreateAccount
from home import TestHome
from men_section import MenCollections
from items import ItemView
from selenium import webdriver
# import time #time.sleep(1)
from time import sleep # sleep(1) mismo resultado de sleep en lina 2 y 3 diferente sintaxis


base_url = 'https://madison-island.com/'
signup_url ='https://madison-island.com/account/register'
# driver = webdriver.Chrome() # no se declara aqui ahora porque quiza se trabaje con uno diferente
categories = {
    'women':0,
    'men':1,
    'accesories':2,
    'home and decor':3
}

class TestSignUp:
    driver = None
    create_account = None #aqui debes estar llamando al archivo y no la clase CreateAccount
    home = None
    men_category = None
    items = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.create_account = CreateAccount(cls.driver) #Archivo(create_account) = Clase(CreateAccount)
        cls.home_interactions = TestHome(cls.driver)
        cls.men_category = MenCollections(cls.driver)
        cls.items = ItemView(cls.driver)
        cls.driver.get(base_url)
        cls.driver.implicitly_wait(10)


    def test_signup_valid_data(self):#Metodos de prueba

        valid_data = self.create_account #aqui se llama al nombre del archivo, no la clase del archivo CreateAccount

        valid_data.fill_first_name()
        valid_data.fill_last_name()
        valid_data.fill_email()
        valid_data.fill_password()
        valid_data.click_create_button()
        #LOCATE FIRST NAME SEND KEYS NOMBRE
        #LOCATE LAST NAME SEND KEYS NOMBRE

    def test_purchase_trouser(self):
        home = self.home_interactions
        men_category = self.men_category
        items = self.items
        home.click_men_category()
        men_category.click_item_by_class_name_and_index(0)
        items.select_size_by_index(2)
        items.select_color_by_index(0)
        items.click_add_to_cart_button()


    @classmethod
    def teardown_class(cls):
        sleep(10)
        cls.driver.quit()


#
# driver.get(base_url)
# current_url = driver.current_url
# assert base_url in driver.current_url, 'No estas en Madison-Island'
#
# sections = driver.find_elements(By.CLASS_NAME,'collection-grid-item')
# sections[categories['women']].click()
# assert 'women' in driver.current_url, 'No estas en la seccion women'
# women_section_title = driver.find_element(By.XPATH, '//h1/span')
# assert 'Collection:\nWomen' == women_section_title.text, 'te equivocaste'
#
#
# delancy_sweater_item = driver.find_element(By.LINK_TEXT,'DELANCY CARDIGAN SWEATER')
# delancy_sweater_item.click()
# item_title = driver.find_element(By.TAG_NAME, 'h1')
# assert 'delancy-cardigan-sweater' in driver.current_url
# assert 'DELANCY CARDIGAN SWEATER' == item_title.text
#
# sizes_dropdown = driver.find_element(By.ID,'SingleOptionSelector-0')
# sizes_selector = Select(sizes_dropdown)
# sizes_selector.select_by_value('M')
# sold_out_button = driver.find_element(By.ID, 'AddToCartText-product-template')
# assert 'SOLD OUT' == sold_out_button.text
# sleep(2)
# sizes_selector.select_by_value('L')
# add_to_cart = driver.find_element(By.ID, 'AddToCartText-product-template')
# assert 'ADD TO CART' == add_to_cart.text
# add_to_cart.click()
#
#
# shopping_cart_section_title = driver.find_element(By.XPATH, '//h1')
# shopping_item_list_name = driver.find_element(By.CLASS_NAME, 'list-view-item__title')
# quantity_box = driver.find_elements(By.CLASS_NAME,'cart__qty-input')
# quantity_box_value = quantity_box[0].get_attribute("value")
#
# assert 'DELANCY CARDIGAN SWEATER' == shopping_item_list_name.text
# assert 'cart' in driver.current_url
# assert 'Your cart' == shopping_cart_section_title.text
# assert '1' == quantity_box_value
#
# catalog = driver.find_element(By.XPATH, '//a[@href="collections/all"]')
# catalog.click()
#
# assert 'collections/all' in driver.current_url
#
# sleep(2)
# driver.quit()
#
