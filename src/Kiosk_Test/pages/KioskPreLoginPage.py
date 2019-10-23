import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from src.Kiosk_Test.pages.base_page import BasePage

class KioskPreLoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Login form elements.
    # https://checkin-stg.usaveinclinics.net/operator/login
    #         result = (By.XPATH, "//span[text()='{}']".format(text))
    login = "intetics"
    password = "Development-2017"
    FIELD_USERNAME = (By.NAME, "username")
    INPUT_LOGIN = By.ID('login')
    # inpLogin = (By.XPATH('//input[@id="login"]'))
    inpPassword = (By.XPATH("//input[@id='password']"))
    # btnLogin = (By.XPATH("//div[3]/button"))
    # errLogin = (By.XPATH("//p[@id='password-helper-text']"))
    # btnIllinois = (By.XPATH("//div[contains(text(),'Illinois')]"))  # Select state
    # btnNorthShore = (By.XPATH("//body//div[contains(text(),'North Sh') and not(contains(text(),'Mun'))]"))  # Select location
    # btnCameraOk = (By.XPATH("//*[contains(text(),'OK')]"))  #Camera test


    # basepage = new BasePage
    # BasePage.get_element(inpLogin).send_keys(login)
    # BasePage.type_in(inpPassword, password)
    # BasePage.click_on(btnLogin)


    def login(self):
        self.type_in(self.INPUT_LOGIN, self.login)
        self.type_in(self.inpPassword, self.password)
        self.click_on(self.btnLogin)
        # self.driver.get_element_by_xpath("//div[3]/button").click()
        # WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable).click()
