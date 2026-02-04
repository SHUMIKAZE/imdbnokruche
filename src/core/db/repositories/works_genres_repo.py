from typing import List

from ..schema import WORKS_GENRES_TABLE

from ...models import Genre, Work
from ..db_api import BaseConnection
from .genres_repo import GenresRepo
from .works_repo import WorksRepo


class WorksGenresRepo:
    table = "works_genres"
    _table_creation_sql = WORKS_GENRES_TABLE


    def __init__(
        self,
        db: BaseConnection,
        works_repo: WorksRepo,
        genres_repo: GenresRepo,
    ) -> None:
        self._db = db
        self._works_repo = works_repo
        self._genres_repo = genres_repo

    def add(self, work_id: int, genre_id: int) -> None:
        sql = f"INSERT OR IGNORE INTO {self.table} (work_id, genre_id) VALUES (?, ?)"
        self._db._execute(sql, (work_id, genre_id,))

    def remove(self, work_id: int, genre_id: int) -> None:
        sql = f"DELETE FROM {self.table} WHERE work_id = ? AND genre_id = ?"

        self._db._execute(sql, (work_id, genre_id,))

    def get_genres_for_work(self, work_id: int) -> List[Genre]:
        sql = f"""
            SELECT g.* FROM genres g
            JOIN {self.table} wg ON g.id = wg.genre_id
            WHERE wg.work_id = ?
        """
        rows = self._db._fetch(sql, (work_id,))

        return [self._genres_repo.model.model_validate(dict(r)) for r in rows]

    def get_works_for_genre(self, genre_id: int) -> List[Work]:
        sql = f"""
            SELECT w.* FROM works w
            JOIN {self.table} wg ON w.id = wg.work_id
            WHERE wg.genre_id = ?
        """
        rows = self._db._fetch(sql, (genre_id,))

        return [self._works_repo.model.model_validate(dict(r)) for r in rows]

    def rewrite(self) -> None:
        sql = f"""
            DROP TABLE IF EXISTS {self.table};
            {self._table_creation_sql}
        """
        
        self._db._executescript(sql)
