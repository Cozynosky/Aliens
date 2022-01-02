import pickle
import os.path

from Aliens.Profile.profile import Profile


def load_profiles():
    profiles = []
    profiles_folder = os.path.join("Data", "Profiles")

    for i in range(1, 4):
        filename = f"Profile_{i}"
        try:
            with open(os.path.join(profiles_folder, filename), "rb") as f:
                profile = pickle.load(f)
                profiles.append(profile)
        except (FileNotFoundError, IOError, EOFError):
            new_profile = Profile()
            profiles.append(new_profile)
            with open(os.path.join(profiles_folder, filename), "wb") as f:
                pickle.dump(new_profile, f)
    return profiles
