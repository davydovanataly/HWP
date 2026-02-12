from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.calculatot_main_page import CalculatorMainPage


def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = CalculatorMainPage(driver)
    main_page.input_wait()
    main_page.input_example()
    main_page.close_browser()

# pytest calculator_method_test.py
