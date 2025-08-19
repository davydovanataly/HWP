from selenium.webdriver.common.by import By


class ShopTotalCost:

    def __init__(self, driver):
        self._driver = driver

# 4 прочитать итоговую стоимость
    def total_cost(self):
        total_text = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        assert total_text == "Total: $58.29", f"$58.29, получено: {total_text}"
        self._driver.quit()