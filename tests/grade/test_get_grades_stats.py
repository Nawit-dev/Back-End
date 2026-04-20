from http import HTTPStatus

import allure
from services.university.helpers.grades_helper import GradesHelper


class TestGetGradesStats:
    @allure.feature("Grades statistics API")
    @allure.story("Получение статистики оценок авторизованным пользователем")
    def test_get_grades_stats(self, university_api_utils_admin):
        stats_grades = GradesHelper(api_utils=university_api_utils_admin)
        with allure.step("Отправляем запрос на получение статистики по оценкам"):
            response = stats_grades.get_stats()
        with allure.step("Проверяем статус код"):
            assert response.status_code == HTTPStatus.OK, (
                f"Expected 200 OK, got {response.status_code}. Response: {response.text}"
            )
