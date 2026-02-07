from typing import List, Any, Optional, Tuple
from sqlite3 import Connection

from .base import BaseConnection


class SQLite3Connection(BaseConnection):
    def __init__(self, conn: Connection) -> None:
        self._conn = conn

    def _fetch(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]] = None,
    ) -> List[Any]:
        cursor = self._conn.cursor()
        if not params:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)

        rows = cursor.fetchall()
        return rows

    def _fetchrow(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]] = None,
    ) -> Any:
        cursor = self._conn.cursor()
        if not params:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)

        row = cursor.fetchone()
        return row

    def _execute(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]] = None,
        ) -> Optional[int]:
        cursor = self._conn.cursor()
        if not params:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)

        self._conn.commit()
        return cursor.lastrowid

    def _executescript(self, sql_script: str) -> None:
        self._conn.executescript(sql_script)
        self._conn.commit()
