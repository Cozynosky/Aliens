import pygame
from Aliens import SETTINGS


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # prepare players image
        self.image = pygame.Surface((64, 64))
        self.image.fill('#00FF00')
        self.rect = self.image.get_rect()
        # lifes
        self.lives = 3
        self.reset_player()
        # player speed
        self.horizontal_speed = 6
        self.vertical_speed = 6
        # movement
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False

    def reset_player(self):
        self.rect.center = (self.rect.width, SETTINGS.WINDOW_HEIGHT // 2)
        self.lives = 3
        # movement
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False

    def update(self) -> None:
        # movement
        if self.go_left and self.rect.left > 0:
            self.rect.x -= self.horizontal_speed
        if self.go_right and self.rect.right < SETTINGS.WINDOW_WIDTH:
            self.rect.x += self.horizontal_speed
        if self.go_up and self.rect.top > 0:
            self.rect.y -= self.vertical_speed
        if self.go_down and self.rect.bottom < SETTINGS.WINDOW_HEIGHT:
            self.rect.y += self.vertical_speed
