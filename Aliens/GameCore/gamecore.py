import pygame

from Aliens.GameCore.player import Player
from Aliens.GameCore.background import EndlessBackground


class Game:
    def __init__(self, game_mode):
        self.game_mode = game_mode
        # init player class
        self.player = Player()
        # setup background
        self.background = EndlessBackground()

    def refactor(self):
        self.background.refactor()
        self.player.refactor()

    def new_game(self):
        self.player.reset_player()

    def update(self):
        self.background.update()
        self.player.update()

    def draw(self, screen):
        self.background.draw(screen)
        self.player.draw(screen)

    def handle_events(self, events):
        self.player.handle_events(events)
