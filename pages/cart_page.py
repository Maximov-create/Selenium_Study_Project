from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from time import sleep


class CartPage(Base):
    '''Страница Корзины'''

    # Locators
    promocode_field = '//input[@placeholder="Введите промокод"]'
    promocode_submit_button = '//button[@class="button promo-code__button blue"]'
    promocode_message_error = '//div[@class="promo-code__message error"]'
    clear_promocode_button = '//button[@class="button promo-code__clear-button light-blue"]'
    order_gift_checkbox = '(//span[@class="chg-app-checkbox__control"])[1]'
    order_gift_box_checkbox = '(//span[@class="chg-app-checkbox__control"])[2]'
    gift_box_spoiler = '//div[@class="app-spoiler__title"]'
    find_out_more_button = '//button[@class="cart-sidebar-gift__popup-btn"]'
    gift_order_info_header = '//h1[@class="app-title app-title--mounted modal__title app-title--header-4"]'
    gift_order_info_close_button = '//button[@aria-label="Закрыть"]'
    title_product_quantity = '//span[@class="app-title__append"]'
    info_item_quantity = '(//div[@class="info-item__title"])[1]'
    info_item_price = '(//div[@class="info-item__value"])[1]'
    info_item_discount_gift_on = '(//div[@class="info-item__value"])[3]'
    info_final_price_gift_on = '(//div[@class="info-item__value"])[4]'
    product_old_price = '(//div[@class="product-price__old"])[1]'
    product_new_price = '(//div[@class="product-price__value product-price__value--discount"])[1]'
    gift_option_price = '//span[@class="cart-sidebar-gift__option-price"]'
    order_button = '//button[@class="button cart-sidebar__order-button blue"]'
    agreement_personal_note = '//a[@href="/about/agreement/personal"]'
    data_policy_note = '(//a[@href="/about/policy"])[2]'
    # Локаторы ниже относятся к другим страницам, однако с целью удобства они тут
    agreement_page_title = '//h1[@class="global-title"]'
    data_policy_title = '//h1[@class="global-title"]'


    # Getters
    def get_promocode_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.promocode_field)))

    def get_promocode_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.promocode_submit_button)))

    def get_promocode_message_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.promocode_message_error)))

    def get_clear_promocode_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_promocode_button)))

    def get_order_gift_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_gift_checkbox)))

    def get_order_gift_box_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_gift_box_checkbox)))

    def get_gift_box_spoiler(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gift_box_spoiler)))

    def get_find_out_more_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.find_out_more_button)))

    def get_gift_order_info_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gift_order_info_header)))

    def get_gift_order_info_close_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gift_order_info_close_button)))

    def get_title_product_quantity(self):
        return self.driver.find_element(By.XPATH, self.title_product_quantity)

    def get_info_item_quantity(self):
        return self.driver.find_element(By.XPATH, self.info_item_quantity)

    def get_info_item_price(self):
        return self.driver.find_element(By.XPATH, self.info_item_price)

    def get_product_old_price(self):
        return self.driver.find_element(By.XPATH, self.product_old_price)

    def get_product_new_price(self):
        return self.driver.find_element(By.XPATH, self.product_new_price)

    def get_item_discount_gift_on(self):
        return self.driver.find_element(By.XPATH, self.info_item_discount_gift_on)

    def get_info_final_price_gift_on(self):
        return self.driver.find_element(By.XPATH, self.info_final_price_gift_on)

    def get_gift_option_price(self):
        return self.driver.find_element(By.XPATH, self.gift_option_price)

    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    def get_agreement_personal_note(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.agreement_personal_note)))

    def get_data_policy_note(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.data_policy_note)))

    def get_agreement_page_title(self):
        return self.driver.find_element(By.XPATH, self.agreement_page_title)

    def get_data_policy_title(self):
        return self.driver.find_element(By.XPATH, self.data_policy_title)


    # Actions
    def click_promocode_field(self):
        self.get_promocode_field().click()
        print('Clicked (Activated) Promocode Field')

    def input_promocode_field(self, code):
        self.get_promocode_field().send_keys(code)
        print(f'Inputted {code} in Promocode Field')

    def click_promocode_submit_button(self):
        self.get_promocode_submit_button().click()
        print('Clicked Promocode submit Button')

    def click_clear_promocode_button(self):
        self.get_clear_promocode_button().click()
        print('Clicked Clear promocode Button')

    def click_order_gift_checkbox(self):
        self.get_order_gift_checkbox().click()
        print('Clicked Order gift Checkbox')

    def click_order_gift_box_checkbox(self):
        self.get_order_gift_box_checkbox().click()
        print('Clicked Order gift box Checkbox')

    def click_gift_box_spoiler(self):
        self.get_gift_box_spoiler().click()
        print('Clicked Gift box Spoiler')

    def click_find_out_more_button(self):
        self.get_find_out_more_button().click()
        print('Clicked Find out more Button')

    def click_gift_order_info_close_button(self):
        self.get_gift_order_info_close_button().click()
        print('Clicked Gift order info close Button')

    def click_order_button(self):
        self.get_order_button().click()
        print('Clicked Order Button')

    def click_agreement_personal_note(self):
        self.get_agreement_personal_note().click()
        print('Clicked Agreement personal Note')

    def click_data_policy_note(self):
        self.get_data_policy_note().click()
        print('Clicked Data policy Note')


    # Methods
    def method_complex_cart_check(self):
        self.get_current_url()
        self.assert_url('https://www.chitai-gorod.ru/cart')
        self.click_promocode_field()
        self.input_promocode_field('1234')
        self.click_promocode_submit_button()
        sleep(3)
        self.assert_word(self.get_promocode_message_error(), 'Промокода не существует')
        self.click_clear_promocode_button()
        sleep(3)
        self.click_order_gift_checkbox()
        sleep(3)
        self.click_order_gift_box_checkbox()
        sleep(3)
        self.click_gift_box_spoiler()
        self.driver.execute_script("window.scrollTo(0, 450);")
        sleep(3)
        self.get_screenshot('Gift Picture')
        self.click_find_out_more_button()
        sleep(3)
        self.assert_word(self.get_gift_order_info_header(), 'Оформление и доставка заказов в подарок')
        self.get_screenshot('Ordering Info')
        sleep(3)
        self.click_gift_order_info_close_button()
        sleep(3)
        self.driver.execute_script("window.scrollTo(0, 650);")

        # Проверка отображения корректного кол-ва товара
        self.assert_word(self.get_title_product_quantity(), '1 товар')
        self.assert_word(self.get_info_item_quantity(), '1 товар')

        # Проверка, что отображаемая цена без скидки равна отображаемой прежней цене товара
        product_price_without_discount = self.get_info_item_price().text
        product_old_price = self.get_product_old_price().text
        assert product_price_without_discount == product_old_price, "Item price and old price DON'T match ERROR"
        print("Item price and old price MATCH OK")

        # Вычисление скидки путем вычисление новой цены из старой
        old_price = int(self.get_product_old_price().text.replace(' ', '').replace('₽', ''))
        new_price = int(self.get_product_new_price().text.split()[0])
        discount_num = str(old_price - new_price)

        # Проверка корректного отображения скидки с полученным выше значением
        info_discount = self.get_item_discount_gift_on().text.replace(' ', '').replace('-', '').replace('₽', '')
        assert discount_num == info_discount, "Discount number DOESN'T match ERROR"
        print('Discount number MATCH OK')

        # Проверка на отображение корректной цены. Складывается новая цена с ценой подарочной упаковки
        gift_option_price = int(self.get_gift_option_price().text.replace(' ', '').replace('₽', ''))
        final_price = int(self.get_info_final_price_gift_on().text.replace(' ', '').replace('₽', ''))
        assert new_price + gift_option_price == final_price, 'Final price ERROR'
        print('Final price MATCH OK')

        self.click_order_button()
        sleep(3)
        self.click_agreement_personal_note()
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(5)
        self.assert_word(self.get_agreement_page_title(), 'СОГЛАСИЕ НА ОБРАБОТКУ ПЕРСОНАЛЬНЫХ ДАННЫХ')
        self.get_screenshot('Agreement Info Page')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        sleep(3)
        self.click_data_policy_note()
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(5)
        self.assert_word(self.get_data_policy_title(), 'ПОЛИТИКА В ОТНОШЕНИИ ОБРАБОТКИ ПЕРСОНАЛЬНЫХ ДАННЫХ')
        self.get_screenshot('Policy Info Page')
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(3)
        self.get_screenshot('Final Picture')

