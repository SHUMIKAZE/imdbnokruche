from ..db_api import BaseConnection
from ...models import Genre

class GenresRepo():
    def __init__(self, db: BaseConnection) -> None:
        self._db = db

    def add_genre(self, genre: Genre) -> None:
        data = genre.model_dump(exclude="id")
        cols = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        
        sql = f"INSERT INTO genres ({cols}) VALUES ({placeholders})"

        self._db._execute(sql, tuple(data.values()))
