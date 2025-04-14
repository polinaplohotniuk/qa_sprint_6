import pytest
from pages.faq_page import FaqPage
from locators.faq_locators import FaqLocators
import allure
from data.constants import ANSWER_0, ANSWER_1, ANSWER_2, ANSWER_3, ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7


@allure.feature("Раздел FAQ")  # добавляем общий раздел для всех тестов по вопросам о важном
class TestFaq: # класс тестов для раздела "Вопросы о важном"

    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
        (FaqLocators.QUESTION_0, FaqLocators.ANSWER_0, ANSWER_0),
        (FaqLocators.QUESTION_1, FaqLocators.ANSWER_1, ANSWER_1),
        (FaqLocators.QUESTION_2, FaqLocators.ANSWER_2, ANSWER_2),
        (FaqLocators.QUESTION_3, FaqLocators.ANSWER_3, ANSWER_3),
        (FaqLocators.QUESTION_4, FaqLocators.ANSWER_4, ANSWER_4),
        (FaqLocators.QUESTION_5, FaqLocators.ANSWER_5, ANSWER_5),
        (FaqLocators.QUESTION_6, FaqLocators.ANSWER_6, ANSWER_6),
        (FaqLocators.QUESTION_7, FaqLocators.ANSWER_7, ANSWER_7)
    ], ids=["Вопрос 0", "Вопрос 1", "Вопрос 2", "Вопрос 3", "Вопрос 4", "Вопрос 5", "Вопрос 6", "Вопрос 7"])
    @allure.story("Проверка ответов на вопросы")  # добавляем сценарии
    @allure.title("Проверка ответа на {question}")
    @allure.description("Проверяем соответствие фактического ответа ожидаемому")
    def test_faq_answers(self, driver, question_locator, answer_locator, expected_answer):
        with allure.step("Инициализация страницы FAQ"):
            faq_page = FaqPage(driver)
        with allure.step("Клик на вопрос"):
            faq_page.click_question(question_locator)
        with allure.step("Получение фактического ответа"):
            actual_answer = faq_page.get_answer_text(answer_locator)
        with allure.step("Сравнение фактического и ожидаемого результатов"):
            assert actual_answer == expected_answer, f"Текст ответа отличается от ожидаемого. Ожидалось: '{expected_answer}', получено: '{actual_answer}'"
