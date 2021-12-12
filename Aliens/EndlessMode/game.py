import pygame

from Aliens import SETTINGS
from Aliens.EndlessMode.player import Player


class Game:
    def __init__(self):
        # init player class
        self.player = Player()
        # setup background
        self.background = self.prepare_background()

    def new_game(self):
        self.player.reset_player()
        self.background = self.prepare_background()

    def prepare_background(self):
        background = pygame.Surface(SETTINGS.WINDOW_SIZE)
        background.fill(pygame.Color('#DDDDDD'))
        return background

    def update(self):
        self.player.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.player.image, self.player.rect)

    def handle_events(self, events):
        self.player.handle_events(events)
