import pygame
from enum import Enum

from Aliens import SETTINGS


class ShipState(Enum):
    ALIVE = 0
    DEAD = 1
    OUTOFLIVES = 2


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.state = ShipState.ALIVE
        # ship frames
        self.ship_frames, self.ship_frame_number = self.load_ship_frames()
        self.boost_frames, self.boost_animation_speed, self.boost_frame_number = self.load_boost_frames()
        self.explosion_frames, self.explosion_animation_speed, self.explosion_frame_number = self.load_explosion_frames()
        # sprite rect and mask
        self.rect = self.prepare_rect()
        self.real_x = self.rect.x
        self.real_y = self.rect.y
        self.image = self.get_image()
        self.mask = self.prepare_mask()
        # movement
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False
        # variables depending on ship
        self.speed = NotImplemented
        self.bullet_damage = NotImplemented
        self.health_capacity = NotImplemented
        self.current_health = NotImplemented

    def load_ship_frames(self):
        raise NotImplementedError

    def load_boost_frames(self):
        raise NotImplementedError

    def load_explosion_frames(self):
        raise NotImplementedError

    def prepare_rect(self):
        raise NotImplementedError

    def prepare_mask(self):
        mask = pygame.mask.from_surface(self.image)
        return mask

    def get_image(self):
        image = pygame.surface.Surface((0,0))
        if self.state == ShipState.ALIVE:
            image = self.boost_frames[int(self.boost_frame_number)].copy()
            image.blit(self.ship_frames[self.ship_frame_number], (0, 0))
        # ship dead
        else:
            if self.explosion_frame_number < len(self.explosion_frames):
                image = self.explosion_frames[int(self.explosion_frame_number)]
        return image

    def shot(self):
        raise NotImplementedError

    def refactor(self):
        self.ship_frames, self.ship_frame_number = self.load_ship_frames()
        self.boost_frames, self.boost_animation_speed, self.boost_frame_number = self.load_boost_frames()
        self.explosion_frames, self.explosion_animation_speed, self.explosion_frame_number = self.load_explosion_frames()

        new_x = self.rect.x * SETTINGS.SCALE
        new_y = self.rect.y * SETTINGS.SCALE
        self.rect = self.prepare_rect()
        self.rect.x = new_x
        self.rect.y = new_y
        self.image = self.get_image()
        self.mask = self.prepare_mask()

    def update(self):
        if self.state == ShipState.ALIVE:
            self.boost_frame_number += self.boost_animation_speed
            if self.boost_frame_number >= len(self.boost_frames):
                self.boost_frame_number = 0
        elif self.state == ShipState.DEAD:
            self.explosion_frame_number += self.explosion_animation_speed

        self.image = self.get_image()

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)
        # check if still alive
        if self.current_health <= 0:
            self.state = ShipState.DEAD
            return True
        # change image depending od health
        elif self.current_health <= self.health_capacity / 4:
            self.ship_frame_number = 2
            return False
        elif self.current_health <= self.health_capacity / 2:
            self.ship_frame_number = 1
            return False
        else:
            return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
