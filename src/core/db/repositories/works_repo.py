from typing import List
from ...models.work import Work
from ..db_api import BaseConnection

class WorksRepo():
    def __init__(self, db: BaseConnection) -> None:
        self._db = db

    def add_work(self, work: Work) -> None:
        sql = """
            INSERT INTO works(
                original_title,
                title,
                native_title,
                format,
                consumption_type,
                industry,
                year
            )
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """
        self._db._execute(sql, (
            work.original_title,
            work.title,
            work.native_title,
            work.format,
            work.consumption_type,
            work.industry,
            work.year,
        ))

    def get_all_works(self) -> List[Work]:
        sql = "SELECT * FROM works"
        rows = self._db._fetch(sql, None)

        works = [
            Work(
                id = row["id"],
                original_title = row["original_title"],
                title = row["title"],
                native_title = row["native_title"],
                format = row["format"],
                consumption_type = row["consumption_type"],
                industry = row["industry"],
                year = row["year"],
            )
            for row in rows
        ]

        return works 
