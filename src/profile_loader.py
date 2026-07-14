from pathlib import Path

def load_profile(profile_path: Path) -> str:
    with open(profile_path, "r", encoding="utf-8") as file:
        return file.read()