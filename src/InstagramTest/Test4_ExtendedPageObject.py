import time

from selenium import webdriver
from src.InstagramTest.pages.Test4_InstLoginPage import LoginPage

validation_PassNotMatch_Error_Message = 'Sorry, your password was incorrect. Please double-check your password.'

driver = webdriver.Chrome('D:\_soft\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

loginPage = LoginPage(driver)
loginPage.enter_username("pyautomation")
loginPage.enter_password("Ab123456!")
loginPage.login()
time.sleep(1)

# main_page = MainPage(driver)
# main_page.click_not_now_button()
# main_page.type_in_search_field("fitness")
# main_page.click_result_with_text("#fitness")
# search_page = SearchResultPage(driver)
# time.sleep(5)
# assert "Follow" in search_page.get_follow_button_text

try:
      assert validation_PassNotMatch_Error_Message in driver.page_source
      print ("Password incorrect error")

except AssertionError:
      print ("Password Confirmation error")

driver.quit()

