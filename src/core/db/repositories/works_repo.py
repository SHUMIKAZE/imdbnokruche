from typing import List
from ...models import Work
from ..db_api import BaseConnection

class WorksRepo():
    def __init__(self, db: BaseConnection) -> None:
        self._db = db

    def add_work(self, work: Work) -> None:
        data = work.to_table_works()

        cols = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))

        sql = f"INSERT INTO works ({cols}) VALUES ({placeholders})"

        self._db._execute(sql, tuple(data.values()))

    def get_all_works(self) -> List[Work]:
        sql = "SELECT * FROM works"
        rows = self._db._fetch(sql, None)

        works = [Work.model_validate(dict(row)) for row in rows]

        return works 
