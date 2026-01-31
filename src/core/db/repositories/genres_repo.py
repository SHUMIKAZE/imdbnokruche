from ..schema import GENRES_TABLE
from ...models import Genre
from .base_repo import BaseRepo

class GenresRepo(BaseRepo[Genre]):
    table = "genres"
    model = Genre
    _table_creation_sql = GENRES_TABLE
