from typing import Optional
from ..repositories import (
    WorksRepo,
    GenresRepo,
    CompletedRepo,
    WorksGenresRepo,
)

from ...models import FullWork

class WorkService:
    def __init__(
        self,
        works_repo: WorksRepo,
        genres_repo: GenresRepo,
        works_genres_repo: WorksGenresRepo,
        completed_repo: CompletedRepo,
    ) -> None:
        self.works_repo = works_repo
        self.genres_repo = genres_repo
        self.works_genres_repo = works_genres_repo
        self.completed_repo = completed_repo

    def create_work(self) -> None:
        pass

    def delete_work(self):
        pass
    
    def complete_work(self):
        pass

    def uncomplete_work(self):
        pass

    def add_genres(self):
        pass

    def get_full_work(self, work_id: int) -> Optional[FullWork]:
        work = self.works_repo.get_by_id(work_id)
        if not work:
            return None

        genres = self.works_genres_repo.get_genres_for_work(work_id)
        completed = self.completed_repo.get_by_id(work_id)
        
        return FullWork(work=work, genres=genres, completed=completed)

    def get_works(self):
        pass
