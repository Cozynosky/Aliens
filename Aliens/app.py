import pygame
from Aliens.MainMenu.main_menu import MainMenu
from Aliens.GameMenu.game_menu import GameMenu
from Aliens.EndlessMode.endless_mode import EndlessMode
from Aliens.SettingsMenu.settingsmenu import SettingsMenu
from Aliens.Profile.profile import Profile
from Aliens.background import EndlessBackground
from Aliens import SETTINGS


class App:
    def __init__(self):
        # pygame setup
        pygame.init()
        pygame.display.set_caption(SETTINGS.WINDOW_TITLE)
        # screen setup
        if SETTINGS.FULLSCREEN:
            self.screen = pygame.display.set_mode((SETTINGS.WINDOW_WIDTH, SETTINGS.WINDOW_HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((SETTINGS.WINDOW_WIDTH, SETTINGS.WINDOW_HEIGHT))
        # prepare endless background
        self.background = EndlessBackground()
        # temp profile selection
        self.profiles = [Profile(), Profile(), Profile()]
        self.current_profile = self.profiles[0]
        # game setup
        self.is_running = True
        self.game_scenes = {
            MainMenu.__name__: MainMenu(self),
            GameMenu.__name__: GameMenu(self),
            EndlessMode.__name__: EndlessMode(self),
            SettingsMenu.__name__: SettingsMenu(self)
        }
        self.current_scene = self.game_scenes[MainMenu.__name__]


    def refactor_ui(self):
        # save user settings to file
        SETTINGS.save_settings()

        pygame.display.quit()
        pygame.display.init()
        pygame.display.set_caption(SETTINGS.WINDOW_TITLE)
        if SETTINGS.FULLSCREEN:
            self.screen = pygame.display.set_mode((SETTINGS.WINDOW_WIDTH, SETTINGS.WINDOW_HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((SETTINGS.WINDOW_WIDTH, SETTINGS.WINDOW_HEIGHT))
        self.background.refactor()
        for scene in self.game_scenes.values():
            scene.refactor_ui()

    def run(self):
        while self.is_running:
            self.current_scene.update()
            self.current_scene.render(self.screen)
            self.current_scene.handle_events(pygame.event.get())
