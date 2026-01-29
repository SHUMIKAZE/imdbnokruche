from abc import ABC, abstractmethod
from typing import List, Any


class BaseConnection(ABC):
    @abstractmethod
    def _fetch(
        self,
        sql: str,
    ) -> List[Any]:
        ...

    @abstractmethod
    def _fetchrow(
        self,
        sql: str,
    ) -> Any:
        ...

    @abstractmethod
    def _execute(
        self,
        sql: str,
    ) -> None:
        ...
