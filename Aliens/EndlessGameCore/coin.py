import pygame
import os.path
import random

from Aliens import SETTINGS


class Coin(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.coin_frames, self.coin_frames_animation_speed, self.coin_frame_number = self.load_coin_frames()
        self.rect = self.prepare_rect(init_x, init_y)
        self.coin_masks = self.prepare_masks()
        self.image = self.get_image()
        self.mask = self.get_mask()
        self.speed = round(1 * SETTINGS.SCALE)

    def refactor(self):
        pass

    def load_coin_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Coins")

        coin_frames = [pygame.image.load(os.path.join(images_folder, f"coin-{i}.png")).convert_alpha() for i in range(8)]
        coin_rect = coin_frames[0].get_rect()
        coin_frames = [pygame.transform.smoothscale(bullet_frame, (coin_rect.width * SETTINGS.SCALE, coin_rect.height * SETTINGS.SCALE)) for bullet_frame in coin_frames]

        coin_frames_animation_speed = 0.1
        coin_frame_number = 0

        return coin_frames, coin_frames_animation_speed, coin_frame_number

    def prepare_rect(self, init_x, init_y):
        rect = self.coin_frames[0].get_rect()
        rect.x = init_x
        rect.y = init_y
        return rect

    def prepare_masks(self):
        masks = [pygame.mask.from_surface(self.coin_frames[i]) for i in range(len(self.coin_frames))]
        return masks

    def get_mask(self):
        mask = self.coin_masks[int(self.coin_frame_number)]
        return mask

    def get_image(self):
        if self.coin_frame_number > len(self.coin_frames):
            self.coin_frame_number = 0

        image = self.coin_frames[int(self.coin_frame_number)]
        return image

    def update(self):
        self.image = self.get_image()
        self.mask = self.get_mask()
        self.coin_frame_number += self.coin_frames_animation_speed

        self.rect.left -= self.speed

        if self.rect.right < 0:
            self.kill()

    @staticmethod
    def drop_coin(drop_rate, coins, init_x, init_y):
        chance = random.random()
        if chance <= drop_rate:
            coins.add(Coin(init_x, init_y))
