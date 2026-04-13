import random

from logger.logger import Logger
from services.university.models.grade_limits import GradeLimits
from services.university.models.grades_request import GradesRequest
from services.university.models.grades_stats_request import GradesStatsRequest
from services.university.university_services import UniversityService
from utils.soft_assert import SoftAssert


class TestStatsCorrectForStudent:
    def test_stats_correct_for_student(self, university_api_utils_admin, teacher, student):
        university_services = UniversityService(api_utils=university_api_utils_admin)
        grades = []
        for _ in range(5):
            grade = GradesRequest(
                teacher_id=teacher.id,
                student_id=student.id,
                grade=random.randint(GradeLimits.MIN, GradeLimits.MAX))
            grades_responses = university_services.creat_grades(grades_request=grade)
            grades.append(grades_responses.grade)
        Logger.info(f"### Step 1. Get list response: {grades}")

        count = len(grades)
        max_grade = max(grades)
        min_grade = min(grades)
        avg_grade = sum(grades) / len(grades)

        grade_stats = GradesStatsRequest(
            teacher_id=teacher.id,
            student_id=student.id,
            group_id=student.group_id
        )

        response_grade_stats = university_services.get_stats_grades(grade_stats)
        Logger.info(f"### Step 2. Get stats response: {response_grade_stats}")

        sa = SoftAssert()

        sa(response_grade_stats.count == count, f"Expected count {count}, got {response_grade_stats.count}")
        sa(response_grade_stats.min == min_grade, f"Expected min {min_grade}, got {response_grade_stats.min}")
        sa(response_grade_stats.max == max_grade, f"Expected max {max_grade}, got {response_grade_stats.max}")
        sa(response_grade_stats.avg == avg_grade, f"Expected avg {avg_grade}, got {response_grade_stats.avg}")
        sa.finalize()
