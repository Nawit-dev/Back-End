import allure
import requests
from services.university.helpers.grades_helper import GradesHelper


class TestGetGrades:
    @allure.feature("Grades")
    @allure.story("Получение списка оценок")
    def test_get_grades(self, university_api_utils_admin):
        grades_helper = GradesHelper(api_utils=university_api_utils_admin)
        with allure.step("Отправляем запрос на получение оценок"):
            response = grades_helper.get_grades()
        with allure.step("Проверяем статус код"):
            assert response.status_code == requests.status_codes.codes.ok, (
                f"Expected 200 OK, got {response.status_code}. Response: {response.text}"
            )

