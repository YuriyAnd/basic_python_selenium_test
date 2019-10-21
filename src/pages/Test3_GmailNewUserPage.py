import time

class NewUserPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def create_New_Account(self):
        time.sleep(1)
        self.clickForMyself()

    def clickForMyself(self):
        btn_create_ForMyself = self.driver.find_element_by_xpath("//div[text()='Для себе']")
        btn_create_ForMyself.click()
        time.sleep(1)
    #
    # def userDataFill(self):
    #     btn_create_ForMyself = self.driver.find_element_by_xpath("//div[text()='Для себе']")
    #     btn_create_ForMyself.click()
    #     time.sleep(1)
