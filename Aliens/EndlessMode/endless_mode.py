import pygame
from sys import exit
from Aliens.scene import Scene
from Aliens.GameCore.gamecore import Game


class EndlessMode(Scene):
    def __init__(self, parent):
        super(EndlessMode, self).__init__(parent)
        self.game = Game(game_mode="ENDLESS", ship=self.app.current_profile.ship)

    def refactor_ui(self):
        self.game.refactor()

    def update(self):
        self.app.background.update()
        self.game.update()

    def render(self, screen):
        self.app.background.draw(screen)
        self.game.draw(screen)
        pygame.display.update()

    def handle_events(self, events):
        self.clock.tick(60)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.reset()
                    self.app.current_scene = self.app.game_scenes["GameMenu"]
            self.game.handle_event(event)
