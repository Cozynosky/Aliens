import pygame
import os.path


class Mixer:
    data_folder = os.path.join("Data", "Sounds")

    def __init__(self, music_volume, sounds_volume):
        self.music_volume = music_volume
        self.sounds_volume = sounds_volume
        pygame.mixer.init()
        # playback
        self.playback = self.prepare_playback("playback.wav")
        # sounds
        self.button_click = self.prepare_sound("button_click.ogg")
        self.player_shot = self.prepare_sound("player_shot.ogg")
        self.take_damage = self.prepare_sound("take_damage.mp3")
        self.collect_coin = self.prepare_sound("collect_coin.ogg")
        self.upgrade_buy = self.prepare_sound("upgrade_buy.wav")
        self.empty_magazine = self.prepare_sound("empty_magazine.wav")
        self.enemy_shot = self.prepare_sound("enemy_shot.ogg")
        self.ship_destroyed = self.prepare_sound("ship_destroyed.wav")
        self.swosh = self.prepare_sound("swosh.flac")
        self.game_over = self.prepare_sound("game_over.wav")

    def set_playback_volume(self, value):
        self.music_volume = value
        self.playback.set_volume(value)

    def set_sounds_volume(self, value):
        self.sounds_volume = value
        self.button_click.set_volume(value)
        self.player_shot.set_volume(value)
        self.take_damage.set_volume(value)
        self.game_over.set_volume(value)
        self.collect_coin.set_volume(value)
        self.upgrade_buy.set_volume(value)
        self.enemy_shot.set_volume(value)
        self.empty_magazine.set_volume(value)
        self.swosh.set_volume(value)
        self.ship_destroyed.set_volume(value)

    def prepare_playback(self, filename):
        playback = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        playback.play(loops=-1)
        playback.set_volume(self.music_volume)
        return playback

    def prepare_sound(self, filename):
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound
