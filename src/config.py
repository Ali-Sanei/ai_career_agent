from pathlib import Path

# Root Project Folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Profile Files
PROFILE_DIR = BASE_DIR / "profile"
PROMPTS_DIR = BASE_DIR / "prompts"
REPORTS_DIR = BASE_DIR / "reports"
JOBS_DIR = BASE_DIR / "jobs"

MASTER_PROFILE = PROFILE_DIR / "master_profile.md"
RESUME = PROFILE_DIR / "resume.pdf"

# Match Score
MINIMUM_SCORE = 85