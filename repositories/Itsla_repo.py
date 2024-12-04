from abc import ABC, abstractmethod
from typing import List

class ITslaRepo(ABC):

    @abstractmethod
    def get_all_succes(self) -> List[dict]:
        pass

    @abstractmethod
    def get_by_date_range(self, start_date: str, end_date: str) -> List[dict]:
        pass

    @abstractmethod
    def get_beursdata_DBD001(self) -> List[dict]:
        pass