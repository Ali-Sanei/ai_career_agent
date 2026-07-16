from app.services.profile_service import ProfileService

service = ProfileService()

print(service.get_target_roles())
print(service.get_blacklist())
print(service.get_preferences())
print(service.get_skills())