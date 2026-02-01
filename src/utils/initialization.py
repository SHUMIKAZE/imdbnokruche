from sqlite3 import Connection
from ..core.db.schema import (
    WORKS_TABLE,
    GENRES_TABLE,
    COMPLETED_TABLE,
)


def init_db(conn: Connection) -> None:
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(WORKS_TABLE)
    conn.executescript(GENRES_TABLE)
    conn.executescript(COMPLETED_TABLE)
    conn.commit()
