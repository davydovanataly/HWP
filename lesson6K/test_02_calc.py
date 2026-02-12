from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_slow_calculator():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))
    driver.get
    ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.ID, "delay").clear()
    driver.find_element(By.ID, "delay").send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text

    assert result == "15", f"Ожидалось '15', получено: '{result}'"

    driver.quit()
