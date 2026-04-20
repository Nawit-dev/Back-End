import random
import time

import pytest
import requests
from faker import Faker
from services.auth.auth_services import AuthServices
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import Subjects
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_services import UniversityService
from utils.api_utils import ApiUtils

faker = Faker()


@pytest.fixture
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthServices.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="session")
def auth_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthServices.SERVICE_URL + "/docs", timeout=5)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.")


@pytest.fixture
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture
def access_token(auth_api_utils_anonym):
    auth_services = AuthServices(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30, special_chars=True, digits=True, upper_case=True, lower_case=True)
    auth_services.register_user(
        register_request=RegisterRequest(
            username=username, password=password, password_repeat=password, email=faker.email()
        )
    )
    login_response = auth_services.login_user(login_request=LoginRequest(username=username, password=password))
    return login_response.access_token


@pytest.fixture
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthServices.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture
def group(university_api_utils_admin):
    university_services = UniversityService(api_utils=university_api_utils_admin)
    group = GroupRequest(name=faker.name())
    group_response = university_services.creat_group(group_request=group)
    return group_response


@pytest.fixture
def teacher(university_api_utils_admin):
    university_services = UniversityService(api_utils=university_api_utils_admin)
    teacher = TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice([subject.value for subject in Subjects]),
    )
    teacher_response = university_services.creat_teacher(teacher_request=teacher)
    return teacher_response


@pytest.fixture
def student(university_api_utils_admin, group):
    university_services = UniversityService(api_utils=university_api_utils_admin)
    student = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=random.choice(list(DegreeEnum)),
        phone=faker.numerify("+7##########"),
        group_id=group.id,
    )

    student_response = university_services.create_student(student_request=student)
    return student_response

