import pygame
from Aliens import SETTINGS


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # init needed values
        self.frames = None
        self.frame = None
        self.animation_speed = None
        self.vertical_speed = None
        self.horizontal_speed = None
        # movement
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False

    def refactor(self):
        raise NotImplementedError

    def load_image(self):
        raise NotImplementedError

    def reset_ship(self):
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False
        self.rect.center = (self.rect.width, SETTINGS.WINDOW_HEIGHT // 2)

    def update(self):
        # movement
        if self.go_left and self.rect.left > 0:
            self.rect.x -= self.horizontal_speed
        if self.go_right and self.rect.right < SETTINGS.WINDOW_WIDTH:
            self.rect.x += self.horizontal_speed
        if self.go_up and self.rect.top > 0:
            self.rect.y -= self.vertical_speed
        if self.go_down and self.rect.bottom < SETTINGS.WINDOW_HEIGHT:
            self.rect.y += self.vertical_speed

        # animation
        self.frame += self.animation_speed
        if self.frame > len(self.frames):
            self.frame = 0

    def shot(self):
        raise NotImplementedError

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.go_up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.go_down = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.go_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.go_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.go_up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.go_down = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.go_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.go_right = False

    def draw(self, screen):
        raise NotImplementedError
