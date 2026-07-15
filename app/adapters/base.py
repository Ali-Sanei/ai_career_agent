from abc import ABC, abstractmethod
from typing import List

from app.models.job import Job


class BaseJobAdapter(ABC):
    @abstractmethod
    def fetch_jobs(self) -> List[Job]:
        """Fetch jobs from a source."""
        raise NotImplementedError