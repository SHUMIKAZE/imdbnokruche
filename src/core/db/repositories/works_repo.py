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
