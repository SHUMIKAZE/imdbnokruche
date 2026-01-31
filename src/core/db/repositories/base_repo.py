from typing import TypeVar, Generic, Type, List
from abc import ABC

from ...models import BaseDBModel
from src.core.db.db_api.base import BaseConnection

T = TypeVar("T", bound=BaseDBModel)

class BaseRepo(Generic[T], ABC):
    table: str
    model: Type[T]
    _table_creation_sql: str

    def __init__(self, db: BaseConnection) -> None:
        self._db = db

    def add(self, obj: T) -> None:
        data = obj.model_dump(exclude={"id"})
        cols = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))

        sql = f"INSERT INTO {self.table} ({cols}) VALUES ({placeholders})"

        self._db._execute(sql, (tuple(data.values())))

    def get_all(self) -> List[T]:
        sql = f"SELECT * FROM {self.table}"
        rows = self._db._fetch(sql, None)

        objs = [self.model.model_validate(dict(row)) for row in rows]

        return objs 

    def get_by_id(self, obj_id: int) -> T:
        sql = f"SELECT * FROM {self.table} WHERE id = ?"

        row = self._db._fetchrow(sql, (obj_id,))
        obj = self.model.model_validate(dict(row))

        return obj

    def delete(self, obj_id: int) -> None:
        sql = f"DELETE FROM {self.table} WHERE id = ?"
        self._db._execute(sql, (obj_id,))

    def update(self, obj: T) -> None:
        data = obj.model_dump()
        assignment = ", ".join(f"{k}=?" for k in data.keys())

        sql = f"UPDATE {self.table} SET {assignment} WHERE id = ?"

        self._db._execute(sql, (*data.values(), obj.id))

    def exists(self, obj_id) -> bool:
        sql = f"SELECT 1 FROM {self.table} WHERE id = ? LIMIT 1"
        
        return self._db._fetchrow(sql, (obj_id,)) is not None

    def rewrite (self) -> None:
        sql = f"""
        DROP TABLE IF EXISTS {self.table};
        {self._table_creation_sql}
        """

        self._db._executescript(sql)
