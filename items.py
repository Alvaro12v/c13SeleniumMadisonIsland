from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


SIZE_DROPDOWN = 'SingleOptionSelector-0'
color_dropdown = 'SingleOptionSelector-1'
Button_cart = 'AddToCartText-product-template'

class ItemView:
    def __init__(self,driver):
        self.driver = driver

    def select_size_by_index(self, index):
        driver = self.driver
        SIZEDROPDOWN = driver.find_element(By.ID, SIZE_DROPDOWN)
        sizes_selector = Select(SIZEDROPDOWN)
        sizes_selector.select_by_index(index)

    def select_color_by_index(self,index):
        driver = self.driver
        ColorDropdown = driver.find_element(By.ID, color_dropdown)
        color_selector = Select(ColorDropdown)
        color_selector.select_by_index(index)

    def click_add_to_cart_button(self):
        self.driver.find_element(By.ID, Button_cart).click()