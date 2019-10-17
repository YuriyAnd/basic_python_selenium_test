from selenium import webdriver
driver = webdriver.Chrome("C:/Users/y.andrus/Desktop/chromedriver_win32/chromedriver.exe")
driver.get("http://wikipedia.org/")

search_field = driver.find_element_by_id("searchInput")
search_button = driver.find_element_by_xpath("//button[@class='pure-button pure-button-primary-progressive']")

search_field.send_keys("Test Automation")
search_button.click()
#from selenium.webdriver.common.keys import Keys
assert "Test automation - Wikipedia" in driver.title
driver.quit()