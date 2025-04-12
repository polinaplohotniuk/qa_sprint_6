import pytest
from pages.faq_page import FaqPage
from locators.faq_locators import FaqLocators
import allure

@allure.title("Тесты раздела FAQ")
@allure.description("Проверка соответствия вопросов и ответов в разделе FAQ")
class TestFaq: # класс тестов для раздела "Вопросы и ответы"
    # параметризованный тест для проверки соответствия вопросов и ответов
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (FaqLocators.QUESTION_0, FaqLocators.ANSWER_0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (FaqLocators.QUESTION_1, FaqLocators.ANSWER_1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (FaqLocators.QUESTION_2, FaqLocators.ANSWER_2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (FaqLocators.QUESTION_3, FaqLocators.ANSWER_3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (FaqLocators.QUESTION_4, FaqLocators.ANSWER_4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (FaqLocators.QUESTION_5, FaqLocators.ANSWER_5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (FaqLocators.QUESTION_6, FaqLocators.ANSWER_6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (FaqLocators.QUESTION_7, FaqLocators.ANSWER_7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ], ids=["Вопрос 0", "Вопрос 1", "Вопрос 2", "Вопрос 3", "Вопрос 4", "Вопрос 5", "Вопрос 6", "Вопрос 7"])
    @allure.title("Проверка ответа на {question}")
    @allure.description("Проверяем соотвует фактический ответа ожидаемому, или нет")
    def test_faq_answers(self, driver, question_locator, answer_locator, expected_answer):
        with allure.step("Инициализация страницы 'Вопросы о важном'"):
            faq_page = FaqPage(driver)
        with allure.step("Клик на вопрос"):
            faq_page.click_question(question_locator)
        with allure.step("Получение фактического ответа"):
            actual_answer = faq_page.get_answer_text(answer_locator)
        with allure.step("Сравнение фактического результата и ожидаемого"):
            assert actual_answer == expected_answer, f"Текст фактического ответа отличается от ожидаемого. Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
