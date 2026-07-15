import sqlite3
from pathlib import Path
from typing import List

from app.models.job import Job

DB_PATH = Path("data/jobs.db")


class JobRepository:
    def __init__(self):
        self.db_path = DB_PATH

    def save(self, job: Job):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR IGNORE INTO jobs (
                title,
                company,
                location,
                remote,
                url,
                description,
                score,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                job.title,
                job.company,
                job.location,
                int(job.remote),
                job.url,
                job.description,
                None,
                "NEW",
            ),
        )

        conn.commit()
        conn.close()

    def save_many(self, jobs: List[Job]):
        for job in jobs:
            if job.is_valid():
                self.save(job)