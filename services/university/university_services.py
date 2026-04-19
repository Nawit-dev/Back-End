from services.general.base_services import BaseService
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.grades_helper import GradesHelper
from services.university.models.grades_request import GradesRequest
from services.university.models.grades_responses import GradesResponses
from services.university.models.grades_stats_request import GradesStatsRequest
from services.university.models.grades_stats_responses import GradesStatsResponse
from services.university.models.group_response import GroupResponse, DeleteStudentResponse
from services.university.models.group_request import GroupRequest, GroupDetailRequest
from services.university.models.student_request import StudentRequest, StudentDetailRequest
from services.university.models.student_response import StudentResponse
from services.university.models.teacher_request import TeacherRequest
from services.university.models.teacher_response import TeacherResponse
from services.university.helpers.teacher_helper import TeacherHelper
from utils.api_utils import ApiUtils
import os


class UniversityService(BaseService):
    SERVICE_URL = os.getenv("SERVICE_URL", "http://192.168.0.104:8001")


    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)
        self.grades_helper = GradesHelper(self.api_utils)

    def creat_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def creat_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def creat_grades(self, grades_request: GradesRequest) -> GradesResponses:
        response = self.grades_helper.post_grades(data=grades_request.model_dump())
        return GradesResponses(**response.json())

    def get_groups(self, group_detail_request: GroupDetailRequest) -> GroupResponse:
        response = self.group_helper.get_group(params=group_detail_request)
        return GroupResponse(**response.json())

    def get_student(self, student_detail_request: StudentDetailRequest) -> StudentResponse:
        response = self.student_helper.get_student(params=student_detail_request)
        return StudentResponse(**response.json())

    def delete_student(self, student_detail_request: StudentDetailRequest) -> DeleteStudentResponse:
        response = self.student_helper.delete_student(student_detail_request.student_id)
        return DeleteStudentResponse(**response.json())

    def get_grades(self) -> list[GradesResponses]:
        response = self.grades_helper.get_grades().json()
        return [GradesResponses.model_validate(x) for x in response]

    def get_stats_grades(self, grades_stats_request: GradesStatsRequest) -> GradesStatsResponse:
        response = self.grades_helper.get_stats(params=grades_stats_request.model_dump())
        return GradesStatsResponse(**response.json())
