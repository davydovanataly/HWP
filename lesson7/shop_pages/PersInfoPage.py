from selenium.webdriver.common.by import By


class PersInfoPage:

    def __init__(self, driver):
        self._driver = driver

    def pers_info(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Наташа")
        self._driver.find_element(By.ID, "last-name").send_keys("Давыдова")
        self._driver.find_element(By.ID, "postal-code").send_keys("129543")
        self._driver.find_element(By.ID, "continue").click()
