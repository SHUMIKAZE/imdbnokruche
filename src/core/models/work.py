from typing import Optional
from .base import BaseDBModel

class Work(BaseDBModel):
    original_title: str
    title: Optional[str] = None
    native_title: Optional[str] = None
    year: int
    format: str
    consumption_type: str
    industry: str
    # completed: bool = False
    # rating: Optional[float] = None
    # genres: List[str] = Field(default_factory=list)
