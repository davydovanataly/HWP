from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("Наташа")
driver.find_element(By.ID, "last-name").send_keys("Давыдова")
driver.find_element(By.ID, "postal-code").send_keys("129543")
driver.find_element(By.ID, "continue").click()

total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text

assert total_text == "Total: $58.29", f"$58.29, получено: {total_text}"

driver.quit()
