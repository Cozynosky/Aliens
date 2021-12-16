import pygame
import os.path
from Aliens import SETTINGS


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y):
        super(Bullet, self).__init__()
        self.bullet_frames, self.explosion_frames, self.rect, self.masks = self.load_image()
        self.frame = 0
        self.rect.topleft = (x, y)
        self.speed = int(speed * SETTINGS.SCALE)
        self.animation_speed = 0.15
        self.hit = False

    def load_image(self):
        images_folder = os.path.join("Data", "Sprites", "Bullets", "FristShip_Bullet")

        # load and scale bullet frames
        bullet_frames = [pygame.image.load(os.path.join(images_folder, f"bullet-{i}.png")).convert_alpha() for i in range(3)]
        bullet_rect = bullet_frames[0].get_rect()
        bullet_frames = [pygame.transform.smoothscale(bullet_frame, (bullet_rect.width * SETTINGS.SCALE, bullet_rect.height * SETTINGS.SCALE)) for bullet_frame in bullet_frames]

        # load and scale explosion frames
        explosion_frames = [pygame.image.load(os.path.join(images_folder, f"explode-{i}.png")).convert_alpha() for i in range(5)]
        explosion_rect = explosion_frames[0].get_rect()
        explosion_frames = [pygame.transform.smoothscale(explosion_frame, (explosion_rect.width * SETTINGS.SCALE, explosion_rect.height * SETTINGS.SCALE)) for explosion_frame in explosion_frames]

        masks = [pygame.mask.from_surface(bullet_frames[i]) for i in range(3)]

        bullet_rect = bullet_frames[0].get_rect()
        return bullet_frames, explosion_frames, bullet_rect, masks

    def update(self):
        if self.hit:
            self.image = self.explosion_frames[int(self.frame)]

            self.frame += self.animation_speed
            if self.frame > len(self.explosion_frames):
                self.kill()

        else:
            self.image = self.bullet_frames[int(self.frame)]
            self.mask = self.masks[int(self.frame)]

            self.frame += self.animation_speed
            if self.frame > len(self.bullet_frames):
                self.frame = 0

            self.rect.x += self.speed
            if self.rect.x > SETTINGS.WINDOW_WIDTH:
                self.kill()

    def enemy_hit(self):
        if self.hit is False:
            self.frame = 0
            self.hit = True
            self.animation_speed = 0.3
