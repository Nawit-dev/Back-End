import requests

from services.university.helpers.grades_helper import GradesHelper


class TestGradesStatsAuth:
    def test_grades_stats_auth(self, university_api_utils_anonym):
        grades_helper = GradesHelper(api_utils=university_api_utils_anonym)
        response = grades_helper.get_grades()
        assert response.status_code == requests.status_codes.codes.unauthorized, \
            f"Expected 401 Unauthorized, got {response.status_code}. Response: {response.text}"
