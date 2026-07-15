from app.adapters.arbeitnow import ArbeitnowAdapter
from app.services.job_repository import JobRepository
from app.storage.database import init_database
from app.utils.logger import logger

logger.info("Starting AI Career Agent")

init_database()

adapter = ArbeitnowAdapter()

jobs = adapter.fetch_jobs()

logger.info(f"Found {len(jobs)} jobs")

repo = JobRepository()

saved, skipped = repo.save_many(jobs)

logger.info(f"Saved: {saved}")

logger.info(f"Skipped: {skipped}")