from pydantic import BaseModel

from services.university.models.base_student import BaseStudent


class StudentResponse(BaseStudent):
    id: int


class DeleteStudentResponse(BaseModel):
    detail: str
