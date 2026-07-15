from app.services.profile_loader import ProfileLoader

profile = ProfileLoader().load()

print(profile["personal"]["name"])
print(profile["skills"]["expert"])