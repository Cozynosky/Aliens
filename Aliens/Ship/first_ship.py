import pygame
import os.path
from Aliens.Ship.ship import Ship
from Aliens.Ship.bullet import Bullet
from Aliens import SETTINGS


class FirstShip(Ship):
    def __init__(self):
        super().__init__()
        # ship speed
        self.horizontal_speed = int(8 * SETTINGS.SCALE)
        self.vertical_speed = int(8 * SETTINGS.SCALE)
        # animation speed
        self.animation_speed = 0.15
        # magazine
        self.magazine_size = 0
        self.shots = pygame.sprite.Group()

    def refactor(self):
        super(FirstShip, self).refactor()
        self.horizontal_speed = 8 * SETTINGS.SCALE
        self.vertical_speed = 8 * SETTINGS.SCALE

    def load_image(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")
        frames = [
            pygame.image.load(os.path.join(images_folder, "vehicle-1.png")).convert_alpha(),
            pygame.image.load(os.path.join(images_folder, "vehicle-2.png")).convert_alpha(),
            pygame.image.load(os.path.join(images_folder, "vehicle-3.png")).convert_alpha(),
            pygame.image.load(os.path.join(images_folder, "vehicle-2.png")).convert_alpha()
        ]
        rect = frames[0].get_rect()
        frames = [
            pygame.transform.scale(frames[0], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.scale(frames[1], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.scale(frames[2], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)),
            pygame.transform.scale(frames[1], (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE))
        ]
        rect = frames[0].get_rect()
        rect.center = (rect.width, SETTINGS.WINDOW_HEIGHT // 2)
        frame = 0
        return frames, frame, rect

    def shot(self):
        self.shots.add(Bullet(10, self.rect.right, self.rect.centery))

    def update(self):
        super(FirstShip, self).update()
        self.shots.update()

    def draw(self, screen):
        super(FirstShip, self).draw(screen)
        self.shots.draw(screen)

    def handle_event(self, event):
        super(FirstShip, self).handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shot()
