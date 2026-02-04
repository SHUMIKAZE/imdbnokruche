from typing import Dict, Optional, TypeVar, Generic, Type, List
from abc import ABC

from ...models import BaseDBModel
from ..db_api import BaseConnection

T = TypeVar("T", bound=BaseDBModel)

class BaseRepo(Generic[T], ABC):
    table: str
    model: Type[T]
    _table_creation_sql: str

    def __init__(self, db: BaseConnection) -> None:
        self._db = db

    def add(self, obj: T) -> None:
        if obj.id == 0:
            data = obj.model_dump(exclude={"id"})
        else:
            data = obj.model_dump()

        cols = ", ".join(data.keys())
        placeholders = ", ".join("?" * len(data))

        sql = f"INSERT INTO {self.table} ({cols}) VALUES ({placeholders})"

        self._db._execute(sql, (tuple(data.values())))

    def get_all(
            self,
            filter: Optional[Dict] = None,
            limit: Optional[int] = None,
            offset: Optional[int] = None) -> List[T]:
        sql = f"SELECT * FROM {self.table}"
        params: list = []
        
        if filter:
            conditions = []
            for k, v in filter.items():
                conditions.append(f"{k} = ?")
                params.append(v)
            sql += " WHERE " + " AND ".join(conditions)

        if limit is not None:
            sql += " LIMIT ?"
            params.append(limit)
            if offset is not None:
                sql += " OFFSET ?"
                params.append(offset)

        rows = self._db._fetch(sql, tuple(params))

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
