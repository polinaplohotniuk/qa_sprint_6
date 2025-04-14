import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data.helpers import get_personal_data, get_comment
from config import SCOOTER_URL
from selenium.webdriver.common.action_chains import ActionChains


class OrderPage(BasePage):  # класс, представляющий страницу заказа самоката
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Открытие страницы заказа через кнопку вверху")  # открывает страницу заказа, кликая на кнопку 'Заказать' вверху страницы самоката
    def open_order_page_from_top(self):
        with allure.step("Переход на страницу заказа"):  # переходим на страницу заказа
            self.navigate(SCOOTER_URL)  # открываем главную страницу
        with allure.step("Клик по верхней кнопке 'Заказать'"):  # кликаем по верхней кнопке "Заказать"
            self.click_order_button(OrderPageLocators.ORDER_BUTTON_TOP)  # нажимаем на кнопку
        with allure.step("Заполнение личной информации"):  # заполняем личную информацию
            self.fill_personal_info()  # заполняем информацию
        with allure.step("Заполнение информации об аренде"):  # заполняем информацию об аренде
            self.fill_rental_info()  # заполняем информацию

    @allure.step("Открытие страницы заказа через кнопку внизу")  # открывает страницу заказа, кликая на кнопку 'Заказать' внизу страницы самоката
    def open_order_page_from_bottom(self):
        with allure.step("Переход на страницу заказа"):  # переходим на страницу заказа
            self.navigate(SCOOTER_URL)  # открываем главную страницу
        with allure.step("Клик по нижней кнопке 'Заказать'"):  # кликаем по нижней кнопке "Заказать"
            self.click_order_button(OrderPageLocators.ORDER_BUTTON_BOTTOM)  # нажимаем на кнопку
        with allure.step("Заполнение личной информации"):  # заполняем личную информацию
            self.fill_personal_info()  # заполняем информацию
        with allure.step("Заполнение информации об аренде"):  # заполняем информацию об аренде
            self.fill_rental_info()  # заполняем информацию

    @allure.step("Клик на кнопку 'Заказать' с локатором: {button_locator}")  # нажимает на кнопку 'Заказать'
    def click_order_button(self, button_locator):
        with allure.step("Ожидание исчезновения спиннера"):  # ожидаем исчезновения спиннера
            try:
                WebDriverWait(self.driver, 5).until(  # ждем исчезновения элемента
                    EC.invisibility_of_element_located(OrderPageLocators.MODAL_OVERLAY)  # используем локатор спиннера
                )
            except TimeoutException:
                print("Спиннер не исчез вовремя.")  # выводим сообщение, если спиннер не исчез

        with allure.step("Получение элемента"):  # получаем элемент кнопки
            element = self.wait.until(EC.element_to_be_clickable(button_locator))  # ждем, пока элемент станет кликабельным
        with allure.step("Прокрутка страницы к кнопке"):  # прокручиваем страницу к кнопке
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)  # прокручиваем элемент
        with allure.step("Небольшая пауза, чтобы убедиться, что элемент полностью виден"):  # небольшая пауза
            self.driver.implicitly_wait(0.5)  # ждем 0.5 секунды
        with allure.step("Клик со смещением"):  # кликаем по кнопке со смещением
            actions = ActionChains(self.driver)  # создаем ActionChains
            actions.move_to_element(element).move_by_offset(0, 1).click().perform()  # перемещаем курсор, делаем смещение и кликаем

    @allure.step("Заполнение личной информации")  # заполняет поля личной информации в форме заказа
    def fill_personal_info(self):
        with allure.step("Получение персональных данных"):  # получаем персональные данные
            name, surname, city, phone = get_personal_data()  # получаем данные
        with allure.step(f"Ввод имени: {name}"):  # вводим имя
            self.enter_text(OrderPageLocators.FIRST_NAME, name)  # вводим имя
        with allure.step(f"Ввод фамилии: {surname}"):  # вводим фамилию
            self.enter_text(OrderPageLocators.SURNAME, surname)  # вводим фамилию (surname, а не lastname)
        with allure.step(f"Ввод адреса: {city}"):  # вводим адрес
            self.enter_text(OrderPageLocators.ADDRESS, city)  # вводим адрес
        with allure.step(f"Ввод телефона: {phone}"):  # вводим номер телефона
            self.enter_text(OrderPageLocators.PHONE, phone)  # вводим номер телефона
        with allure.step("Клик на поле 'Метро'"):  # кликаем на поле "Метро"
            self.click_element(OrderPageLocators.METRO_INPUT)  # кликаем на поле "Метро"
        with allure.step("Выбор станции метро"):  # выбираем станцию метро
            self.click_element(OrderPageLocators.METRO_STATION)  # выбираем станцию метро
        with allure.step("Клик на кнопку 'Далее'"):  # кликаем на кнопку "Далее"
            self.click_element(OrderPageLocators.NEXT_BUTTON)  # кликаем "Далее", чтобы перейти к следующему шагу

    @allure.step("Заполнение информации об аренде")  # заполняет информацию об аренде в форме заказа
    def fill_rental_info(self):
        with allure.step("Клик на поле 'Когда привезти'"):  # кликаем на поле "Когда привезти"
            self.click_element(OrderPageLocators.RENTAL_DATE)  # кликаем на поле "Когда привезти"
        with allure.step("Выбор даты"):  # выбираем дату
            self.click_element(OrderPageLocators.DATE_PICKER_DAY)  # выбираем дату
        with allure.step("Клик на поле 'Срок аренды'"):  # кликаем на поле "Срок аренды"
            self.click_element(OrderPageLocators.RENTAL_PERIOD)  # кликаем на поле "Срок аренды"
        with allure.step("Выбор срока аренды"):  # выбираем срок аренды
            self.click_element(OrderPageLocators.PERIOD_OPTION)  # выбираем срок аренды
        with allure.step("Выбор цвета самоката"):  # выбираем цвет самоката
            self.click_element(OrderPageLocators.COLOR_BLACK)  # выбираем цвет самоката
        with allure.step("Ввод комментария для курьера"):  # вводим комментарий для курьера
            self.enter_text(OrderPageLocators.COMMENT, get_comment())  # пишем коммент для курьера
        with allure.step("Клик на кнопку 'Заказать'"):  # кликаем на кнопку "Заказать"
            self.click_element(OrderPageLocators.ORDER_BUTTON)  # кликаем "Заказать"
        with allure.step("Подтверждение заказа"):  # подтверждаем заказ
            self.click_element(OrderPageLocators.CONFIRM_BUTTON)  # подтверждаем заказ

    @allure.step("Проверка отображения сообщения об успешном заказе")  # проверяет, отображается ли сообщение об успешном заказе
    def is_success_displayed(self):
        with allure.step("Проверка наличия сообщения об успешном заказе"):  # проверяем наличие сообщения об успешном заказе
            return self.element_is_present(OrderPageLocators.SUCCESS_MODAL)  # проверяем наличие элемента
