from logger.logger import Logger
from services.university.university_services import UniversityServices


class TestStatsCorrectForStudent:
    def test_stats_correct_for_student(self, university_api_utils_admin):
        university_services = UniversityServices(api_utils=university_api_utils_admin)

        response_grade = university_services.get_grades()
        grades = [item["grade"] for item in response_grade]
        count = len(grades)
        max_grade = max(grades)
        min_grade = min(grades)
        avg_grade = sum(grades) / len(grades)
        Logger.info(f"### Step 1. Get list response: {grades}")

        response_grade_stats = university_services.get_stats_grades()
        Logger.info(f"### Step 2. Get stats response: {response_grade_stats}")

        assert response_grade_stats["count"] == count, f"Expected count {count}, got {response_grade_stats['count']}"
        assert response_grade_stats["min"] == min_grade, f"Expected min {min_grade}, got {response_grade_stats['min']}"
        assert response_grade_stats["max"] == max_grade, f"Expected max {max_grade}, got {response_grade_stats['max']}"
        assert response_grade_stats["avg"] == avg_grade, f"Expected avg {avg_grade}, got {response_grade_stats['avg']}"
