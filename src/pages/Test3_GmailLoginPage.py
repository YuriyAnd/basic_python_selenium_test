import time

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def elementsCreate(self):
        lnk_CreateNew = self.driver.find_element_by_xpath("//span[text()='Створити обліковий запис']")
        lnk_CreateNew.click()



