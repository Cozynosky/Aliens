import pygame
from Aliens import SETTINGS


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # prepare players image
        self.image, self.rect = self.reset_image()
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

    def reset_image(self):
        image = pygame.Surface((128 * SETTINGS.SCALE, 128 * SETTINGS.SCALE))
        image.fill('#00FF00')
        rect = image.get_rect()
        rect.center = (rect.width, SETTINGS.WINDOW_HEIGHT // 2)
        return image, rect

    def reset_player(self):
        # reset image
        self.image, self.rect = self.reset_image()
        # reset lives
        self.lives = 3
        # movement
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False

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

    def handle_events(self, events):
        for event in events:
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

