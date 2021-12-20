import pygame
import os.path
from Aliens import SETTINGS
from Aliens.Ship.ship import Ship, ShipState
from Aliens.Bullets.ship_bullet import ShipBullet


class FirstShip(Ship):
    def __init__(self):
        super(FirstShip, self).__init__()

        self.speed = int(7 * SETTINGS.SCALE)
        self.hit_damage = 5
        self.health_capacity = 10
        self.current_health = 10
        self.lives = 3

        self.magazine_size = 3
        self.in_magazine = 3
        self.reload_time = 1                   # in seconds
        self.to_reload = self.reload_time       # in seconds
        self.reloading = False

    def new_game(self):
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False
        self.health_capacity = 10
        self.hit_damage = 5
        self.magazine_size = 3
        self.lives = 3
        self.reload_time = 1

        self.reset()

        self.speed = int(7 * SETTINGS.SCALE)

    def reset(self):
        self.state = ShipState.ALIVE
        self.current_health = self.health_capacity
        self.in_magazine = 3
        self.to_reload = self.reload_time
        self.reloading = False

        self.ship_frame_number = 0
        self.explosion_frame_number = 0
        self.boost_frame_number = 0
        self.rect = self.prepare_rect()

    def refactor(self):
        super(FirstShip, self).refactor()
        self.speed = int(7 * SETTINGS.SCALE)

    def load_ship_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")

        ship_frames = [pygame.image.load(os.path.join(images_folder, f"ship-{i}.png")).convert_alpha() for i in range(3)]
        rect = ship_frames[0].get_rect()
        ship_frames = [pygame.transform.smoothscale(ship_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for ship_frame in ship_frames]

        ship_frame_number = 0

        return ship_frames, ship_frame_number

    def load_boost_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")

        boost_frames = [pygame.image.load(os.path.join(images_folder, f"boost-{i}.png")).convert_alpha() for i in range(3)]
        rect = boost_frames[0].get_rect()
        boost_frames = [pygame.transform.smoothscale(boost_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for boost_frame in boost_frames]

        boost_animation_speed = 0.15
        boost_frame_number = 0

        return boost_frames, boost_animation_speed, boost_frame_number

    def load_explosion_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")

        boost_frames = [pygame.image.load(os.path.join(images_folder, f"explode-{i}.png")).convert_alpha() for i in range(7)]
        rect = boost_frames[0].get_rect()
        boost_frames = [pygame.transform.smoothscale(boost_frame, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE)) for boost_frame in boost_frames]

        boost_animation_speed = 0.2
        boost_frame_number = 0

        return boost_frames, boost_animation_speed, boost_frame_number

    def prepare_rect(self):
        rect = self.ship_frames[0].get_rect()
        rect.center = (rect.width, SETTINGS.WINDOW_HEIGHT // 2)
        return rect

    def shot(self):
        if self.in_magazine > 0:
            self.in_magazine -= 1
            return ShipBullet(self.rect.right, self.rect.centery, 10, self.hit_damage)
        else:
            return False

    def update(self):
        super(FirstShip, self).update()

        if self.state == ShipState.ALIVE:
            if self.go_left and self.rect.left > 0:
                self.rect.x -= self.speed
            if self.go_right and self.rect.right < SETTINGS.WINDOW_WIDTH:
                self.rect.x += self.speed
            if self.go_up and self.rect.top > (-25 * SETTINGS.SCALE):
                self.rect.y -= self.speed
            if self.go_down and self.rect.bottom < SETTINGS.WINDOW_HEIGHT + (25 * SETTINGS.SCALE):
                self.rect.y += self.speed

            if self.in_magazine < self.magazine_size:
                self.reloading = True
                if self.to_reload < 0:
                    self.in_magazine += 1
                    self.to_reload = self.reload_time
                    self.reloading = False
                else:
                    self.to_reload -= 0.016

        elif self.state == ShipState.DEAD:
            if self.explosion_frame_number >= len(self.explosion_frames):
                if self.lives == 0:
                    self.state = ShipState.OUTOFLIVES
                else:
                    self.reset()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.go_up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.go_down = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.go_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.go_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.go_up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.go_down = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.go_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.go_right = False

    def take_damage(self, damage):
        super(FirstShip, self).take_damage(damage)
        if self.state == ShipState.DEAD:
            self.lives -= 1

