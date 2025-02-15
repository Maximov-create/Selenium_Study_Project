import pytest
from base.helpful import clear_screens_directory


@pytest.fixture(scope='session')
def set_up_clear():
    clear_screens_directory()  # Для очистки директории со скриншотами перед запуском тестов
    print('TEST START')
    yield
    print('TEST FINISH')
