import pygame
from sys import exit
from Aliens.scene import Scene
from Aliens.EndlessGameCore.gamecore import Game
from Aliens.EndlessGameCore.gamecore import GameState
from Aliens.EndlessModeMenu.pause_scene import PauseScene


class EndlessMode(Scene):
    def __init__(self, parent):
        super(EndlessMode, self).__init__(parent)
        self.game = Game(profile=self.app.current_profile, scene=self)
        self.pause_scene = PauseScene(self.game)

    def refactor_ui(self):
        self.game.refactor()
        self.pause_scene.refactor_ui()

    def update(self):
        if self.game.paused:
            self.pause_scene.update()
        else:
            if self.game.state == GameState.GAME_ON:
                self.game.update()
            elif self.game.state == GameState.GAME_OFF:
                pygame.mouse.set_visible(True)
                self.app.current_scene = self.app.game_scenes["GameMenu"]

    def render(self, screen):
        self.app.background.draw(screen)
        self.game.draw(screen)
        if self.game.paused:
            self.pause_scene.render(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_visible(True)
                    self.game.paused = not self.game.paused
            self.game.handle_event(event)

            if self.game.paused:
                self.pause_scene.handle_events(event)

        if self.game.paused:
            self.pause_scene.manager.update(time_delta)
