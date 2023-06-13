# Selenium

from selenium import webdriver
from selenium.webdriver.common.keys import keys

driver = webdriver.Firefox(executable_path="")
driver.get("https://www.google.com.br")
driver.find_element_by_name("q").send_keys("Reconhecimento Facial")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
