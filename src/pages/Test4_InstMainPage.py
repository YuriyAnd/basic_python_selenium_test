import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage():
    def __init__(self, driver):
        self.driver = driver


class SearchResultPage():
    def __init__(self, driver):
        self.driver = driver


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(expected_condition, message="Unable to locate element")

    def click_on(self, locator):
        self.get_element(locator).click()

    def type_in(self, locator, text):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.get_element(locator).text

    def click_not_now_button(self):
        self.click_on(self.BUTTON_NOT_NOW)

    def type_in_search_field(self, text):
        self.type_in(self.FIELD_SEARCH, text)

    def click_result_with_text(self, text):
        result = (By.XPATH, "//span[text()='{}']".format(text))
        self.click_on(result)