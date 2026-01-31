from ...models import Genre
from .base_repo import BaseRepo

class GenresRepo(BaseRepo[Genre]):
    table = "genres"
    model = Genre
