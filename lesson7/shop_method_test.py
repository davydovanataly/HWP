from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from lesson7.shop_pages.ShopMainPage import ShopMainPage
from lesson7.shop_pages.ShopBuyPage import ShopBuyPage
from lesson7.shop_pages.PersInfoPage import PersInfoPage
from lesson7.shop_pages.ShopTotalCost import ShopTotalCost


def test_shop_total_price():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = ShopMainPage(driver)
    buy_page = ShopBuyPage(driver)
    pers_info = PersInfoPage(driver)
    total_cost = ShopTotalCost(driver)
    main_page.auth_user()
    buy_page.add_to_cart()
    pers_info.pers_info()
    total_cost.total_cost()
# pytest shop_method_test.py
