from .base_repo import BaseRepo
from ...models import Work

class WorksRepo(BaseRepo[Work]):
    table = "works"
    model = Work
