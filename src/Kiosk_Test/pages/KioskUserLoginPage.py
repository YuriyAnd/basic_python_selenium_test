import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from src.Kiosk_Test.pages.base_page import BasePage


class KioskUserLoginPage():
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

class SearchResultPage():
    def __init__(self, driver):
        self.driver = driver