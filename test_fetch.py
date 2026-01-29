from src.core.db.db_api import SQLite3Connection
from sqlite3 import Row, connect

conn = connect("media.db")
conn.row_factory = Row

db = SQLite3Connection(conn)

rows = db._fetch("SELECT * FROM genres WHERE name = ?", ("detective",))

for r in rows:
    print(dict(rows))
