from services.university.models.student_request import StudentDetailRequest
from services.university.university_services import UniversityService
from utils.soft_assert import SoftAssert


class TestGetStudent:
    def test_get_student(self, university_api_utils_admin, group, student):
        university_services = UniversityService(api_utils=university_api_utils_admin)

        response = university_services.get_student(StudentDetailRequest(student_id=student.id))

        sa = SoftAssert()

        sa(student.id == response.id, f"id mismatch: expected={student.id}, actual={response.id}")
        sa(
            student.first_name == response.first_name,
            f"first_name mismatch: expected={student.first_name}, actual={response.first_name}",
        )
        sa(
            student.last_name == response.last_name,
            f"last_name mismatch: expected={student.last_name}, actual={response.last_name}",
        )
        sa(student.email == response.email, f"email mismatch: expected={student.email}, actual={response.email}")
        sa(student.degree == response.degree, f"degree mismatch: expected={student.degree}, actual={response.degree}")
        sa(student.phone == response.phone, f"phone mismatch: expected={student.phone}, actual={response.phone}")
        sa(
            student.group_id == response.group_id,
            f"group_id mismatch: expected={student.group_id}, actual={response.group_id}",
        )
        sa.finalize()
