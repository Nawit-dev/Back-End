import time

import pytest
import requests

from faker import Faker

from services.auth.auth_services import AuthServices

from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.university_services import UniversityServices
from utils.api_utils import ApiUtils

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthServices.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="session", autouse=False)
def auth_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthServices.SERVICE_URL + "/docs")
            response.raise_for_status()
        except:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.")


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityServices.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym):
    auth_services = AuthServices(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_services.register_user(register_request=RegisterRequest(
        username=username,
        password=password,
        password_repeat=password,
        email=faker.email()))
    login_response = auth_services.login_user(login_request=LoginRequest(username=username, password=password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(url=AuthServices.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityServices.SERVICE_URL, headers={"Authorization": f"Bearer {access_token}"})
    return api_utils
