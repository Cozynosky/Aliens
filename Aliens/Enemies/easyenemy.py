import pygame
import os.path
import random

from Aliens import SETTINGS


class EasyEnemy(pygame.sprite.Sprite):
    def __init__(self, wave):
        pygame.sprite.Sprite.__init__(self)
        self.wave = wave
        # load images
        self.boost_frames, self.boost_frame_number, self.body_frame, self.rect, self.mask = self.load_image()
        self.rect.left = SETTINGS.WINDOW_WIDTH
        self.rect.top = random.randint(0, int(SETTINGS.WINDOW_HEIGHT - self.rect.height))
        # base dest
        self.dest_x = random.randint(SETTINGS.WINDOW_WIDTH//2, int(SETTINGS.WINDOW_WIDTH - self.rect.width))
        self.dest_y = 0
        # animation speed
        self.animation_speed = 0.15
        self.speed = int(3 * SETTINGS.SCALE)
        # movement
        self.right = False
        self.left = True
        self.up = False
        self.down = False

    def load_image(self):
        images_folder = os.path.join("Data", "Sprites", "Enemies", "EasyEnemy")
        body_frame = pygame.image.load(os.path.join(images_folder, "base.png")).convert_alpha()
        boost_frames = [
            pygame.image.load(os.path.join(images_folder, "0.png")).convert_alpha(),
            pygame.image.load(os.path.join(images_folder, "1.png")).convert_alpha(),
            pygame.image.load(os.path.join(images_folder, "2.png")).convert_alpha(),
        ]
        rect = body_frame.get_rect()
        body_frame = pygame.transform.smoothscale(body_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE))
        boost_frames = [
            body_frame,
            pygame.transform.smoothscale(boost_frames[0], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.smoothscale(boost_frames[1], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.smoothscale(boost_frames[2], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.smoothscale(boost_frames[1], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.smoothscale(boost_frames[0], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE))
        ]
        rect = body_frame.get_rect()
        mask = pygame.mask.from_surface(body_frame)
        boost_frame_number = 0
        return boost_frames, boost_frame_number, body_frame, rect, mask

    def update(self):
        # load frame
        self.boost_frame_number += self.animation_speed
        if self.boost_frame_number > len(self.boost_frames):
            self.boost_frame_number = 0

        self.image = self.body_frame.copy()
        self.image.blit(self.boost_frames[int(self.boost_frame_number)], (0, 0))

        if self.wave <= 5:
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

    def draw(self, screen):
        screen.blit(self.image, self.rect)

