import pytest
from selenium import webdriver
import config

@pytest.fixture(scope="function") # фикстура, чтобы драйвер запускался отдельно на каждый тест
def driver():
    driver = webdriver.Firefox() # запускает тесты в браузере Firefox
    driver.get(config.SCOOTER_URL) # Открытие главной страницы "Самоката"
    yield driver     # Передача объекта WebDriver в тест
    driver.quit()     # Закрытие браузера после теста
