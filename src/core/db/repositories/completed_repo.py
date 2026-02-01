from ..schema import COMPLETED_TABLE
from .base_repo import BaseRepo
from ...models import Completed

class CompletedRepo(BaseRepo[Completed]):
    table = "completed"
    model = Completed
    _table_creation_sql = COMPLETED_TABLE

    def increment_view(self, work_id: int) -> None:
        sql = f"UPDATE {self.table} SET view_count = view_count + 1 WHERE id = ?"

        self._db._execute(sql, (work_id,))

    def set_score(self, work_id: int, score: int) -> None:
        sql = f"UPDATE {self.table} SET score = ? WHERE id = ?"

        self._db._execute(sql, (score, work_id,))

    def set_notes(self, work_id: int, notes: str) -> None:
        sql = f"UPDATE {self.table} SET notes = ? WHERE id = ?"

        self._db._execute(sql, (notes, work_id,))
