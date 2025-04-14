import pytest
import allure
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage
from data.helpers import get_personal_data
from config import SCOOTER_URL
from selenium.webdriver.remote.webdriver import WebDriver


# параметризованный тест для проверки двух кнопок "Заказать"
@pytest.mark.parametrize("button_locator", [
    OrderPageLocators.ORDER_BUTTON_TOP,  # локатор верхней кнопки "Заказать"
    OrderPageLocators.ORDER_BUTTON_BOTTOM  # локатор нижней кнопки "Заказать"
], ids=["top_button", "bottom_button"])  # задаём ID для параметров, чтоб понимать, что проверяем
@allure.title("Проверка оформления заказа самоката с использованием кнопки {button_locator}")
@allure.description("Проверяет, что при нажатии на кнопку 'Заказать' (верхнюю или нижнюю) происходит успешное оформление заказа")
def test_order_flow(driver: WebDriver, button_locator):  # сам тест
    with allure.step("Инициализация страницы заказа"):
        page = OrderPage(driver)  # создаём экземпляр страницы заказа
    with allure.step("Открытие страницы Самоката"):
        page.navigate(SCOOTER_URL)  # открываем страницу Самоката
    with allure.step("Клик на кнопку 'Заказать'"):
        page.click_order_button(button_locator)  # кликаем на кнопку "Заказать"
    with allure.step("Заполнение личных данных"):
        page.fill_personal_info()  # заполняем личные данные
    with allure.step("Заполнение данных об аренде"):
        page.fill_rental_info()  # заполняем данные об аренде
    with allure.step("Проверка сообщения об успешном заказе"):
        assert page.is_success_displayed(), "Сообщение об успешном заказе не появилось."  # проверяем, что заказ оформился
