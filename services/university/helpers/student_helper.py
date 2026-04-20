import requests

from services.general.helpers.BaseHelper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_student(self, params) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, params=params)
        return response

    def delete_student(self, student_id) -> requests.Response:
        endpoint = f"{self.ENDPOINT_PREFIX}/{student_id}/"
        response = self.api_utils.delete(endpoint)
        return response
