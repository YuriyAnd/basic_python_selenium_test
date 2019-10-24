import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from src.Kiosk_Test.pages.base_page import BasePage

class KioskUserLoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Login form elements.
    # https://checkin.usaveinclinics.net/operator/login
    #         result = (By.XPATH, "//span[text()='{}']".format(text))


    # // Language
    # elements.
    btnContinueEn = (By.XPATH, "//span[contains(text(),'(EN)')]")
    btnContinueEs = (By.XPATH, "//span[contains(text(),'(ES)')]")
    btnContinueRu = (By.XPATH, "//span[contains(text(),'Continue (RU)')]")
    lblVisitReceprionist = (By.XPATH, "//h1[contains(text(),'This device is not configured yet. Please visit receptionist')]")
    lblVisitReceprionistEs = (By.XPATH, "//h1[contains(text(),'Por favor visita la recepcion')]")
    lblVisitReceprionistRu = (By.XPATH, "//h1[contains(text(),'Пожалуйста, свяжитесь с администратором')]")
    # Main section elements.
    inpLastName = (By.XPATH, "//input[@id='last-name']")
    inpDOB = (By.XPATH, "//input[@id='date-of-birth']")
    btnNext = (By.XPATH, "//span[contains(text(),'Next')]")
    btnNewUser = (By.XPATH, "//span[contains(text(),'New Patient')]")
    #Common
    btnBack = (By.XPATH, "//div[1]/button[1]/span[1]/*")
    btnSkip = (By.XPATH, "//span[contains(text(), 'Skip')]")

    # 2 Photo
    imgCurrentPhoto = (By.XPATH, "//div[1]/img[1]")
    btnUseThisPhoto = (By.XPATH, "//span[contains(text(),'Use this photo')]")
    btnReTakePhoto = (By.XPATH, "//span[contains(text(), 'Re-take photo')]")

    # 3 Contact Info
    # 4 Address
    # 5 Emergency Contact
    # 6 PCP
    # 7 Driver Licence
    # 8 Payment Type
    btnInsurance = (By.XPATH, "//  span[contains(text(), 'Insurance')]")
    btnSelfPay = (By.XPATH, "// span[contains(text(), 'Self pay')]")


    def userlogin(self):
        self.click_on(self.btnContinueEn)
        self.type_in(self.inpLastName, self.login_v)
        self.type_in(self.inpDOB, self.DOB_v)
        self.click_on(self.btnNext)
        self.click_on(self.btnUseThisPhoto)
        self.click_on(self.btnNext)
        self.click_on(self.btnNext)
        self.click_on(self.btnNext)
        self.click_on(self.btnNext)
        self.click_on(self.btnUseThisPhoto)
        self.click_on(self.btnInsurance)

        # self.type_in(self.page, " ")

        time.sleep(2)


        time.sleep(10)
        # self.click_on(self.btnIllinois)
        # self.click_on(self.btnNorthShore)
        # self.get_element(self.btnCameraOk)
        # self.click_on(self.btnCameraOk)