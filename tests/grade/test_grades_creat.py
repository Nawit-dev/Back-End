import random
from services.university.models.grade_limits import GradeLimits
from services.university.models.grades_request import GradesRequest
from services.university.university_services import UniversityService
from faker import Faker

from utils.soft_assert import SoftAssert

faker = Faker()


class TestGradesCreat:

    def test_grades_creat(self, university_api_utils_admin, teacher, student):
        university_services = UniversityService(api_utils=university_api_utils_admin)
        grade = GradesRequest(teacher_id=teacher.id, student_id=student.id,
                              grade=random.randint(GradeLimits.MIN, GradeLimits.MAX))
        grades_responses = university_services.creat_grades(grades_request=grade)

        sa = SoftAssert()

        sa(grades_responses.teacher_id == grade.teacher_id,
           f"Expected teacher_id={grade.teacher_id}, got {grades_responses.teacher_id}")
        sa(grades_responses.student_id == grade.student_id,
           f"Expected student_id={grade.student_id}, got {grades_responses.student_id}")
        sa(grades_responses.grade == grade.grade, f"Expected grade={grade.grade}, got {grades_responses.grade}")
        sa(grades_responses.id is not None, f"Expected id to be set, got None")
        sa.finalize()
