import pygame
from datetime import datetime
from Aliens.scene import Scene
from Aliens.EndlessGameCore.gamecore import Game
from Aliens.EndlessGameCore.gamecore import GameState
from Aliens.EndlessModeScene.pause_scene import PauseScene
from Aliens.EndlessModeScene.gameover_scene import GameOverScene


class EndlessModeScene(Scene):
    def __init__(self, parent):
        super(EndlessModeScene, self).__init__(parent)
        self.game = Game(scene=self)
        self.pause_scene = PauseScene(self)
        self.game_over_scene = GameOverScene(self.game)

    def refactor_ui(self):
        self.game.refactor()
        self.pause_scene.refactor_ui()
        self.game_over_scene.refactor_ui()

    def update(self):
        super(EndlessModeScene, self).update()
        self.game.update()

    def render(self, screen):
        self.app.background.draw(screen)
        self.game.draw(screen)
        if self.game.paused:
            self.pause_scene.render(screen)
        if self.game.state == GameState.GAME_OVER:
            self.game_over_scene.render(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                self.game.end_time = datetime.now()
                self.game.save_progress()
                self.app.close_app()
            self.game.handle_event(event)

            if self.game.state == GameState.GAME_OVER:
                self.game_over_scene.handle_events(event)

            if self.game.paused:
                self.pause_scene.handle_events(event)

        if self.game.paused:
            self.pause_scene.manager.update(time_delta)

        if self.game.state == GameState.GAME_OVER:
            self.game_over_scene.manager.update(time_delta)
