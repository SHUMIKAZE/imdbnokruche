from sqlite3 import Connection
from .tables import (
    CREATE_WORKS_SQL,
    CREATE_GENRES_SQL,
    CREATE_COMPLETED_SQL,
)


def init_db(conn: Connection) -> None:
    conn.executescript(CREATE_WORKS_SQL)
    conn.executescript(CREATE_GENRES_SQL)
    conn.executescript(CREATE_COMPLETED_SQL)
    conn.commit()
