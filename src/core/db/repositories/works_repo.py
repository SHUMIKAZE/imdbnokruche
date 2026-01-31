from ..schema import WORKS_TABLE
from .base_repo import BaseRepo
from ...models import Work

class WorksRepo(BaseRepo[Work]):
    table = "works"
    model = Work
    _table_creation_sql = WORKS_TABLE
