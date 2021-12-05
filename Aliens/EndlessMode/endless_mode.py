import pygame
from sys import exit
from Aliens.scene import Scene
from Aliens.settings import *
from Aliens.EndlessMode.player import Player


class EndlessMode(Scene):
    def __init__(self, parent):
        super(EndlessMode, self).__init__(parent)
        self.player = Player()
        self.background = pygame.Surface(WINDOW_SIZE)
        self.background.fill(pygame.Color('#DDDDDD'))

    def update(self):
        self.player.update()

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.player.image, self.player.rect)
        pygame.display.update()

    def handle_events(self, events):
        self.clock.tick(60)
        for event in events:

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.go_up = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.go_down = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.go_left = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.go_right = True
                if event.key == pygame.K_ESCAPE:
                    self.reset_game()
                    self.app.previous_scene = self.app.game_scenes[EndlessMode.__name__]
                    self.app.current_scene = self.app.game_scenes['GameMenu']

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.player.go_up = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.player.go_down = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.go_left = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.go_right = False

    def reset_game(self):
        self.player.reset_player()
