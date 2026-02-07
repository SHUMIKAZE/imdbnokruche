from ..repositories_models import (
    Work,
    Genre,
    Completed,
)

from pydantic import BaseModel, Field
from typing import List, Optional

class FullWork(BaseModel):
    work: Work
    genres: List[Genre] = Field(default_factory=list)
    completed: Optional[Completed]
