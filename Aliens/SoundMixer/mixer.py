import pygame
import os.path


class Mixer:
    data_folder = os.path.join("Data", "Sounds")

    def __init__(self, music_volume, sounds_volume):
        self.music_volume = music_volume
        self.sounds_volume = sounds_volume
        pygame.mixer.init()
        # playback
        self.playback = self.prepare_playback()
        # sounds
        self.button_click = self.prepare_button_click()

    def set_playback_volume(self, value):
        self.music_volume = value
        self.playback.set_volume(value)

    def set_sounds_volume(self, value):
        self.sounds_volume = value
        self.button_click .set_volume(value)

    def prepare_playback(self):
        filename = "playback.wav"
        playback = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        playback.play(loops=-1)
        playback.set_volume(self.music_volume)
        return playback

    def prepare_button_click(self):
        filename = "button_click.ogg"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound
