from faker import Faker
from faker.generator import random

from logger.logger import Logger
from services.university.models.base_student import DegreeEnum
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.university_services import UniversityServices

faker = Faker()


class TestStudent:
    def test_student_create(self, university_api_utils_admin):
        Logger.info("### Step 1. Create group")
        university_services = UniversityServices(api_utils=university_api_utils_admin)
        group = GroupRequest(name=faker.name())
        group_response = university_services.creat_group(group_request=group)

        Logger.info("### Step 2. Create group")
        student = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice([option for option in DegreeEnum]),
            phone=faker.numerify("+7##########"),
            group_id=group_response.id)

        student_response = university_services.create_student(student_request=student)

        assert student_response.group_id == group_response.id, ("Wrong group id."
                                                                f"Actual: '{student_response.id}', "
                                                                f"but expected: '{group_response.id}'")
