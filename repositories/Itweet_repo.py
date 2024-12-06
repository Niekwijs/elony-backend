from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

class ITweetRepo(ABC):
    
    @abstractmethod
    def get_all(self) -> List[List]:
        """Fetch all tweets from the repository."""
        pass
    
    @abstractmethod
    def get_tweet_by_id(self, id: int) -> dict:
        """Fetch a tweet by its ID."""
        pass
    
    @abstractmethod
    def check_if_saved(self, tweet_id: int) -> bool:
        """Check if a tweet is saved."""
        pass
    
    @abstractmethod
    def save_tweet_by_id(self, tweet_id: int, save_date: datetime) -> dict:
        """Save a tweet by its ID."""
        pass
    
    @abstractmethod
    def get_three_after_date(self, date: datetime) -> List[List]:
        """Fetch three tweets after a specific date that haven't been saved."""
        pass