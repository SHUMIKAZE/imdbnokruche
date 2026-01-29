from src.db.db_api import SQLite3Connection
from sqlite3 import Row, connect

conn = connect("media.db")
conn.row_factory = Row

db = SQLite3Connection(conn)

db._execute("INSERT INTO genres(name) VALUES(?)", ("detective",))
