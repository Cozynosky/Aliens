import pygame
import os.path
import random

from Aliens import SETTINGS
from enum import Enum


class EnemyState(Enum):
    ALIVE = 0
    DEAD = 1


class EasyEnemy(pygame.sprite.Sprite):
    def __init__(self, wave_number):
        pygame.sprite.Sprite.__init__(self)
        self.wave_number = wave_number
        # load images
        self.boost_frames, self.body_frames, self.explosion_frames, self.rect, self.mask = self.load_image()
        self.body_frame_number = 0
        self.boost_frame_number = 0
        self.explosion_frame_number = 0
        # place rect
        self.rect.left = SETTINGS.WINDOW_WIDTH
        self.rect.top = random.randint(0, int(SETTINGS.WINDOW_HEIGHT - self.rect.height))
        # base dest
        self.dest_x = random.randint(SETTINGS.WINDOW_WIDTH//2, int(SETTINGS.WINDOW_WIDTH - self.rect.width))
        self.dest_y = 0
        # animation speed
        self.animation_speed = 0.15
        self.explosion_animation_speed = 0.20
        self.speed = int(3 * SETTINGS.SCALE)
        # health
        self.health_capacity = 10
        self.current_health = self.health_capacity
        # movement
        self.right = False
        self.left = True
        self.up = False
        self.down = False
        # state
        self.state = EnemyState.ALIVE

    def load_image(self):
        images_folder = os.path.join("Data", "Sprites", "Enemies", "EasyEnemy")

        # load body frames
        body_frames = [pygame.image.load(os.path.join(images_folder, f"ship-{i}.png")).convert_alpha() for i in range(3)]
        rect = body_frames[0].get_rect()
        body_frames = [pygame.transform.smoothscale(body_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for body_frame in body_frames]

        # load boost images
        boost_frames = [pygame.image.load(os.path.join(images_folder, f"boost-{i}.png")).convert_alpha() for i in range(3)]
        boost_frames = [body_frames[0]] + [pygame.transform.smoothscale(boost_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for boost_frame in boost_frames]

        # load explosion images
        explosion_frames = [pygame.image.load(os.path.join(images_folder, f"explode-{i}.png")).convert_alpha() for i in range(8)]
        explosion_frames = [pygame.transform.smoothscale(explosion_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for
            explosion_frame in explosion_frames]

        rect = body_frames[0].get_rect()
        mask = pygame.mask.from_surface(body_frames[0])
        return boost_frames, body_frames, explosion_frames, rect, mask

    def update(self):
        if self.state == EnemyState.ALIVE:
            # increase boost animation
            self.boost_frame_number += self.animation_speed
            if self.boost_frame_number > len(self.boost_frames):
                self.boost_frame_number = 0
            # load frame
            self.image = self.boost_frames[int(self.boost_frame_number)].copy()
            self.image.blit(self.body_frames[self.body_frame_number], (0, 0))

            # moving mechanics depending on wave
            if self.wave_number <= 5:
                if self.left:
                    if self.rect.x > self.dest_x:
                        self.rect.x -= self.speed
                    else:
                        self.left = False
                        self.up = random.choice([True, False])
                        self.down = not self.up
                elif self.up:
                    if self.rect.y > 0:
                        self.rect.y -= self.speed
                    else:
                        self.up = False
                        self.down = True
                elif self.down:
                    if self.rect.y < SETTINGS.WINDOW_HEIGHT - self.rect.height:
                        self.rect.y += self.speed
                    else:
                        self.down = False
                        self.up = True

        elif self.state == EnemyState.DEAD:
            self.image = self.explosion_frames[int(self.explosion_frame_number)]
            self.explosion_frame_number += self.explosion_animation_speed
            if self.explosion_frame_number > len(self.explosion_frames):
                self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def got_hit(self, damage):
        self.current_health -= damage
        # check if still alive
        if self.current_health <= 0:
            self.state = EnemyState.DEAD
            return True
        # change image depending od health
        elif self.current_health <= self.health_capacity/4:
            self.body_frame_number = 2
            return False
        elif self.current_health <= self.health_capacity/2:
            self.body_frame_number = 1
            return False
        else:
            return False
