from typing import List, Any
from sqlite3 import Connection

from .base import BaseConnection


class SQLite3Connection(BaseConnection):
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def _fetch(self, sql: str) -> List[Any]:
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        return rows

    def _fetchrow(self, sql: str) -> Any:
        cursor = self.conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()

        return row

    def _execute(self, sql: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

    def _executescript(self, sql_script: str) -> None:
        self.conn.executescript(sql_script)
        self.conn.commit()
