from src.core.db import WorksRepo
from src.core.db import SQLite3Connection
from sqlite3 import Row, connect

conn = connect("m.db")
conn.row_factory = Row

db = SQLite3Connection(conn)

rep = WorksRepo(db)

works = rep.get_all_works()

for work in works:
    print(work.id, work.original_title, work.year)
