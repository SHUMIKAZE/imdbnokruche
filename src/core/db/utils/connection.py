from pathlib import Path
from sqlite3 import Connection, Row, connect

def connect_db(db_path: Path) -> Connection:
    conn = connect(db_path)
    conn.row_factory = Row
    return conn

def close_db(conn: Connection) -> None:
    conn.close()
