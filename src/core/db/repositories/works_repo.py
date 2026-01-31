from typing import List
from ...models import Work
from ..db_api import BaseConnection

class WorksRepo():
    def __init__(self, db: BaseConnection) -> None:
        self._db = db

    def add_work(self, work: Work) -> None:
        data = work.model_dump(exclude="id")

        cols = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))

        sql = f"INSERT INTO works ({cols}) VALUES ({placeholders})"

        self._db._execute(sql, tuple(data.values()))

    def get_all_works(self) -> List[Work]:
        sql = "SELECT * FROM works"
        rows = self._db._fetch(sql, None)

        works = [Work.model_validate(dict(row)) for row in rows]

        return works 

    def get_work_by_id(self, work_id: int) -> Work:
        sql = "SELECT * FROM works WHERE id = ?"

        row = self._db._fetchrow(sql, (work_id,))
        work = Work.model_validate(dict(row))

        return work

    def delete_work(self, work_id: int) -> None:
        sql = "DELETE FROM works WHERE id = ?"
        self._db._execute(sql, (work_id,))

    def update_work(self, work: Work) -> None:
        data = work.model_dump()
        assignment = ", ".join(f"{k}=?" for k in data.keys())

        sql = f"UPDATE works SET {assignment} WHERE id = ?"

        self._db._execute(sql, (*data.values(), work.id))

    def exists(self, work_id) -> bool:
        sql = "SELECT 1 FROM works WHERE id = ? LIMIT 1"
        
        return self._db._fetchrow(sql, (work_id,)) is not None
