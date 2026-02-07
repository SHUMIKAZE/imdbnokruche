from pydantic import BaseModel

class BaseDBModel(BaseModel):
    id: int = 0
