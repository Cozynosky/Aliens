import pygame
from Aliens.GameMenu.main_menu import MainMenu
from Aliens.constraints import *

game_scenes = {
    MainMenu.__name__: MainMenu()
}


class App:
    def __init__(self):
        # pygame setup
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        # game setup
        self.is_running = True
        self.current_scene = game_scenes[MainMenu.__name__]

    def run(self):
        while self.is_running:
            self.current_scene.update()
            self.current_scene.render(self.screen)
            self.current_scene.handle_events(pygame.event.get())
