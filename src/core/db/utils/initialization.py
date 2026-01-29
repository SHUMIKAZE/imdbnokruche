from sqlite3 import Connection
from ..db_api import SQLite3Connection
from .tables import CREATE_WORKS_SQL


def init_db(conn: Connection) -> None:
    db = SQLite3Connection(conn)
    db._executescript(CREATE_WORKS_SQL)
