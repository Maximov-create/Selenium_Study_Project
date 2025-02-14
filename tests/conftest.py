import pytest
from base.helpful import clear_screens_directory


@pytest.fixture(scope='session')
def set_up_clear():
    print('TEST START')
    clear_screens_directory() # Для очистки директории со скриншотами перед запуском тестов
    yield
    print('TEST FINISH')
