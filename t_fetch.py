from src.core.models import Work
from src.core.db import WorksRepo
from src.core.db import SQLite3Connection
from src.utils import connect_db, close_db, init_db

from pathlib import Path
from json import dumps

db_path = Path("media.db")
conn = connect_db(db_path)
init_db(conn)

db = SQLite3Connection(conn)
rep = WorksRepo(db)

works = rep.get_all_works()

work = Work(id = 3, original_title="Inglourious Basterds", title="Russian title", year=2009, format="Film", consumption_type="watch", industry="American film")

rep.add_work(work)

works = rep.get_all_works()

for w in works:
    print(dumps(w.model_dump(), indent=2))

print(dumps(work.model_dump(), indent=2))

print(rep.exists(3))

close_db(conn)
