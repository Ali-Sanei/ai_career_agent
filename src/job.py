from dataclasses import dataclass

@dataclass
class Job:

    title: str
    company: str
    location: str
    remote: bool
    url: str
    description: str