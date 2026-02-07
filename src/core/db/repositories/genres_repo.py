from typing import Optional
from ..schema import GENRES_TABLE
from ...models import Genre
from .base_repo import BaseRepo

class GenresRepo(BaseRepo[Genre]):
    table = "genres"
    model = Genre
    _table_creation_sql = GENRES_TABLE

    def get_by_name(self, genre_name: str) -> Optional[Genre]:
        sql = f"SELECT * FROM {self.table} WHERE name = ?"

        row = self._db._fetchrow(sql, (genre_name,))
        if not row:
            return None

        obj = self.model.model_validate(dict(row))
        return obj

    def get_or_create(self, genre_name: str) -> Genre:
        genre = self.get_by_name(genre_name)
        if genre:
            return genre
        
        genre = Genre(name=genre_name)
        genre = self.add(genre)

        return genre
