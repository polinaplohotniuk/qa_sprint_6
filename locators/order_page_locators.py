from selenium.webdriver.common.by import By

class OrderPageLocators: # локаторы для элементов страницы оформления заказа
    # кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[contains(text(), 'Заказать')])[1]") # верхняя кнопка "Заказать" на странице
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]") # нижняя кнопка "Заказать" на странице

    # 1. поля формы "Для кого самокат"
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']") # поле ввода имени
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле ввода фамилии
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поле ввода адреса
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле ввода номера телефона

    # элементы выбора станции метро
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле ввода станции метро
    METRO_STATION = (By.XPATH, "//li[@class='select-search__row' and contains(., 'Сокольники')]") # сама станция метро

    # кнопка перехода
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']") # кнопка "Далее" после заполнения формы "Для кого самокат"

    # 2. поля формы "Про аренду"
    RENTAL_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле выбора даты доставки
    DATE_PICKER_DAY = (By.XPATH,
                       "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='26']")
    # выбираем число
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")  # выпадающий список срока аренды
    PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")  # опция "сутки" в выпадающем списке
    COLOR_BLACK = (By.ID, "black") # чекбокс возле чёрного цвета
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # поле комментария

    # кнопки подтверждения заказа
    ORDER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")  # кнопка "Заказать" на форме "Про аренду"
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']") # Кнопка подтверждения в модальном окне
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]") # модальное окно с подтверждением заказа
