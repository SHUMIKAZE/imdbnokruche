from src.core.models import Work, Genre, Completed, FullWork
from src.core.db import WorksRepo, GenresRepo, CompletedRepo, WorksGenresRepo, WorkService
from src.core.db import SQLite3Connection
from src.utils import connect_db, close_db, init_db

from pathlib import Path

db_path = Path("media.db")
conn = connect_db(db_path)
init_db(conn)

db = SQLite3Connection(conn)

wr = WorksRepo(db)
gr = GenresRepo(db)
cr = CompletedRepo(db)
wgr = WorksGenresRepo(db, wr, gr)

ws = WorkService(wr, gr, wgr, cr)

wr.rewrite()
gr.rewrite()
cr.rewrite()
wgr.rewrite()

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

print(gr.exists(3))
gr.delete(3)
print(gr.exists(3))



c1 = Completed(id=1, score=912, view_count=1)
c2 = Completed(id=2, score=1000, view_count=1)

cr.add(c1)
cr.add(c2)

coms = cr.get_all()

print("#" * 80)
for com in coms:
    print(com.model_dump_json(indent=2))

cr.set_score(work_id=1, score=922)
cr.set_notes(work_id=2, notes="Absolute cinema")
cr.increment_view(work_id=1)

coms = cr.get_all()

print("#" * 80)
for com in coms:
    print(com.model_dump_json(indent=2))



wgr.add(1, 1)
wgr.add(1, 2)
wgr.add(1, 5)
wgr.add(2, 1)
wgr.add(2, 4)

wgs = wgr.get_works_for_genre(1)
print("#" * 80)
for wg in wgs:
    print(wg.model_dump_json(indent=2))

wgr.remove(1, 1)

wgs = wgr.get_genres_for_work(1)
print("#" * 80)
for wg in wgs:
    print(wg.model_dump_json(indent=2))

rs = db._fetch("SELECT * FROM works_genres")
for r in rs:
    print(dict(r))

print(wgr.exists(1, 5))
print(wgr.exists(3, 3))

fullwork = ws.get_full_work(2)

fw = Work(original_title="asdadasd", year=15, format="Series", consumption_type="watch", industry="asdda")
fg1 = g1
fg2 = Genre(name="sadasdad")
fc = Completed(view_count=2, score=234)

ffw = FullWork(work=fw, genres=[fg1, fg2], completed=fc)

ffw = ws.create_work(ffw)

print(ffw)

close_db(conn)
