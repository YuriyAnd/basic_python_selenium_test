from selenium import webdriver
import time
from src.pages.Test3_GmailLoginPage import LoginPage
from src.pages.Test3_GmailNewUserPage import NewUserPage
from src.pages.Test3_GmailNewUserPageElements import NewUserPageElements

validation_Size_Error_Message = 'Пароль має містити щонайменше 8 символів'
validation_PassNotMatch_Error_Message = 'Паролі не збігаються. Повторіть спробу.'

driver = webdriver.Chrome('D:\_soft\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("https://accounts.google.com")

loginPage = LoginPage(driver)
loginPage.elementsCreate()

newUser = NewUserPage(driver)
newUser.create_New_Account()

NewUserPageEls = NewUserPageElements(driver)
NewUserPageEls.userDataElements()

# try:
#     assert validation_Size_Error_Message in driver.page_source
#     print ("Password size error")
# except AssertionError:
#     assert validation_PassNotMatch_Error_Message in driver.page_source
#     print ("Password Confirmation error")
#     # except AssertionError:
#     # print('Not cathced!')
driver.quit()

