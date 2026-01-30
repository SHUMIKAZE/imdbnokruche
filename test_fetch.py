from src.core.db import WorksRepo
from src.core.db import SQLite3Connection
from src.utils import connect_db, close_db, init_db

from pathlib import Path
from pprint import pprint

db_path = Path("media.db")
conn = connect_db(db_path)
init_db(conn)

db = SQLite3Connection(conn)

rep = WorksRepo(db)

works = rep.get_all_works()

for work in works:
    print(work.id, work.original_title, work.year)

pprint(rep.get_work_by_id(1))

close_db(conn)
