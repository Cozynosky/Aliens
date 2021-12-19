import pygame
import os.path
import random

from Aliens import SETTINGS
from Aliens.Ship.ship import Ship, ShipState
from Aliens.Bullets.easyenemy_bullet import EasyEnemyBullet


class EasyEnemy(Ship):
    def __init__(self, wave_number):
        super(EasyEnemy, self).__init__()
        self.wave_number = wave_number
        self.go_left = True
        self.dest_x, self.dest_y = self.generate_destination()

        self.speed = int(3 * SETTINGS.SCALE)
        self.hit_damage = 3
        self.health_capacity = 10
        self.current_health = 10
        self.shot_cooldown = 3
        self.time_to_shot = 3

    def load_ship_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "EasyEnemy")

        ship_frames = [pygame.image.load(os.path.join(images_folder, f"ship-{i}.png")).convert_alpha() for i in range(3)]
        rect = ship_frames[0].get_rect()
        ship_frames = [pygame.transform.smoothscale(ship_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for ship_frame in ship_frames]

        ship_frame_number = 0

        return ship_frames, ship_frame_number

    def load_boost_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "EasyEnemy")

        boost_frames = [pygame.image.load(os.path.join(images_folder, f"boost-{i}.png")).convert_alpha() for i in range(6)]
        rect = boost_frames[0].get_rect()
        boost_frames = [pygame.transform.smoothscale(boost_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for boost_frame in boost_frames]

        boost_animation_speed = 0.10
        boost_frame_number = 0

        return boost_frames, boost_animation_speed, boost_frame_number

    def load_explosion_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "EasyEnemy")

        explosion_frames = [pygame.image.load(os.path.join(images_folder, f"explode-{i}.png")).convert_alpha() for i in range(8)]
        rect = explosion_frames[0].get_rect()
        explosion_frames = [pygame.transform.smoothscale(explosion_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for
            explosion_frame in explosion_frames]

        explosion_animation_speed = 0.20
        explosion_frame_number = 0

        return explosion_frames, explosion_animation_speed, explosion_frame_number

    def prepare_rect(self):
        rect = self.ship_frames[0].get_rect()
        rect.left = SETTINGS.WINDOW_WIDTH
        rect.top = random.randint(0, int(SETTINGS.WINDOW_HEIGHT - rect.height))

        return rect

    def try_shot(self, shots):
        self.time_to_shot += 0.016
        if self.time_to_shot > self.shot_cooldown:
            shots.add(self.shot())
            self.time_to_shot = 0

    def shot(self):
        return EasyEnemyBullet(self.rect.left, self.rect.centery, 6, self.hit_damage)

    def generate_destination(self):
        dest_x, dest_y = 0, 0
        if self.wave_number <= 5 and self.go_left:
            dest_x = random.randint(SETTINGS.WINDOW_WIDTH//2, int(SETTINGS.WINDOW_WIDTH - self.rect.width))
            dest_y = 0

        return dest_x, dest_y

    def update(self):
        super(EasyEnemy, self).update()
        if self.state == ShipState.ALIVE:
            if self.wave_number <= 5:
                if self.go_left:
                    if self.rect.x > self.dest_x:
                        self.rect.x -= self.speed
                    else:
                        self.go_left = False
                        self.go_up = random.choice([True, False])
                        self.go_down = not self.go_up
                elif self.go_up:
                    if self.rect.y > 0:
                        self.rect.y -= self.speed
                    else:
                        self.go_up = False
                        self.go_down = True
                elif self.go_down:
                    if self.rect.y < SETTINGS.WINDOW_HEIGHT - self.rect.height:
                        self.rect.y += self.speed
                    else:
                        self.go_down = False
                        self.go_up = True

        elif self.state == ShipState.DEAD:
            if self.explosion_frame_number >= len(self.explosion_frames):
                self.kill()
