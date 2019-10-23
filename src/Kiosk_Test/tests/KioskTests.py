import time
from selenium import webdriver
from src.Kiosk_Test.pages.KioskPreLoginPage import KioskPreLoginPage
from src.Kiosk_Test.pages.KioskUserLoginPage import KioskUserLoginPage
from src.Kiosk_Test.pages.KioskUserStartPage import KioskUserStartPage


# I am on main page
# I type "#fitness" in "search" field
# I click on "#fitness"
# I am on search result page I see "Follow" button

validation_PassNotMatch_Error_Message = 'Sorry, your password was incorrect. Please double-check your password.'

driver = webdriver.Chrome('D:\_soft\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

preloginPage = KioskPreLoginPage(driver)
preloginPage.login()
time.sleep(1)

# main_page = KioskUserLoginPage(driver)
# main_page.click_not_now_button()
# main_page.type_in_search_field("fitness")
# main_page.click_result_with_text("#fitness")
# time.sleep(1)
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
      print ("Password Confirmation error")

driver.quit()

