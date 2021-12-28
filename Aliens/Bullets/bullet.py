import pygame
from Aliens import SETTINGS
from enum import Enum


class BulletState(Enum):
    ALIVE = 0
    DEAD = 1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y, speed, hit_damage):
        pygame.sprite.Sprite.__init__(self)
        self.state = BulletState.ALIVE
        self.bullet_frames, self.bullet_frames_animation_speed, self.bullet_frame_number = self.load_bullet_frames()
        self.explosion_frames, self.explosion_frames_animation_speed, self.explosion_frame_number = self.load_explosion_frames()
        self.rect = self.prepare_rect(init_x, init_y)
        self.bullet_masks = self.prepare_masks()
        self.current_mask = self.get_mask()
        self.image = self.get_image()
        # movement
        self.go_right = False
        self.go_left = False
        self.speed = speed
        self.hit_damage = hit_damage

    def load_bullet_frames(self):
        raise NotImplementedError

    def load_explosion_frames(self):
        raise NotImplementedError

    def prepare_masks(self):
        masks = [pygame.mask.from_surface(self.bullet_frames[i]) for i in range(len(self.bullet_frames))]
        return masks

    def get_mask(self):
        mask = self.bullet_masks[int(self.bullet_frame_number)]
        return mask

    def prepare_rect(self, x, y):
        rect = self.bullet_frames[0].get_rect()
        rect.topleft = (x, y)
        return rect

    def get_image(self):
        image = None
        if self.state == BulletState.ALIVE:
            if self.bullet_frame_number > len(self.bullet_frames):
                self.bullet_frame_number = 0
            image = self.bullet_frames[int(self.bullet_frame_number)]
        # if dead
        else:
            if self.explosion_frame_number > len(self.explosion_frames):
                self.kill()
            else:
                image = self.explosion_frames[int(self.explosion_frame_number)]
        return image

    def update(self):
        self.image = self.get_image()
        if self.state == BulletState.ALIVE:
            self.current_mask = self.get_mask()
            self.bullet_frame_number += self.bullet_frames_animation_speed

            if self.go_left:
                self.rect.x -= self.speed
                if self.rect.right < 0:
                    self.kill()

            elif self.go_right:
                self.rect.x += self.speed
                if self.rect.left > SETTINGS.WINDOW_WIDTH:
                    self.kill()

        elif self.state == BulletState.DEAD:

            self.explosion_frame_number += self.explosion_frames_animation_speed

    def ship_hit(self):
        self.state = BulletState.DEAD
