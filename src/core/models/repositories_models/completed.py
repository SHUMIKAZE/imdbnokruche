from typing import Optional
from .base import BaseDBModel

class Completed(BaseDBModel):
    view_count: int
    score: Optional[int] = 0
    notes: Optional[str] = None
