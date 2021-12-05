import pygame
from Aliens.Menu.main_menu import MainMenu
from Aliens.GameMenu.game_menu import GameMenu
from Aliens.EndlessMode.endless_mode import EndlessMode
from Aliens.settings import *


class App:
    def __init__(self):
        # pygame setup
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        # game setup
        self.is_running = True
        self.game_scenes = {
            MainMenu.__name__: MainMenu(self),
            GameMenu.__name__: GameMenu(self),
            EndlessMode.__name__: EndlessMode(self)
        }
        self.current_scene = self.game_scenes[MainMenu.__name__]

    def run(self):
        while self.is_running:
            self.current_scene.update()
            self.current_scene.render(self.screen)
            self.current_scene.handle_events(pygame.event.get())
