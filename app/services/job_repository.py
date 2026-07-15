import sqlite3
from pathlib import Path
from typing import List

from app.models.job import Job

DB_PATH = Path("data/jobs.db")


class JobRepository:
    def __init__(self):
        self.db_path = DB_PATH

    def save_many(self, jobs: List[Job]) -> tuple[int, int]:
        """
        Save jobs to database.

        Returns:
            (saved_count, skipped_count)
        """

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        saved = 0
        skipped = 0

        for job in jobs:

            if not job.is_valid():
                skipped += 1
                continue

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

            if cursor.rowcount == 1:
                saved += 1
            else:
                skipped += 1

        conn.commit()
        conn.close()

        return saved, skipped