import pygame
import os.path
from Aliens import SETTINGS, SOUNDS
from Aliens.Ship.ship import Ship, ShipState
from Aliens.Bullets.ship_bullet import ShipBullet


class PlayerShip(Ship):
    def __init__(self, app):
        super(PlayerShip, self).__init__()
        self.app = app
        self.state = ShipState.RESPAWNING
        self.respawn_speed = 10 * SETTINGS.SCALE
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
        # immortal bubble
        self.bubble_frames, self.bubble_frame_number, self.bubble_animation_speed = self.load_bubble_frames()

    def new_game(self):
        self.reset_directions()
        self.reloading = False

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
        # immortal bubble
        self.bubble_frames, self.bubble_frame_number, self.bubble_animation_speed = self.load_bubble_frames()

        self.reset()

    def reset(self):
        self.state = ShipState.RESPAWNING
        self.current_health = self.health_capacity
        self.in_magazine = self.magazine_size
        self.to_reload = self.reload_time
        self.reloading = False

        self.ship_frame_number = 0
        self.explosion_frame_number = 0
        self.boost_frame_number = 0
        self.bubble_frame_number = 0
        self.rect = self.prepare_rect()
        self.real_x = self.rect.x
        self.real_y = self.rect.y
        self.app.background.animate_background = True
        self.reset_directions()

    def reset_directions(self):
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False

    def refactor(self):
        super(PlayerShip, self).refactor()
        self.speed = round(self.app.current_profile.ship_speed.get_value() * SETTINGS.SCALE)
        self.bullet_speed = self.app.current_profile.bullet_speed.get_value()

    def load_ship_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")

        ship_frames = [pygame.image.load(os.path.join(images_folder, f"ship-{i}.png")).convert_alpha() for i in range(3)]
        rect = ship_frames[0].get_rect()
        ship_frames = [pygame.transform.smoothscale(ship_frame, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE))) for ship_frame in ship_frames]

        ship_frame_number = 0

        return ship_frames, ship_frame_number

    def load_bubble_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")

        bubble_frames = [pygame.image.load(os.path.join(images_folder, f"bubble-{i}.png")).convert_alpha() for i in range(9)]
        rect = bubble_frames[0].get_rect()
        bubble_frames = [pygame.transform.smoothscale(bubble_frame, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE))) for bubble_frame in bubble_frames]

        bubble_frame_number = 0
        bubble_animation_speed = 0.4

        return bubble_frames, bubble_frame_number, bubble_animation_speed

    def load_boost_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")

        boost_frames = [pygame.image.load(os.path.join(images_folder, f"boost-{i}.png")).convert_alpha() for i in range(3)]
        rect = boost_frames[0].get_rect()
        boost_frames = [pygame.transform.smoothscale(boost_frame, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE))) for boost_frame in boost_frames]

        boost_animation_speed = 0.15
        boost_frame_number = 0

        return boost_frames, boost_animation_speed, boost_frame_number

    def load_explosion_frames(self):
        images_folder = os.path.join("Data", "Sprites", "Ships", "FirstShip")

        boost_frames = [pygame.image.load(os.path.join(images_folder, f"explode-{i}.png")).convert_alpha() for i in range(7)]
        rect = boost_frames[0].get_rect()
        boost_frames = [pygame.transform.smoothscale(boost_frame, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE))) for boost_frame in boost_frames]

        boost_animation_speed = 0.2
        boost_frame_number = 0

        return boost_frames, boost_animation_speed, boost_frame_number

    def prepare_rect(self):
        rect = self.ship_frames[0].get_rect()
        rect.centery = SETTINGS.WINDOW_HEIGHT // 2
        rect.right = 0
        return rect

    def get_image(self):
        image = super(PlayerShip, self).get_image()
        return image

    def shot(self):
        if self.in_magazine > 0:
            SOUNDS.player_shot.play()
            number_of_shots = self.app.current_profile.bullets_in_shot.get_value()
            shot = ShipBullet(self.rect.right, self.rect.centery - (20 * SETTINGS.SCALE), self.bullet_speed, self.bullet_damage)
            if number_of_shots % 2 == 0:
                shot.real_y -= shot.rect.height / 2
                shot.rect.y = int(shot.real_y)

            shots = [shot]
            for i in range(number_of_shots-1):
                if i % 2 == 0:
                    vertical_number = (i + 2) // 2
                else:
                    vertical_number = (i+1) // -2
                new_shot = ShipBullet(self.rect.right, shot.rect.top + (shot.rect.height * vertical_number), self.bullet_speed, self.bullet_damage)
                shots.append(new_shot)
            self.in_magazine -= 1
            return shots
        else:
            SOUNDS.empty_magazine.play()
            return False

    def update(self):
        super(PlayerShip, self).update()

        if self.bubble_frame_number < len(self.bubble_frames):
            self.image.blit(self.bubble_frames[int(self.bubble_frame_number)], (0, 0))
            if self.state == ShipState.RESPAWNING:
                self.bubble_frame_number = 0
            else:
                self.bubble_frame_number += self.bubble_animation_speed

        if self.state == ShipState.ALIVE:
            if self.go_left and self.rect.left > 0:
                self.real_x -= self.speed
            if self.go_right and self.rect.right < SETTINGS.WINDOW_WIDTH:
                self.real_x += self.speed
            if self.go_up and self.rect.top > (-25 * SETTINGS.SCALE):
                self.real_y -= self.speed
            if self.go_down and self.rect.bottom < SETTINGS.WINDOW_HEIGHT + (25 * SETTINGS.SCALE):
                self.real_y += self.speed

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
                    self.rect = self.prepare_rect()
                    self.state = ShipState.OUTOFLIVES
                else:
                    self.reset()

        elif self.state == ShipState.RESPAWNING:
            if self.rect.right < self.rect.width * 2:
                self.real_x += self.respawn_speed * SETTINGS.SCALE
            else:
                self.state = ShipState.ALIVE

    def handle_event(self, event):
        if self.state == ShipState.ALIVE:
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




