from abc import ABC, abstractmethod
from typing import List, Any, Optional, Tuple


class BaseConnection(ABC):
    @abstractmethod
    def _fetch(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]],
    ) -> List[Any]:
        ...

    @abstractmethod
    def _fetchrow(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]],
    ) -> Any:
        ...

    @abstractmethod
    def _execute(
        self,
        sql: str,
        params: Optional[Tuple[Any, ...]],
    ) -> Optional[int]:
        ...

    @abstractmethod
    def _executescript(
        self,
        sql_script: str,
    ) -> None:
        ...
