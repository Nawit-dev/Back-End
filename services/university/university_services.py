from services.general.base_services import BaseService
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.models.group_response import GroupResponse
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from services.university.models.teacher_request import TeacherRequest
from services.university.models.teacher_response import TeacherResponse
from services.university.helpers.teacher_helper import TeacherHelper
from utils.api_utils import ApiUtils


class UniversityServices(BaseService):
    SERVICE_URL = "http://192.168.0.104:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)


    def creat_group(self,group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def creat_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return  TeacherResponse(**response.json())