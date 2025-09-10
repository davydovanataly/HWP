import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from lesson10.shop_pages.ShopMainPage import ShopMainPage
from lesson10.shop_pages.ShopBuyPage import ShopBuyPage
from lesson10.shop_pages.PersInfoPage import PersInfoPage
from lesson10.shop_pages.ShopTotalCost import ShopTotalCost


@allure.feature("Проверка общей стоимости заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест проверки итоговой стоимости товаров")
@allure.description(
    "Проверка корректного расчета общей стоимости выбранных товаров")
def test_shop_total_price():
    with allure.step("Открытие сайта и авторизация"):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        main_page = ShopMainPage(driver)
        main_page.auth_user()
    with allure.step("Добавление товаров в корзину"):
        buy_page = ShopBuyPage(driver)
        buy_page.add_to_cart()
    with allure.step("Переход к оформлению заказа"):
        pers_info = PersInfoPage(driver)
        pers_info.pers_info()
    with allure.step("Проверка итоговой стоимости"):
        total_cost = ShopTotalCost(driver)
        total_cost.total_cost()
