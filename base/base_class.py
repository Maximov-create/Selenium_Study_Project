from datetime import datetime


class Base:
    '''Универсальные методы'''

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        '''Method get current url'''
        get_url = self.driver.current_url
        print(f'CURRENT URL: {get_url}')

    def assert_word(self, word, expected_word):
        '''Method assert word'''
        value_word = word.text
        assert value_word == expected_word, f'VALUE ASSERTION FAIL = {value_word} | EXPECTED = {expected_word}'
        print(f'VALUE ASSERTION OK = {value_word}')

    def assert_url(self, expected_url):
        '''Method assert URL'''
        url_value = self.driver.current_url
        assert url_value == expected_url, f'URL ASSERTION FAIL = {url_value} | EXPECTED = {expected_url}'
        print(f'URL ASSERTION OK = {url_value}')

    def get_screenshot(self, screen_name='screenshot'):
        '''Method screenshot'''
        now_date = datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
        name_screenshot = f'screen {now_date} {screen_name} .png'
        self.driver.save_screenshot(f'./screens/{name_screenshot}')
        print(f'SCREENSHOT MADE {screen_name}')
