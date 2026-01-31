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

wr.rewrite()
gr.rewrite()

#####################################################
################ START TESTING HERE #################
#####################################################

w1 = Work(original_title="Parasyte: The Maxim", year=2015, format="Series", consumption_type="watch", industry="Japanese animation")
w2 = Work(original_title="Pulp Fiction", year=1994, format="Movie", consumption_type="watch", industry="American film")
w3 = Work(original_title="Breaking Bad", year=2013, format="Series", consumption_type="watch", industry="American series")
w4 = Work(original_title="War and piece", year=1867, format="Book", consumption_type="read", industry="Russian classic")

wr.add(w1)
wr.add(w2)
wr.add(w3)
wr.add(w4)

works = wr.get_all(limit=3, offset=1)

print("#" * 80)
for work in works:
    print(work.model_dump_json(indent=2))

w3 = Work(id=3, original_title="Better Call Saul", year=2022, format="Series", consumption_type="watch", industry="American series")

wr.update(w3)

works = wr.get_all(filter={"consumption_type": "watch"})

print("#" * 80)
for work in works:
    print(work.model_dump_json(indent=2))


g1 = Genre(name="arthouse")
g2 = Genre(name="drama")
g3 = Genre(name="novel")
g4 = Genre(name="detective")
g5 = Genre(name="shounen")

gr.add(g1)
gr.add(g2)
gr.add(g3)
gr.add(g4)
gr.add(g5)

genres = gr.get_all()

print("#" * 80)
for genre in genres:
    print(genre.model_dump_json(indent=2))

print(gr.exists(5))
gr.delete(5)
print(gr.exists(5))


close_db(conn)
