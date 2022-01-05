import pygame
import os.path
from Aliens import SETTINGS
from Aliens.Ship.ship import Ship, ShipState
from Aliens.Bullets.ship_bullet import ShipBullet


class PlayerShip(Ship):
    def __init__(self, app):
        super(PlayerShip, self).__init__()
        self.app = app
        # upgradable values from current profile
        self.speed = self.app.current_profile.ship_speed.get_value() * SETTINGS.SCALE
        self.bullet_speed = self.app.current_profile.bullet_speed.get_value()
        self.bullet_damage = self.app.current_profile.bullet_damage.get_value()
        self.health_capacity = self.app.current_profile.health_capacity.get_value()
        self.lives = self.app.current_profile.lives.get_value()
        self.magazine_size = self.app.current_profile.magazine_size.get_value()
        self.reload_time = self.app.current_profile.reload_time.get_value()                      # in seconds
        self.reloading = False
        self.current_health = self.health_capacity
        self.in_magazine = self.magazine_size
        self.to_reload = self.reload_time

    def new_game(self):
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False
        self.reloading = False

        # upgradable values from current profile
        self.speed = round(self.app.current_profile.ship_speed.get_value() * SETTINGS.SCALE)
        self.bullet_speed = self.app.current_profile.bullet_speed.get_value()
        self.bullet_damage = self.app.current_profile.bullet_damage.get_value()
        self.health_capacity = self.app.current_profile.health_capacity.get_value()
        self.lives = self.app.current_profile.lives.get_value()
        self.magazine_size = self.app.current_profile.magazine_size.get_value()
        self.reload_time = self.app.current_profile.reload_time.get_value()                      # in seconds
        self.reloading = False
        self.current_health = self.health_capacity
        self.in_magazine = self.magazine_size
        self.to_reload = self.reload_time

        self.reset()

    def reset(self):
        self.state = ShipState.ALIVE
        self.current_health = self.health_capacity
        self.in_magazine = self.magazine_size
        self.to_reload = self.reload_time
        self.reloading = False

        self.ship_frame_number = 0
        self.explosion_frame_number = 0
        self.boost_frame_number = 0
        self.rect = self.prepare_rect()

    def refactor(self):
        super(PlayerShip, self).refactor()
        self.speed = round(self.app.current_profile.ship_speed.get_value() * SETTINGS.SCALE)
        self.bullet_speed = self.app.current_profile.bullet_speed.get_value()

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
            return ShipBullet(self.rect.right, self.rect.centery, self.bullet_speed, self.bullet_damage)
        else:
            return False

    def update(self):
        super(PlayerShip, self).update()

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
        if super(PlayerShip, self).take_damage(damage):
            self.lives -= 1
            return True
        else:
            return False




