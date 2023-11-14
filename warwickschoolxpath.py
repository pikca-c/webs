from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
driver = webdriver.Chrome("C:/Users/vinci/Documents/chromedriver-win64/chromedriver.exe",chrome_options=chrome_options)

driver.get("https://www.warwickschool.org/academic/results")
driver.implicitly_wait(10)
allow_cookies = driver.find_element(By.CLASS_NAME, "cookie_information__button ")
allow_cookies.click()

results = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/p[5]")
print (results.text)