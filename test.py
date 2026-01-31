from src.core.models import Work, Genre
from src.core.db import WorksRepo, GenresRepo
from src.core.db import SQLite3Connection
from src.utils import connect_db, close_db, init_db

from pathlib import Path

db_path = Path("media.db")
conn = connect_db(db_path)
init_db(conn)

db = SQLite3Connection(conn)
wr = WorksRepo(db)
gr = GenresRepo(db)

works = wr.get_all()

work = Work(original_title="Inglourious Basterds", title="Russian title", year=2009, format="Film", consumption_type="watch", industry="American film")

wr.add(work)

works = wr.get_all()

for w in works:
    print(w.model_dump_json(indent=2))


print(wr.exists(3))

gen = Genre(name = "arthouse")

if not gr.exists(1):
    gr.add(gen)
gr.delete(1)

gen2 = Genre(id = 2, name = "detective")

gr.add(gen2)

gen3 = Genre(id = 2, name = "definately not detective")

gr.update(gen3)

genres = gr.get_all()
for g in genres:
    print(g.model_dump_json(indent=2))

close_db(conn)
