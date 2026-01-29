from typing import List, Any
from sqlite3 import Connection

from .base import BaseConnection


class SQLite3Connection(BaseConnection):
    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    def _fetch(self, sql: str) -> List[Any]:
        cursor = self.conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        return data
