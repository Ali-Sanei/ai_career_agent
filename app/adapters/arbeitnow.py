import requests

from app.models.job import Job
from app.adapters.base import BaseJobAdapter


class ArbeitnowAdapter(BaseJobAdapter):

    URL = "https://www.arbeitnow.com/api/job-board-api"

    def fetch_jobs(self):

        response = requests.get(self.URL, timeout=30)

        response.raise_for_status()

        data = response.json()

        jobs = []

        for item in data["data"]:

            jobs.append(
                Job(
                    title=item.get("title", ""),
                    company=item.get("company_name", ""),
                    location=item.get("location", ""),
                    remote=item.get("remote", False),
                    url=item.get("url", ""),
                    description=item.get("description", "")
                )
            )

        return jobs