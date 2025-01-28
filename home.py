from selenium import webdriver
from selenium.webdriver.common.by import By

home_sections = 'collection-grid-item'

class TestHome:

    def __init__(self,driver):
        self.driver = driver

    def click_men_category(self):
        sections = self.driver.find_elements(By.CLASS_NAME, home_sections)
        sections[1].click()



