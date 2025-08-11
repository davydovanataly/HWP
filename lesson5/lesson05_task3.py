from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/inputs")


driver.find_element(By.TAG_NAME, "input").clear
driver.find_element(By.TAG_NAME, "input").send_keys("Pro")
time.sleep(5)

driver.quit()
