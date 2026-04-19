import requests
import allure

from services.university.helpers.grades_helper import GradesHelper


class TestGradesStatsAuth:
    @allure.feature("Grades Stats API")
    @allure.story("Запрос без авторизации возвращает 401")
    def test_grades_stats_auth(self, university_api_utils_anonym):
        grades_helper = GradesHelper(api_utils=university_api_utils_anonym)
        with allure.step("Отправляем запрос на получение оценок"):
            response = grades_helper.get_grades()
        with allure.step("Проверяем статус код"):
            assert response.status_code == requests.status_codes.codes.unauthorized, \
                f"Expected 401 Unauthorized, got {response.status_code}. Response: {response.text}"
