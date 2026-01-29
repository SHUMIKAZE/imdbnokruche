from src.core.models.work import Work
from src.core.db.repositories.works_repo import WorksRepo
from src.core.db.db_api import SQLite3Connection
from sqlite3 import Row, connect

conn = connect("m.db")
conn.row_factory = Row

db = SQLite3Connection(conn)
work = Work(original_title="Pulp Fiction", year=1994, format="Film", consumption_type="watch", industry="American film")

rep = WorksRepo(db)

rep.add_work(work)
