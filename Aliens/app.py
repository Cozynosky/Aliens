import pygame
from Aliens.MainMenuScene.mainmenuscene import MainMenuScene
from Aliens.GameMenuScene.gamemenuscene import GameMenuScene
from Aliens.EndlessModeScene.endlessmodescene import EndlessModeScene
from Aliens.SettingsScene.settingsscene import SettingsScene
from Aliens.StatisticsScene.statisticsscene import StatisticsScene
from Aliens.Profile.load_profiles import load_profiles
from Aliens.Profile.save_profiles import save_profiles
from Aliens.ProfilesScene.profilesscene import ProfileScene
from Aliens.background import EndlessBackground
from Aliens import SETTINGS
from sys import exit


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
        self.profiles = load_profiles()
        self.current_profile = self.profiles[0]
        self.profile_selected = False
        # game setup
        self.is_running = True
        self.game_scenes = {
            MainMenuScene.__name__: MainMenuScene(self),
            ProfileScene.__name__: ProfileScene(self),
            GameMenuScene.__name__: GameMenuScene(self),
            EndlessModeScene.__name__: EndlessModeScene(self),
            SettingsScene.__name__: SettingsScene(self),
            StatisticsScene.__name__: StatisticsScene(self)
        }
        self.current_scene = self.game_scenes[MainMenuScene.__name__]
        self.previous_scene = self.current_scene

    def close_app(self):
        save_profiles(self.profiles)
        self.is_running = False
        pygame.quit()
        exit()

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
