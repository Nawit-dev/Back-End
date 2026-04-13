from services.university.models.grade_limits import GradeLimits

from pydantic import BaseModel, ConfigDict, Field


class BaseGrades(BaseModel):
    model_config = ConfigDict(extra="forbid")
    teacher_id: int
    student_id: int
    grade: int = Field(ge=GradeLimits.MIN, le=GradeLimits.MAX)
