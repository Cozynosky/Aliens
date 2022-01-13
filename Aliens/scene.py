import pygame
import pygame_gui
from Aliens import SETTINGS


class Scene:
    def __init__(self, parent):
        pygame.init()
        self.app = parent
        self.clock = pygame.time.Clock()
        self.manager = self.prepare_manager()

    def prepare_manager(self):
        return pygame_gui.UIManager(SETTINGS.WINDOW_SIZE, 'Data/default_theme.json')

    def update(self):
        self.app.background.update()

    def refactor_ui(self):
        raise NotImplementedError

    def render(self, screen):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
