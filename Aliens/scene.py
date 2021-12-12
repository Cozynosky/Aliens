import pygame


class Scene:
    def __init__(self, parent):
        pygame.init()
        self.app = parent
        self.clock = pygame.time.Clock()

    def update(self):
        raise NotImplementedError

    def refactor_ui(self):
        raise NotImplementedError

    def render(self, screen):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError
