from dataclasses import dataclass


@dataclass(slots=True)
class Job:
    title: str
    company: str
    location: str
    remote: bool
    url: str
    description: str

    def is_valid(self) -> bool:
        return bool(
            self.title.strip()
            and self.company.strip()
            and self.url.strip()
        )