from selenium import webdriver
from selenium.webdriver.common.by import By

men_categories_items = 'grid__item--collection-template'

class MenCollections:

    def __init__(self,driver):
        self.driver = driver

    def click_item_by_class_name_and_index(self,index):
        items_list = self.driver.find_elements(By.CLASS_NAME, men_categories_items)
        items_list[index].click()