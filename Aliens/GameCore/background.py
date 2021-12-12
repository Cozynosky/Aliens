import pygame
import os.path

from Aliens import SETTINGS


class EndlessBackground:
    def __init__(self):
        self.layers = self.load_layers()

    def load_layers(self):
        layers = []
        for i in range(6):
            layers.append(BackgroundLayer(f"{i}.png", i+1))
        return layers

    def update(self):
        for layer in self.layers:
            layer.update()

    def refactor(self):
        self.layers = self.load_layers()

    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)


class BackgroundLayer:
    images_folder = os.path.join("Data", "Sprites", "Background")

    def __init__(self, filename, speed):
        self.image, self.rect, self.following_rect = self.load_image(filename)
        self.rect_x = self.rect.x
        self.rect_y = self.rect.y
        self.following_rect_x = self.following_rect.x
        self.following_rect_y = self.following_rect.y
        self.speed = (speed * SETTINGS.SCALE)

    def load_image(self, filename):
        image = pygame.image.load(os.path.join(self.images_folder, filename)).convert_alpha()
        rect = image.get_rect()
        scale = SETTINGS.WINDOW_HEIGHT / rect.height
        image = pygame.transform.scale(image, (rect.width * scale, rect.height * scale))
        rect = image.get_rect()
        rect.topleft = (0, 0)
        following_rect = rect.copy()
        following_rect.left = rect.right
        return image, rect, following_rect

    def update(self):
        self.rect_x -= self.speed
        self.rect.x = round(self.rect_x)
        self.following_rect_x -= self.speed
        self.following_rect.x = round(self.following_rect_x)

        if self.rect.right <= 0:
            self.rect.left = self.following_rect.right
            self.rect_x = self.rect.x
        if self.following_rect.right <= 0:
            self.following_rect.left = self.rect.right
            self.following_rect_x = self.following_rect.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.following_rect)
