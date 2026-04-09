import requests

from services.university.helpers.grades_helper import GradesHelper


class TestGetGrades:

    def test_get_grades(self, university_api_utils_admin):
        grades_helper = GradesHelper(api_utils=university_api_utils_admin)
        response = grades_helper.get_grades()
        assert response.status_code == requests.status_codes.codes.ok, \
            f"Expected 200 OK, got {response.status_code}. Response: {response.text}"
