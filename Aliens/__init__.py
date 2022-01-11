from Aliens.settings import Settings
from Aliens.SoundMixer.mixer import Mixer

SETTINGS = Settings()
SOUNDS = Mixer(SETTINGS.MUSIC_VOLUME, SETTINGS.SOUNDS_VOLUME)
