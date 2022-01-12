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
        self.player_shot = self.prepare_player_shot()
        self.take_damage = self.prepare_take_damage()
        self.collect_coin = self.prepare_collect_coin()
        self.upgrade_buy = self.prepare_upgrade_buy()
        self.empty_magazine = self.prepare_empty_magazine()
        self.enemy_shot = self.prepare_enemy_shot()
        self.ship_destroyed = self.prepare_ship_destroyed()
        self.swosh = self.prepare_swosh()
        self.game_over = self.prepare_game_over()

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

    def prepare_ship_destroyed(self):
        filename = "ship_destroyed.wav"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_player_shot(self):
        filename = "player_shot.ogg"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_take_damage(self):
        filename = "take_damage.mp3"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_collect_coin(self):
        filename = "collect_coin.ogg"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_upgrade_buy(self):
        filename = "upgrade_buy.wav"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_empty_magazine(self):
        filename = "empty_magazine.wav"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_bubble_pop(self):
        filename = "bubble_pop.wav"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_enemy_shot(self):
        filename = "enemy_shot.ogg"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_swosh(self):
        filename = "swosh.flac"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound

    def prepare_game_over(self):
        filename = "game_over.wav"
        sound = pygame.mixer.Sound(os.path.join(self.data_folder, filename))
        sound.set_volume(self.sounds_volume)
        return sound
