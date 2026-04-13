from pydantic import BaseModel

from services.university.models.base_student import BaseStudent


class StudentRequest(BaseStudent):
    pass


class StudentDetailRequest(BaseModel):
    student_id: int
