import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):  # класс для главной страницы, наследуемся от BasePage
    def __init__(self, driver: WebDriver): # инициализация главной страницы
        super().__init__(driver)  # вызов конструктора родительского класса BasePage
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Клик на логотип Яндекса")
    def click_yandex_logo(self): # клик на логотип Яндекса
        yandex_logo = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        )
        yandex_logo.click()

        self.wait.until(lambda d: len(d.window_handles) > 1)

    @allure.step("Клик на логотип Самоката")
    def click_scooter_logo(self): # клик на логотип Самоката
        logo = self.wait.until(
            EC.visibility_of_element_located(MainPageLocators.SCOOTER_LOGO)
        )
        self.driver.execute_script("arguments[0].click();", logo)

    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self): # переключение на последнюю открытую вкладку браузера
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self

    @allure.step("Закрытие текущего окна")
    def close_current_window(self): # закрывает текущую вкладку браузера, переключается на оставшуюся
        if len(self.driver.window_handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
