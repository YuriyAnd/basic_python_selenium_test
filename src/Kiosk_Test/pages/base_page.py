import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(expected_condition, message="Unable to locate element")

    def non_exist_element(self, locator):
        expected_condition = not ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(expected_condition, message="'Error message' is exist")

    def get_clickable_element(self, locator):
        expected_condition = ec.element_to_be_clickable(locator)
        return WebDriverWait(self.driver, 10).until(expected_condition, message="Unable to locate clickable element")

    def click_on(self, locator):
        self.get_clickable_element(locator).click()

    def type_in(self, locator, text):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.get_element(locator).text

    def alrt_close(self):
        try:
            WebDriverWait(self, 1).until(ec.alert_is_present(),
                                         'Timed out waiting for Alert creation ' +
                                         'confirmation popup to appear.')
            self.switch_to.alert.accept()
        except:
            print("Alert Not Found.")
