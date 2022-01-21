import pygame
import os.path
import random

from Aliens import SETTINGS, SOUNDS
from Aliens.Ship.ship import Ship, ShipState
from Aliens.Bullets.easyenemy_bullet import EasyEnemyBullet


class EasyEnemy(Ship):
    def __init__(self, wave_number):
        super(EasyEnemy, self).__init__()
        self.wave_number = wave_number
        self.dest_x = self.generate_x_destination()
        self.dest_y = 0
        self.go_left = True

        self.speed = self.get_speed()
        self.bullet_speed = self.get_bullet_speed()
        self.hit_damage = self.get_hit_damage()
        self.health_capacity = self.get_health_capacity()
        self.current_health = self.health_capacity
        self.shot_cooldown = self.get_shoot_cooldown()
        self.time_to_shot = self.get_time_to_shoot()

    def refactor(self):
        super(EasyEnemy, self).refactor()
        self.speed = self.get_speed()
        self.bullet_speed = self.get_bullet_speed()
        self.dest_y *= SETTINGS.SCALE
        self.dest_x *= SETTINGS.SCALE

    def get_speed(self):
        # WAVE, VALUE: 1, 2 -> 5, 2.2 -> 10, 2.5 -> 20, 3 -> 50, 6
        speed = 0.0119337 * self.wave_number ** 1.48289 + 2.04706
        # make max speed value
        speed = min(8, speed)
        return speed * SETTINGS.SCALE

    def get_bullet_speed(self):
        # WAVE, VALUE: 1, 4 -> 5, 4.5 -> 10, 6 -> 20, 10 -> 50, 22
        bullet_speed = 0.168918 * self.wave_number ** 1.2 + 3.57386
        # make max bullet speed
        bullet_speed = min(24, bullet_speed)
        return bullet_speed

    def get_hit_damage(self):
        # WAVE, VALUE: 1, 3 -> 5, 4 -> 10, 7 -> 20, 15-> 50, 40
        hit_damage = 0.311198 * self.wave_number ** 1.22737 + 2.20444
        return round(hit_damage, 2)

    def get_health_capacity(self):
        # WAVE, VALUE: 1, 10 -> 5, 15-> 10, 22-> 20, 50 -> 50, 140
        health_capacity = 0.814922 * self.wave_number ** 1.30038 + 8.25383
        return round(health_capacity, 2)

    def get_shoot_cooldown(self):
        # WAVE, VALUE: 1, 4 -> 5, 3.9 -> 10, 3.7 -> 20, 3.5 -> 50, 2.5
        cooldown = 4.00704 - 0.0196861 * self.wave_number ** 1.108
        cooldown = max(cooldown, 0.5)
        cooldown = random.uniform(cooldown, cooldown * 2)
        return cooldown

    def get_time_to_shoot(self):
        return self.shot_cooldown

    def load_ship_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "EasyEnemy")

        ship_frames = [pygame.image.load(os.path.join(images_folder, f"ship-{i}.png")).convert_alpha() for i in
                       range(3)]
        rect = ship_frames[0].get_rect()
        ship_frames = [
            pygame.transform.smoothscale(ship_frame, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE))) for
            ship_frame in ship_frames]

        ship_frame_number = 0

        return ship_frames, ship_frame_number

    def load_boost_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "EasyEnemy")

        boost_frames = [pygame.image.load(os.path.join(images_folder, f"boost-{i}.png")).convert_alpha() for i in
                        range(6)]
        rect = boost_frames[0].get_rect()
        boost_frames = [
            pygame.transform.smoothscale(boost_frame, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE))) for
            boost_frame in boost_frames]

        boost_animation_speed = 0.10
        boost_frame_number = 0

        return boost_frames, boost_animation_speed, boost_frame_number

    def load_explosion_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "EasyEnemy")

        explosion_frames = [pygame.image.load(os.path.join(images_folder, f"explode-{i}.png")).convert_alpha() for i in
                            range(8)]
        rect = explosion_frames[0].get_rect()
        explosion_frames = [
            pygame.transform.smoothscale(explosion_frame, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE)))
            for explosion_frame in explosion_frames]

        explosion_animation_speed = 0.20
        explosion_frame_number = 0

        return explosion_frames, explosion_animation_speed, explosion_frame_number

    def prepare_rect(self):
        rect = self.ship_frames[0].get_rect()
        rect.left = SETTINGS.WINDOW_WIDTH
        rect.top = random.randint(0, round(SETTINGS.WINDOW_HEIGHT - rect.height))

        return rect

    def try_shot(self, shots):
        self.time_to_shot += 0.016
        if self.time_to_shot > self.shot_cooldown:
            SOUNDS.enemy_shot.play()
            shots.add(self.shot())
            self.time_to_shot = 0

    def shot(self):
        return EasyEnemyBullet(self.rect.left, self.rect.centery, self.bullet_speed, self.hit_damage)

    def generate_x_destination(self):

        dest_x = random.randint(SETTINGS.WINDOW_WIDTH // 2, round(SETTINGS.WINDOW_WIDTH - self.rect.width))

        return dest_x

    def generate_y_destination(self):

        if self.wave_number <= 10:
            dest_y = random.choice([0, round(SETTINGS.WINDOW_HEIGHT - self.rect.height)])
        else:
            dest_y = random.randint(0, round(SETTINGS.WINDOW_HEIGHT - self.rect.height))

        if self.rect.y > dest_y:
            self.go_up = True
        else:
            self.go_up = False
        self.go_down = not self.go_up

        return dest_y

    def update(self):
        super(EasyEnemy, self).update()
        if self.state == ShipState.ALIVE:
            if self.go_left:
                if self.rect.x > self.dest_x:
                    self.real_x -= self.speed
                else:
                    self.go_left = False
                    self.dest_y = self.generate_y_destination()
            else:
                if self.go_up:
                    if self.rect.y > self.dest_y:
                        self.real_y -= self.speed
                    else:
                        self.dest_y = self.generate_y_destination()
                elif self.go_down:
                    if self.rect.y < self.dest_y:
                        self.real_y += self.speed
                    else:
                        self.dest_y = self.generate_y_destination()

                if self.wave_number > 20:
                    if self.rect.right < 0:
                        self.rect.left = SETTINGS.WINDOW_WIDTH
                        self.real_x = self.rect.left

                    self.real_x -= 0.5 * SETTINGS.SCALE

        elif self.state == ShipState.DEAD:
            if self.explosion_frame_number >= len(self.explosion_frames):
                self.kill()
