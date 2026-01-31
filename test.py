from src.core.models import Work, Genre
from src.core.db import WorksRepo, GenresRepo
from src.core.db import SQLite3Connection
from src.utils import connect_db, close_db, init_db

from pathlib import Path
from json import dumps

db_path = Path("media.db")
conn = connect_db(db_path)
init_db(conn)

db = SQLite3Connection(conn)
wr = WorksRepo(db)
gr = GenresRepo(db)

works = wr.get_all_works()

work = Work(original_title="Inglourious Basterds", title="Russian title", year=2009, format="Film", consumption_type="watch", industry="American film")

wr.add_work(work)

works = wr.get_all_works()

for w in works:
    print(dumps(w.model_dump(), indent=2))

# print(dumps(work.model_dump(), indent=2))

print(wr.exists(3))

gen = Genre(name = "arthouse")

gr.add_genre(gen)

close_db(conn)
