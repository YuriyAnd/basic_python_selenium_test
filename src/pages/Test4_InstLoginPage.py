import time
from selenium.webdriver.common.by import By
from src.pages.Test4_InstMainPage import BasePage


class LoginPage(BasePage):
    FIELD_USERNAME = (By.NAME, "username")
    FIELD_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
    def enter_username(self, username):
        self.type_in(self.FIELD_USERNAME, username)
    def enter_password(self, password):
        self.type_in(self.FIELD_PASSWORD, password)
    def login(self):
        self.click_on(self.BUTTON_LOGIN)