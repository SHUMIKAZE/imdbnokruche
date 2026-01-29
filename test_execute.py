from src.core.models.work import Work
from src.core.db.repositories.works_repo import WorksRepo
from src.core.db.db_api import SQLite3Connection
from src.utils import connect_db, close_db, init_db

from pathlib import Path

db_path = Path("media.db")

conn = connect_db(db_path)
init_db(conn)

db = SQLite3Connection(conn)
work = Work(original_title="Inglourious Basterds", year=2009, format="Film", consumption_type="watch", industry="American film")

rep = WorksRepo(db)

rep.add_work(work)

close_db(conn)
