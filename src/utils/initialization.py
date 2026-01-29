from sqlite3 import Connection
from .tables import CREATE_WORKS_SQL


def init_db(conn: Connection) -> None:
    conn.executescript(CREATE_WORKS_SQL)
    conn.commit()
