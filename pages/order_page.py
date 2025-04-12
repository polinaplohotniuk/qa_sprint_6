import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from helpers import get_personal_data, get_comment


class OrderPage(BasePage): # класс для страницы заказа, наследуемся от BasePage
    def __init__(self, driver: WebDriver): # инициализация страницы заказа
        super().__init__(driver) # вызов конструктора родительского класса BasePage
        self.wait = WebDriverWait(driver, 15) # ожидание

    @allure.step("Клик на кнопку 'Заказать' с локатором: {button_locator}")
    def click_order_button(self, button_locator): # нажатие на кнопку "Заказать"
        with allure.step("Прокрутка страницы к кнопке"):
            element = self.wait.until(EC.element_to_be_clickable(button_locator)) # ждём, пока кнопка не станет кликабельной
            self.driver.execute_script("arguments[0].scrollIntoView();", element) # прокручиваем страницу к кнопке

        with allure.step("Клик на кнопку с помощью JavaScript"):
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнение личной информации")
    def fill_personal_info(self): # заполняем личную информацию
        with allure.step("Получение персональных данных"):
            name, lastname, city, phone = get_personal_data() # получаем данные из хелпера
        with allure.step(f"Ввод имени: {name}"):
            self.enter_text(OrderPageLocators.FIRST_NAME, name) # пишем имя
        with allure.step(f"Ввод фамилии: {lastname}"):
            self.enter_text(OrderPageLocators.SURNAME, lastname) # пишем фамилию
        with allure.step(f"Ввод адреса: {city}"):
            self.enter_text(OrderPageLocators.ADDRESS, city) # пишем адрес
        with allure.step(f"Ввод телефона: {phone}"):
            self.enter_text(OrderPageLocators.PHONE, phone) # пишем номер телефона

        with allure.step("Клик на поле 'Метро'"):
            self.click_element(OrderPageLocators.METRO_INPUT) # кликаем на поле "Метро"
        with allure.step("Выбор станции метро"):
            self.click_element(OrderPageLocators.METRO_STATION) # выбираем станцию метро
        with allure.step("Клик на кнопку 'Далее'"):
            self.click_element(OrderPageLocators.NEXT_BUTTON) # кликаем "Далее", чтобы перейти к следующему шагу

    @allure.step("Заполнение информации об аренде")
    def fill_rental_info(self): # заполняем информациюдля аренды
        try:
            with allure.step("Клик на поле 'Когда привезти'"):
                self.click_element(OrderPageLocators.RENTAL_DATE) # кликаем на поле "Когда привезти"
            with allure.step("Выбор даты"):
                self.click_element(OrderPageLocators.DATE_PICKER_DAY) # выбираем дату
            with allure.step("Клик на поле 'Срок аренды'"):
                self.click_element(OrderPageLocators.RENTAL_PERIOD) # кликаем на поле "Срок аренды"
            with allure.step("Выбор срока аренды"):
                self.click_element(OrderPageLocators.PERIOD_OPTION) # выбираем срок аренды
            with allure.step("Выбор цвета самоката"):
                self.click_element(OrderPageLocators.COLOR_BLACK) # выбираем цвет самоката
            with allure.step("Ввод комментария для курьера"):
                self.enter_text(OrderPageLocators.COMMENT, get_comment()) # пишем коммент для курьера
            with allure.step("Клик на кнопку 'Заказать'"):
                self.click_element(OrderPageLocators.ORDER_BUTTON) # кликаем "Заказать"
            with allure.step("Подтверждение заказа"):
                self.click_element(OrderPageLocators.CONFIRM_BUTTON) # подтверждаем заказ

        except Exception as e:
            print(f"Ошибка при заполнении информации об аренде: {str(e)}") # выводим ошибку
            raise

    @allure.step("Проверка отображения сообщения об успешном заказе")
    def is_success_displayed(self): # проверяем, что появилось сообщение об успешном заказе
        return self.element_is_present(OrderPageLocators.SUCCESS_MODAL) # проверяем наличие элемента
