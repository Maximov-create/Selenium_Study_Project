from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from time import sleep


class TBookPage(Base):
    '''Страница Тестовой Книги (любой)'''

    # Locators
    reviews_number_text_button = '//span[@class="product-info-review-detail__text"]'
    offer_bonus_info_button = '//span[@class="product-offer-bonus__text"]'
    scroll_arrow_button = '//button[@class="scroll-button__arrow"]'
    buy_product_button = '//button[@class="product-offer-button chg-app-button chg-app-button--primary chg-app-button--extra-large chg-app-button--brand-blue chg-app-button--block"]'
    cart_num_badge = '//span[@class="badge-notice header-cart__badge"]'
    cart_icon = '//a[@href="/cart"]'
    product_header_title = '//h1[@class="detail-product__header-title"]'
    author_title = '//div[@class="product-info-authors detail-product__header-authors"]'
    publisher_title_upper = '(//a[@itemprop="publisher"])[2]'


    # Getters
    def get_reviews_number_text_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reviews_number_text_button)))

    def get_offer_bonus_info_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.offer_bonus_info_button)))

    def get_scroll_arrow_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.scroll_arrow_button)))

    def get_buy_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_button)))

    def get_cart_num_badge(self):
        return self.driver.find_element(By.XPATH, self.cart_num_badge)

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_icon)))

    def get_product_header_title(self):
        return self.driver.find_element(By.XPATH, self.product_header_title)

    def get_author_title(self):
        return self.driver.find_element(By.XPATH, self.author_title)

    def get_publisher_title_upper(self):
        return self.driver.find_element(By.XPATH, self.publisher_title_upper)


    # Actions
    def click_reviews_number_text_button(self):
        self.get_reviews_number_text_button().click()
        print('Clicked Reviews number text Button')

    def click_offer_bonus_info_button(self):
        self.get_offer_bonus_info_button().click()
        print('Clicked Offer bonus info Button')

    def click_scroll_arrow_button(self):
        self.get_scroll_arrow_button().click()
        print('Clicked Scroll arrow button Button')

    def click_buy_product_button(self):
        self.get_buy_product_button().click()
        print('Clicked Buy product Button')

    def click_buy_product_button(self):
        self.get_buy_product_button().click()
        print('Clicked Buy product Button')

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print('Clicked Cart Icon')

    def show_product_header_title(self):  # Метод для вывода названия книги в заголовке с возрастным рейтингом
        product_header_title = self.get_product_header_title().text.replace('\n', ' ')
        print(product_header_title)

    def show_author_title(self):  # Метод для вывода автора(ов)
        author_title = self.get_author_title().text
        print(author_title)

    def show_publisher_title_upper(self):  # Метод для вывода из верхней карточки издателя
        publisher_title = self.get_publisher_title_upper().text
        print(publisher_title)


    # Methods
    def method_complex_buy_product(self):
        self.get_current_url()
        self.show_product_header_title()
        self.show_author_title()
        self.show_publisher_title_upper()
        self.click_reviews_number_text_button()
        sleep(3)
        self.click_offer_bonus_info_button()
        sleep(3)
        self.get_screenshot('Info Bonus')
        sleep(3)
        self.click_scroll_arrow_button()
        sleep(3)
        self.click_buy_product_button()
        sleep(3)
        self.assert_word(self.get_cart_num_badge(), '1')  # Проверка, что возле иконки корзины появилась цифра 1
