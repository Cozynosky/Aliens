import pygame
import os.path

from Aliens import SETTINGS


class EndlessBackground:
    def __init__(self, animation_speed=0.3):
        self.animation_speed = animation_speed
        self.layers = self.load_layers(self.animation_speed)

    def load_layers(self, animation_speed):
        layers = []
        for i in range(6):
            layers.append(BackgroundLayer(f"{i}.png", (i+1) * animation_speed))
        return layers

    def reset(self):
        for layer in self.layers:
            layer.reset()

    def update(self):
        for layer in self.layers:
            layer.update()

    def refactor(self):
        self.layers = self.load_layers(self.animation_speed)

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
        self.speed = speed * SETTINGS.SCALE

    def load_image(self, filename):
        image = pygame.image.load(os.path.join(self.images_folder, filename)).convert_alpha()
        rect = image.get_rect()
        image = pygame.transform.scale(image, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE))
        rect = image.get_rect()
        rect.topleft = (0, 0)
        following_rect = rect.copy()
        following_rect.left = rect.right
        return image, rect, following_rect

    def reset(self):
        self.rect.left = 0
        self.rect_x = 0
        self.following_rect.left = self.rect.right
        self.following_rect_x = self.following_rect.x

    def update(self):
        self.rect_x -= self.speed
        self.rect.x = int(self.rect_x)
        self.following_rect_x -= self.speed
        self.following_rect.x = int(self.following_rect_x)

        if self.rect.right <= 0:
            self.rect.left = self.following_rect.right
            self.rect_x = self.rect.x
        if self.following_rect.right <= 0:
            self.following_rect.left = self.rect.right
            self.following_rect_x = self.following_rect.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.following_rect)
