from config import MASTER_PROFILE
from profile_loader import load_profile

def main():

    profile = load_profile(MASTER_PROFILE)

    print("=" * 50)
    print("MASTER PROFILE LOADED")
    print("=" * 50)
    print(profile[:1000])


if __name__ == "__main__":
    main()