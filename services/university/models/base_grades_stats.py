from pydantic import BaseModel, ConfigDict


class BaseGradesStats(BaseModel):
    model_config = ConfigDict(extra="forbid")
    student_id: None | int
    teacher_id: None | int
    group_id: None | int
