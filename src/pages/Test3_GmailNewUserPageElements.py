import time

class NewUserPageElements():
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def userDataElements(self):
        fldFirstName = self.driver.find_element_by_id("firstName")
        fldLastName = self.driver.find_element_by_id("lastName")
        fldEmail = self.driver.find_element_by_id("username")
        fldPass = self.driver.find_element_by_name("Passwd")
        fldConfirmPassword = self.driver.find_element_by_name("ConfirmPasswd")
        btnProceed = self.driver.find_element_by_xpath("//div//span[text()='Далі']")

        fldFirstName.send_keys("FN_Test1")
        fldLastName.send_keys("LN_Test1")
        fldEmail.send_keys("Email_Test1")
        fldPass.send_keys("Pass1")
        fldConfirmPassword.send_keys("pass2")
        btnProceed.click()
        time.sleep(1)
