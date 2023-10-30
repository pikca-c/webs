from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Users/vinci/Documents/chromedriver-win64/chromedriver.exe")
driver.get("https://www.warwickschool.org/academic/results")
driver.find_element_by_css_selector(".cookie_information__close").click()

gcse = driver.find_element(By.CLASS_NAME, ".template.template--accordion")
strong = gcse.find_elements(By.TAG_NAME, ".strong")
  