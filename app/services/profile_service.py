from app.services.profile_loader import ProfileLoader


class ProfileService:
    def __init__(self):
        self.loader = ProfileLoader()
        self._profile = None

    def get_profile(self):
        if self._profile is None:
            self._profile = self.loader.load()
        return self._profile

    def get_target_roles(self):
        return self.get_profile()["career"]["target_roles"]

    def get_blacklist(self):
        return self.get_profile()["blacklist"]

    def get_preferences(self):
        return self.get_profile()["preferences"]

    def get_skills(self):
        return self.get_profile()["skills"]