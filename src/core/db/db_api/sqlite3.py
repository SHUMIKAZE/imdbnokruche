from typing import List, Any, Optional, Tuple
from sqlite3 import Connection

from .base import BaseConnection


class SQLite3Connection(BaseConnection):
    def __init__(self, conn: Connection) -> None:
        self._conn = conn

    def _fetch(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]],
    ) -> List[Any]:
        cursor = self._conn.cursor()
        cursor.execute(sql, params or ())
        rows = cursor.fetchall()

        return rows

    def _fetchrow(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]],
    ) -> Any:
        cursor = self._conn.cursor()
        cursor.execute(sql, params or ())
        row = cursor.fetchone()

        return row

    def _execute(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]],
    ) -> None:
        cursor = self._conn.cursor()
        cursor.execute(sql, params or ())
        self._conn.commit()

    def _executescript(self, sql_script: str) -> None:
        self._conn.executescript(sql_script)
        self._conn.commit()
