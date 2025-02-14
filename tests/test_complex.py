import pytest
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.sales_page import SalesPage
from pages.t_book_page import TBookPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from base.helpful import clear_screens_directory


def test_complex_case_1(set_up_clear):
    driver = webdriver.Chrome()

    driver.get('https://www.chitai-gorod.ru')
    driver.maximize_window()

    mp = MainPage(driver)
    mp.method_choose_city()
    mp.click_sales_link_button()
    print()
    sleep(5)

    sp = SalesPage(driver)
    sp.method_complex_filters()
    sp.click_test_book_first_any()
    print()
    sleep(5)

    tbp = TBookPage(driver)
    tbp.method_complex_buy_product()
    tbp.click_cart_icon()
    print()
    sleep(5)

    cp = CartPage(driver)
    cp.method_complex_cart_check()

    driver.quit()
