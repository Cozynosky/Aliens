import pickle
import os.path


def save_profiles(profiles):
    profiles_folder = os.path.join("Data", "Profiles")

    for i in range(len(profiles)):
        filename = f"Profile_{i+1}"

        with open(os.path.join(profiles_folder, filename), "wb") as f:
            pickle.dump(profiles[i], f)
