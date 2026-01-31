from typing import List
from ..db_api import BaseConnection
from ...models import Genre

class GenresRepo():
    def __init__(self, db: BaseConnection) -> None:
        self._db = db

    def add_genre(self, genre: Genre) -> None:
        data = genre.model_dump(exclude={"id"})
        cols = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))
        
        sql = f"INSERT INTO genres ({cols}) VALUES ({placeholders})"

        self._db._execute(sql, tuple(data.values()))

    def get_all_genres(self) -> List[Genre]:
        sql = "SELECT * FROM genres"
        rows = self._db._fetch(sql, None)

        genres = [Genre.model_validate(dict(row)) for row in rows]

        return genres

    def get_by_id(self, genre_id: int) -> Genre:
        sql = "SELECT * FROM genres WHERE id = ?"

        row = self._db._fetchrow(sql, (genre_id,))
        genre = Genre.model_validate(dict(row))

        return genre

    def delete_genre(self, genre_id: int) -> None:
        sql = "DELETE FROM genres WHERE id = ?"
        self._db._execute(sql, (genre_id,))

    def update_genre(self, genre: Genre) -> None:
        data = genre.model_dump()
        assignment = ", ".join(f"{k}=?" for k in data.keys())

        sql = f"UPDATE genres SET {assignment} WHERE id = ?"

        self._db._execute(sql, (*data.values(), genre.id))

    def exists(self, genre_id) -> bool:
        sql = "SELECT 1 FROM genres WHERE id = ? LIMIT 1"
        
        return self._db._fetchrow(sql, (genre_id,)) is not None
