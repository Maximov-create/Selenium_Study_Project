from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from time import sleep
from utilities.logger import Logger
import allure


class MainPage(Base):
    '''Главная страница'''

    # Locators
    city_header_button = '//button[@class="header-city header-top-bar__city"]'
    change_city_button = '//div[@class="button change-city__button change-city__button--cancel light-blue"]'
    select_country_dropdown_menu = '//div[@class="app-select city-modal__select"]'
    Belarus_list_button = '//li[contains(@class, "app-select__list-item") and contains(.//span, "Беларусь")]'
    city_input_field = '//input[@class="city-modal__city-input"]'
    list_city_choice = '//li[contains(@class, "cities-list__item") and contains(text(), "д. Ермаки, Район Пинский, обл. Брестская")]'
    sales_link_button = '//a[contains(@class, "header-bottom__link") and contains(text(), "Распродажа")]'


    # Getters
    def get_city_header_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_header_button)))

    def get_change_city_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.change_city_button)))

    def get_select_country_dropdown_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_country_dropdown_menu)))

    def get_Belarus_list_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.Belarus_list_button)))

    def get_city_input_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_input_field)))

    def get_list_city_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.list_city_choice)))

    def get_sales_link_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sales_link_button)))


    # Actions
    def click_city_header_button(self):
        self.get_city_header_button().click()
        print('Clicked City header Button')

    def click_change_city_button(self):
        self.get_change_city_button().click()
        print('Clicked Change city Button')

    def click_select_country_dropdown_menu(self):
        self.get_select_country_dropdown_menu().click()
        print('Clicked Select country dropdown menu Button')

    def click_Belarus_list_button(self):
        self.get_Belarus_list_button().click()
        print('Clicked Belarus list Button')

    def click_city_input_field(self):
        self.get_city_input_field().click()
        print('Clicked (Activated) city name Field')

    def input_city_input_field(self, city_name):
        self.get_city_input_field().send_keys(city_name)
        print(f'Inputted {city_name} in City input Field')

    def click_list_city_2(self):
        self.get_list_city_2().click()
        print('Clicked list city 2')

    def click_sales_link_button(self):
        self.get_sales_link_button().click()
        print('Clicked Sales link Button')


    # Methods
    def method_choose_city(self):
        with allure.step('method_choose_city'):
            Logger.add_start_step(method='method_choose_city')
            self.get_current_url()
            self.assert_url('https://www.chitai-gorod.ru/')
            self.click_city_header_button()
            self.click_change_city_button()
            self.click_select_country_dropdown_menu()
            self.click_Belarus_list_button()
            self.click_city_input_field()
            self.input_city_input_field(city_name='Пинск')
            self.click_list_city_2()
            sleep(5)
            self.get_screenshot('City Changed')
            Logger.add_end_step(url=self.driver.current_url, method='method_choose_city')
