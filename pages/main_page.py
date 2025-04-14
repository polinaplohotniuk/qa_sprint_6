import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):  # класс, представляющий главную страницу
    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # вызываем конструктор родительского класса
        self.driver = driver  # сохраняем экземпляр драйвера

    @allure.step("Клик на логотип Яндекса")  # клик на логотип Яндекса
    def click_yandex_logo(self):
        yandex_logo = self.wait.until(  # ожидаем, пока логотип Яндекса станет кликабельным
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)  # используем локатор логотипа Яндекса
        )
        yandex_logo.click()  # кликаем на логотип
        self.wait_for_new_window()  # ожидаем открытия нового окна

    @allure.step("Клик на логотип Самоката")  # клик на логотип Самоката
    def click_scooter_logo(self):
        logo = self.wait.until(  # ожидаем, пока логотип станет видимым
            EC.visibility_of_element_located(MainPageLocators.SCOOTER_LOGO)  # используем локатор логотипа
        )
        self.driver.execute_script("arguments[0].click();", logo)  # кликаем на логотип через JavaScript

    @allure.step("Переключение на новое окно")  # переключаемся на новое окно
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])  # переключаемся на последнее открытое окно
        return self

    @allure.step("Закрытие текущего окна")  # закрываем текущее окно
    def close_current_window(self):
        if len(self.driver.window_handles) > 1:  # если открыто больше одного окна
            self.driver.close()  # закрываем текущее окно
            self.driver.switch_to.window(self.driver.window_handles[0])  # переключаемся на первое окно

    @allure.step("Ожидание и проверка URL содержит: {expected_url}")  # ожидаем и проверяем, что URL содержит expected_url
    def wait_and_verify_url_contains(self, expected_url, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(  # ожидаем, пока URL не будет содержать expected_url
                EC.url_contains(expected_url),  # проверяем, что URL содержит expected_url
                message=f"Ожидаемый URL не содержит '{expected_url}'. Текущий URL: {self.driver.current_url}"  # сообщение об ошибке
            )
        except TimeoutException:  # если время ожидания истекло
            raise AssertionError(
                f"Не дождались загрузки страницы, содержащей {expected_url}")  # выбрасываем исключение

    @allure.step("Ожидание и проверка URL равен: {expected_url}")  # ожидаем и проверяем, что URL равен expected_url
    def wait_and_verify_url_to_be(self, expected_url, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(  # ожидаем, пока URL не будет равен expected_url
                EC.url_to_be(expected_url),  # проверяем, что URL равен expected_url
                message=f"Ожидаемый URL: '{expected_url}', текущий URL: {self.driver.current_url}"  # сообщение об ошибке
            )
        except TimeoutException:  # если время ожидания истекло
            raise AssertionError(f"Не дождались загрузки страницы с URL: {expected_url}")  # Выбрасываем исключение

    @allure.step("Открытие страницы: {url}")  # открываем страницу по URL
    def open_page(self, url):
        self.driver.get(url)  # открываем страницу

    @allure.step("Ожидание загрузки логотипа Самоката")  # ожидаем загрузку логотипа Самоката
    def wait_for_scooter_logo(self, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(  # ожидаем, пока логотип не станет кликабельным
                EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO),  # используем локатор логотипа
                message="Логотип Самоката не появился на странице"  # сообщение об ошибке
            )
        except TimeoutException:  # если время ожидания истекло
            raise AssertionError("Не дождались загрузки логотипа Самоката")  # выбрасываем исключение

    def wait_for_new_window(self, timeout=10):  # ожидаем открытие нового окна
        WebDriverWait(self.driver, timeout).until(  # ожидаем, пока не откроется новое окно
            self.new_window_is_opened,  # вызываем метод, проверяющий открытие нового окна
            message="Не дождались открытия нового окна"  # сообщение об ошибке
        )

    def new_window_is_opened(self, driver):  # проверяет, открылось ли новое окно
        return len(driver.window_handles) > 1  # возвращаем True, если количество окон больше 1
