import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import YANDEX_DZEN_URL, SCOOTER_URL
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

@allure.title("Проверка редиректа на Яндекс по клику на логотип")
@allure.description("Проверяет, что при клике на логотип Яндекса происходит переход на страницу Яндекс.Дзен")
def test_yandex_logo_redirect(driver): # тест редиректа при клике на логотип Яндекса
    with allure.step("Инициализация главной страницы"):
        main_page = MainPage(driver)
    with allure.step("Клик на логотип Яндекса"):
        main_page.click_yandex_logo()
    with allure.step("Переключение на новое окно"):
        main_page.switch_to_new_window()
    with allure.step("Проверка URL после редиректа"):
        WebDriverWait(driver, 15).until(
            EC.url_contains('dzen.ru'),
            message=f"Редирект на Дзен не случился. Текущий URL: {driver.current_url}"
        )
    with allure.step("Закрытие текущего окна"):
        main_page.close_current_window()

@allure.title("Проверка редиректа на главную страницу Самоката по клику на логотип")
@allure.description("Проверяет, что при клике на логотип Самоката на странице заказа происходит переход на главную страницу Самоката")
def test_scooter_logo_redirect(driver): # редирект через логотип Самоката на главную страницу Самоката
    with allure.step("Инициализация главной страницы"):
        main_page = MainPage(driver)
    with allure.step("Открытие страницы заказа"):
        driver.get(SCOOTER_URL + "/order") # открываю страницу заказа
    with allure.step("Явное ожидание загрузки логотипа"):
        # явное ожидание загрузки логотипа
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO),
            message="Логотип Самоката не появился на странице"
        )
    with allure.step("Клик на логотип Самоката"):
        main_page.click_scooter_logo()  # кликаю на логотип
    with allure.step("Проверка URL после редиректа"):
        # проверяю URL, добавляю явное ожидание
        WebDriverWait(driver, 15).until(
            EC.url_to_be(SCOOTER_URL + "/"),
            message=f"Редирект на главную страницу не случился. Текущий URL: {driver.current_url}"
        )
