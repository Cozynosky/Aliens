import pygame
from enum import Enum


class ShipState(Enum):
    ALIVE = 0
    DEAD = 1


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
        self.image = self.get_image()
        self.mask = self.prepare_mask()
        # movement
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False
        # variables depending on ship
        self.speed = NotImplemented
        self.hit_damage = NotImplemented
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
        image = None
        if self.state == ShipState.ALIVE:
            if self.boost_frame_number >= len(self.boost_frames):
                self.boost_frame_number = 0
            image = self.boost_frames[int(self.boost_frame_number)].copy()
            image.blit(self.ship_frames[self.ship_frame_number], (0, 0))
        # ship dead
        else:
            if self.explosion_frame_number >= len(self.explosion_frames):
                self.kill()
            else:
                image = self.explosion_frames[int(self.explosion_frame_number)]
        return image

    def shot(self):
        raise NotImplementedError

    def refactor(self):
        self.ship_frames, self.ship_frame_number = self.load_ship_frames()
        self.boost_frames, self.boost_animation_speed, self.boost_frame_number = self.load_boost_frames()
        self.explosion_frames, self.explosion_animation_speed, self.explosion_frame_number = self.load_explosion_frames()

    def update(self):
        self.image = self.get_image()

        if self.state == ShipState.ALIVE:
            self.boost_frame_number += self.boost_animation_speed
        elif self.state == ShipState.DEAD:
            self.explosion_frame_number += self.explosion_animation_speed

    def take_damage(self, damage):
        self.current_health -= damage
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