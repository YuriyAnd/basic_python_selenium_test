import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.Kiosk_Test.pages.KioskPreLoginPage import KioskPreLoginPage
from src.Kiosk_Test.pages.KioskUserLoginPage import KioskUserLoginPage
from src.Kiosk_Test.pages.KioskUserStartPage import KioskUserStartPage


# I am on main page
# I type "#fitness" in "search" field
# I click on "#fitness"
# I am on search result page I see "Follow" button

validation_PassNotMatch_Error_Message = 'Sorry, your password was incorrect. Please double-check your password.'

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument('--start-maximized')
driverpath = 'D:\_soft\chromedriver.exe'

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path = driverpath, options = chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://checkin-stg.usaveinclinics.net/operator/login")

preloginPage = KioskPreLoginPage(driver)
preloginPage.prelogin()
time.sleep(1)

kiosk_user_login_page = KioskUserLoginPage(driver)
kiosk_user_login_page.userlogin()
time.sleep(1)
#
# main_page = KioskUserStartPage(driver)
# main_page.click_not_now_button()
# main_page.type_in_search_field("fitness")
# main_page.click_result_with_text("#fitness")
# time.sleep(1)

try:
      assert validation_PassNotMatch_Error_Message in driver.page_source
      print ("Password incorrect error")
except AssertionError:
      print ("Password error is not displayed")

driver.quit()

