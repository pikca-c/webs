from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
driver = webdriver.Chrome("C:/Users/vinci/Documents/chromedriver-win64/chromedriver.exe",chrome_options=chrome_options)

driver.get("https://www.warwickschool.org/academic/results")
driver.implicitly_wait(10)
allow_cookies = driver.find_element(By.CLASS_NAME, "cookie_information__button ")
allow_cookies.click()

gcse = driver.find_element(By.CLASS_NAME, "content__region")
print (gcse.text)


  
