from pydantic import BaseModel

from services.university.models.base_group import BaseGroup


class GroupRequest(BaseGroup):
    pass


class GroupDetailRequest(BaseModel):
    group_id: int
