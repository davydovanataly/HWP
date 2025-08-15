from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.NAME, "first-name").send_keys("Иван")
last_name = driver.find_element(By.NAME, "last-name").send_keys("Петров")
address = driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
zip_code = driver.find_element(By.NAME, "zip-code").send_keys()
city = driver.find_element(By.NAME, "city").send_keys("Москва")
country = driver.find_element(By.NAME, "country").send_keys("Россия")
e_mail = driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
phone = driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
job_position = driver.find_element(By.NAME, "job-position").send_keys("QA")
company = driver.find_element(By.NAME, "company").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button").click()


def test_form_colors():
    zip_code_div = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_div.get_attribute("class")


assert "alert-success" in driver.find_element(By.ID,
                                              "first-name").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "last-name").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "address").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "city").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "country").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "e-mail").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "phone").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "job-position").get_attribute
("class")
assert "alert-success" in driver.find_element(By.ID,
                                              "company").get_attribute
("class")


driver.quit()
# Я не понимаю почему питест выдает тут ошибку,
# ему не нравится метод "get attribute"
