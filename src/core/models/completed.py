from typing import Optional
from pydantic import BaseModel

class Completed(BaseModel):
    work_id: int = 0
    rating: Optional[float] = 0
    notes: Optional[str]
