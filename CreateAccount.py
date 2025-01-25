#aqui voy a agregar mis locators
import data
from selenium import webdriver
from selenium.webdriver.common.by import By


#lOCATORS
INPUT_FIRST_NAME_ID = 'FirstName'
INPUT_LAST_NAME_ID = 'LastName'
INPUT_EMAIL_ID= 'Email'
INPUT_PASSWORD_ID = 'CreatePassword'
INPUT_CREATE_BUTTON_XPATH = '//*[@value="Create"]'

class CreateAccount: #nos da las acciones que vamos a hacer en la pagina de registro

    def __init__(self):
        self.driver = webdriver.Chrome()

    def fill_first_name(self):
        self.driver.find_element(By.ID, INPUT_FIRST_NAME_ID).send_keys(data.valid_user['first_name'])

    def fill_last_name(self):
        self.driver.find_element(By.ID, INPUT_LAST_NAME_ID).send_keys(data.valid_user['last_name'])

    def fill_email(self):
        self.driver.find_element(By.ID, INPUT_EMAIL_ID).send_keys(data.valid_user['email'])

    def fill_password(self):
        self.driver.find_element(By.ID, INPUT_PASSWORD_ID).send_keys(data.valid_user['password'])

    def click_create_button(self):
        self.driver.find_element(By.XPATH, INPUT_CREATE_BUTTON_XPATH).click()


