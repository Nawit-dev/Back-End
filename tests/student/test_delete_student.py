from services.university.models.student_request import StudentDetailRequest
from services.university.university_services import UniversityService


class TestDeleteStudent:
    def test_delete_student(self, university_api_utils_admin, group, student):
        university_services = UniversityService(api_utils=university_api_utils_admin)

        response = university_services.delete_student(StudentDetailRequest(student_id=student.id))

        assert response.detail == "Student deleted", (
            f"Wrong response detail. Actual: '{response.detail}', "
            f"expected: 'Student deleted'"
        )
