import random

import allure
from services.university.models.grade_limits import GradeLimits
from services.university.models.grades_request import GradesRequest
from services.university.models.grades_stats_request import GradesStatsRequest
from services.university.university_services import UniversityService
from utils.soft_assert import SoftAssert


class TestStatsCorrectForStudent:
    @allure.feature("Grades statistics API")
    @allure.story("Корректный расчёт статистики для студента")
    def test_stats_correct_for_student(self, university_api_utils_admin, teacher, student):
        university_services = UniversityService(api_utils=university_api_utils_admin)
        grades = []
        with allure.step("Создаём 5 оценок студенту"):
            for _ in range(5):
                grade = GradesRequest(
                    teacher_id=teacher.id, student_id=student.id, grade=random.randint(GradeLimits.MIN, GradeLimits.MAX)
                )
            grades_responses = university_services.creat_grades(grades_request=grade)
            grades.append(grades_responses.grade)
        with allure.step(f"Полученные оценки: {grades}"):
            pass

        count = len(grades)
        max_grade = max(grades)
        min_grade = min(grades)
        avg_grade = sum(grades) / len(grades)

        grade_stats = GradesStatsRequest(teacher_id=teacher.id, student_id=student.id, group_id=student.group_id)
        with allure.step("Запрашиваем статистику оценок"):
            response_grade_stats = university_services.get_stats_grades(grade_stats)
        with allure.step(f"Ответ статистики: {response_grade_stats}"):
            pass

        sa = SoftAssert()

        with allure.step("Проверяем count"):
            sa(response_grade_stats.count == count, f"Expected count {count}, got {response_grade_stats.count}")
        with allure.step("Проверяем min"):
            sa(response_grade_stats.min == min_grade, f"Expected min {min_grade}, got {response_grade_stats.min}")
        with allure.step("Проверяем max"):
            sa(response_grade_stats.max == max_grade, f"Expected max {max_grade}, got {response_grade_stats.max}")
        with allure.step("Проверяем avg"):
            sa(response_grade_stats.avg == avg_grade, f"Expected avg {avg_grade}, got {response_grade_stats.avg}")
        sa.finalize()

