from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd 

driver = webdriver.Chrome("C:/Users/vinci/Documents/chromedriver-win64/chromedriver.exe")

driver.get('https://hoopshype.com/salaries/players/')