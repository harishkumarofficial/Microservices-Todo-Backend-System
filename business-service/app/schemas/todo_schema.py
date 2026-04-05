from pydantic import BaseModel

class TodoCreateRequest(BaseModel):
    title: str
    description: str


class TodoUpdateRequest(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool  