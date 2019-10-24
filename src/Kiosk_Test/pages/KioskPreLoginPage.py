import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from src.Kiosk_Test.pages.base_page import BasePage

class KioskPreLoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Login form elements.
    # https://checkin.usaveinclinics.net/operator/login
    #         result = (By.XPATH, "//span[text()='{}']".format(text))
    login_v = "intetics"
    password_v = "Development-2017"
    inpLogin = (By.ID, 'login')
    inpPassword = (By.XPATH, "//input[@id='password']")
    btnLogin = (By.XPATH, "//div[3]/button")
    # errLogin = (By.XPATH, "//p[@id='password-helper-text']")
    btnIllinois = (By.XPATH, "//div[contains(text(),'Illinois')]")  # Select state
    btnNorthShore = (By.XPATH, "//body//div[contains(text(),'North Sh') and not(contains(text(),'Mun'))]")  # Select location
    btnCameraOk = (By.XPATH, "//*[contains(text(),'OK')]")  #Camera test
    page = (By.TAG_NAME, "body")

    def prelogin(self):
        self.type_in(self.inpLogin, self.login_v)
        self.type_in(self.inpPassword, self.password_v)
        self.click_on(self.btnLogin)
        self.click_on(self.btnIllinois)
        self.click_on(self.btnNorthShore)
        self.get_element(self.btnCameraOk)
        self.click_on(self.btnCameraOk)
        self.alrt_close()