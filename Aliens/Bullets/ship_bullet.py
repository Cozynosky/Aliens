import pygame
import os.path
from Aliens import SETTINGS
from Aliens.Bullets.bullet import Bullet


class ShipBullet(Bullet):
    def __init__(self, init_x, init_y, speed, hit_damage):
        super(ShipBullet, self).__init__(init_x, init_y, speed, hit_damage)
        # set moving to right
        self.go_right = True

    def load_bullet_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Bullets", "FristShip_Bullet")

        bullet_frames = [pygame.image.load(os.path.join(images_folder, f"bullet-{i}.png")).convert_alpha() for i in range(3)]
        bullet_rect = bullet_frames[0].get_rect()
        bullet_frames = [pygame.transform.smoothscale(bullet_frame, (int(bullet_rect.width * SETTINGS.SCALE), int(bullet_rect.height * SETTINGS.SCALE))) for bullet_frame in bullet_frames]

        bullet_frames_animation_speed = 0.15
        bullet_frame_number = 0

        return bullet_frames, bullet_frames_animation_speed, bullet_frame_number

    def load_explosion_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Bullets", "FristShip_Bullet")

        explosion_frames = [pygame.image.load(os.path.join(images_folder, f"explode-{i}.png")).convert_alpha() for i in range(5)]
        explosion_rect = explosion_frames[0].get_rect()
        explosion_frames = [pygame.transform.smoothscale(explosion_frame, (int(explosion_rect.width * SETTINGS.SCALE), int(explosion_rect.height * SETTINGS.SCALE))) for explosion_frame in explosion_frames]

        explosion_frames_animation_speed = 0.3
        explosion_frame_number = 0

        return explosion_frames, explosion_frames_animation_speed, explosion_frame_number
