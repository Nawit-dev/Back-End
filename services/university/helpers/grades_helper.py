import requests

from services.general.helpers.BaseHelper import BaseHelper


class GradesHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    STATS_ENDPOINT = f"{ENDPOINT_PREFIX}/stats/"

    def post_grades(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response

    def get_grades(self, params: dict | None = None):
        response = self.api_utils.get(self.ROOT_ENDPOINT, params=params)
        return response

    def get_stats(self, params: dict | None = None) -> requests.Response:
        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response
