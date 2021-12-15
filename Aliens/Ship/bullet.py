import pygame
import os.path
from Aliens import SETTINGS


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y):
        super(Bullet, self).__init__()
        self.frames, self.frame, self.rect = self.load_image()
        self.image = self.frames[self.frame]
        self.rect.topleft = (x, y)
        self.speed = int (speed * SETTINGS.SCALE)
        self.animation_speed = 0.15

    def load_image(self):
        images_folder = os.path.join("Data", "Sprites", "Bullets", "Bullet1")
        frames = [
            pygame.image.load(os.path.join(images_folder, "0.png")).convert_alpha(),
            pygame.image.load(os.path.join(images_folder, "1.png")).convert_alpha(),
            pygame.image.load(os.path.join(images_folder, "2.png")).convert_alpha(),

        ]
        rect = frames[0].get_rect()
        frames = [
            pygame.transform.scale(frames[0], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.scale(frames[1], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.scale(frames[2], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
        ]
        rect = frames[0].get_rect()
        rect.center = (rect.width, SETTINGS.WINDOW_HEIGHT // 2)
        frame = 0
        return frames, frame, rect

    def update(self):
        self.frame += self.animation_speed
        if self.frame > len(self.frames):
            self.frame = 0

        self.image = self.frames[int(self.frame)]

        self.rect.x += self.speed
        if self.rect.x > SETTINGS.WINDOW_WIDTH:
            self.kill()
