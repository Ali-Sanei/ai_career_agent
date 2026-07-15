from app.models.job import Job


ALLOWED_KEYWORDS = [
    "Infrastructure",
    "System",
    "DevOps",
    "Cloud",
    "Platform",
    "SRE",
    "Linux",
    "Windows",
    "Virtualization",
    "VMware",
]


BLOCKED_KEYWORDS = [
    "Frontend",
    "Front-End",
    "Backend",
    "Back-End",
    "Full Stack",
    "Full-Stack",
    "Data Scientist",
    "Machine Learning",
    "QA",
    "Tester",
    "Designer",
    "Marketing",
    "Sales",
    "Intern",
]


class RuleEngine:

    def filter(self, jobs: list[Job]) -> list[Job]:

        filtered = []

        for job in jobs:

            title = job.title.lower()

            if any(word.lower() in title for word in BLOCKED_KEYWORDS):
                continue

            if any(word.lower() in title for word in ALLOWED_KEYWORDS):
                filtered.append(job)

        return filtered