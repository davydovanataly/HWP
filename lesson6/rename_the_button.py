from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

driver.find_element(By.CSS_SELECTOR, "input").clear()
driver.find_element(By.CSS_SELECTOR, "input").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)

driver.quit()
