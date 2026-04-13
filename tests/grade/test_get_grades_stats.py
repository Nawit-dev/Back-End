import requests

from services.university.helpers.grades_helper import GradesHelper


class TestGetGradesStats:

    def test_get_grades_stats(self, university_api_utils_admin, ):
        stats_grades = GradesHelper(api_utils=university_api_utils_admin)
        response = stats_grades.get_stats()
        assert response.status_code == requests.status_codes.codes.ok, \
            f"Expected 200 OK, got {response.status_code}. Response: {response.text}"
