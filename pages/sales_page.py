from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from base.base_class import Base
from time import sleep
from utilities.logger import Logger
import allure


class SalesPage(Base):
    '''Страница Распродажи'''

    # Locators
    minimal_sort_open_button = '//div[@class="minimal-sort__button"]'
    minimal_sort_by_popularity = '//div[contains(@class, "minimal-sort__item") and contains(text(), "По популярности")]'
    rosmen_filter_checkbox = '//span[contains(@class, "multiple-select-options__item-text") and contains(text(), "РОСМЭН")]'
    exmo_filter_checkbox = '//span[contains(@class, "multiple-select-options__item-text") and contains(text(), "Эксмо")]'
    author_filter_field = '//input[@placeholder="Найти больше авторов"]'
    author_Alexander_Pushkin_search_li = '//li[contains(@class, "app-input__item") and contains(text(), "Александр Сергеевич Пушкин")]'
    hardcover_checkbox = '//span[contains(@class, "multiple-select-options__item-text") and contains(text(), "Твёрдый переплёт")]'
    year_slider_left = '//div[@class="vue-slider-dot-handle"]'
    year_range_input_right = '(//input[@class="app-range-input__input"])[2]'
    test_book_first_any = '//a[@class="product-card__picture product-card__row"][1]'
    sales_header_title = '//h1[@class="app-catalog-page__title"]'
    # Локаторы должны быть привязаны, индексы могут сместиться и тогда все ляжет

    # Getters
    def get_minimal_sort_open_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minimal_sort_open_button)))

    def get_minimal_sort_by_popularity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minimal_sort_by_popularity)))

    def get_rosmen_filter_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rosmen_filter_checkbox)))

    def get_exmo_filter_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exmo_filter_checkbox)))

    def get_author_filter_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.author_filter_field)))

    def get_author_Alexander_Pushkin_search_li(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.author_Alexander_Pushkin_search_li)))

    def get_hardcover_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hardcover_checkbox)))

    def get_year_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_slider_left)))

    def get_year_range_input_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.year_range_input_right)))

    def get_test_book_first_any(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test_book_first_any)))

    def get_sales_header_title(self):
        return self.driver.find_element(By.XPATH, self.sales_header_title)


    # Actions
    def click_minimal_sort_open_button(self):
        self.get_minimal_sort_open_button().click()
        print('Clicked Minimal sort Button')

    def click_minimal_sort_by_popularity(self):
        self.get_minimal_sort_by_popularity().click()
        print('Clicked Minimal sort by popularity')

    def click_rosmen_filter_checkbox(self):
        self.get_rosmen_filter_checkbox().click()
        print('Clicked РОСМЭН filter Checkbox')

    def click_exmo_filter_checkbox(self):
        self.get_exmo_filter_checkbox().click()
        print('Clicked Эксмо filter Checkbox')

    def click_author_filter_field(self):
        self.get_author_filter_field().click()
        print('Clicked (Activated) Author filter Field')

    def input_author_filter_field(self, author_name):
        self.get_author_filter_field().send_keys(author_name)
        print(f'Inputted {author_name} in Author filter Field')

    def click_author_Alexander_Pushkin_search_li(self):
        self.get_author_Alexander_Pushkin_search_li().click()
        print('Clicked author Александр Сергеевич Пушкин in search List')

    def click_hardcover_checkbox(self):
        self.get_hardcover_checkbox().click()
        print('Clicked Hardcover Checkbox')

    def move_year_slider_left(self, x, y):
        ActionChains(self.driver).click_and_hold(self.get_year_slider_left()).move_by_offset(x, y).release().perform()
        print('Moved year slider left')

    def click_year_range_input_right(self):
        self.get_year_range_input_right().click()
        print('Clicked year range input right')

    def input_year_range_input_right(self, year_num):
        self.get_year_range_input_right().send_keys(Keys.CONTROL + 'a')  # Очистка поля перед вставкой значения
        self.get_year_range_input_right().send_keys(Keys.DELETE)
        self.get_year_range_input_right().send_keys(year_num)
        self.get_year_range_input_right().send_keys(Keys.ENTER)
        print('Inputted year range input right')

    def click_test_book_first_any(self):
        self.get_test_book_first_any().click()
        print('Clicked test book')


    # Methods
    def method_complex_filters(self):
        with allure.step('method_complex_filters'):
            Logger.add_start_step(method='method_complex_filters')
            self.get_current_url()
            self.assert_url('https://www.chitai-gorod.ru/sales')
            self.assert_word(self.get_sales_header_title(), 'РАСПРОДАЖА')  # Сверяем заголовок
            self.click_minimal_sort_open_button()
            self.click_minimal_sort_by_popularity()
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 1100);")
            sleep(3)
            self.click_rosmen_filter_checkbox()
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 750);")
            sleep(3)
            self.click_exmo_filter_checkbox()
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 1200);")
            sleep(3)
            self.click_author_filter_field()
            self.input_author_filter_field('Александ Серг Пушк')  # Значение специально неполное
            self.click_author_Alexander_Pushkin_search_li()
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 1600);")
            sleep(3)
            self.click_hardcover_checkbox()
            sleep(5)
            self.driver.execute_script("window.scrollTo(0, 1700);")
            sleep(3)
            self.move_year_slider_left(120, 0)
            sleep(3)
            self.driver.execute_script("window.scrollTo(0, 1700);")
            sleep(3)
            self.click_year_range_input_right()
            sleep(3)
            self.input_year_range_input_right('2022')
            sleep(3)
            self.driver.execute_script("window.scrollTo(0, 200);")
            sleep(3)
            self.get_screenshot('Filters')
            Logger.add_end_step(url=self.driver.current_url, method='method_complex_filters')
