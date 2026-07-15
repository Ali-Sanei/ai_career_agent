import json
from pathlib import Path


class ProfileLoader:

    def __init__(self):
        self.profile_path = Path("profile/master_profile.json")

    def load(self):

        with open(self.profile_path, encoding="utf-8") as f:
            return json.load(f)