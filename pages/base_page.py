import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:  # базовый класс страницы, содержащий общие методы
    def __init__(self, driver: WebDriver): # инициализация базовой страницы
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Переход по URL: {url}")
    def navigate(self, url): # переход по указанному URL
        self.driver.get(url)

    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator, timeout=10): # поиск элемента на странице с ожиданием
        return self.wait.until(EC.presence_of_element_located(locator), timeout=timeout)

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator): # клик по элементу с предварительной прокруткой до него
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except TimeoutException as e:
            print(f"Элемент не кликабельный: {locator}. Ошибка: {e}")
            raise

    @allure.step("Ввод текста '{text}' в поле: {locator}")
    def enter_text(self, locator, text): # ввод текста в поле с предварительной очисткой
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException as e:
            print(f"Поле ввода не найдено: {locator}. Ошибка: {e}")
            raise

    @allure.step("Проверка наличия элемента: {locator}")
    def element_is_present(self, locator, timeout=10): # проверка, есть ли элемент на странице
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
