import os.path

import pygame

from Aliens import SETTINGS


class GameUI:
    def __init__(self, gamecore):
        pygame.init()
        self.game = gamecore

        self.big_font, self.middle_font, self.small_font = self.load_font()

        self.score_text = self.get_score_text()
        self.score_rect = self.get_score_rect()

        self.wave_text = self.get_wave_text()
        self.wave_rect = self.get_wave_rect()

        self.enemies_left_text = self.get_enemies_left_text()
        self.enemies_left_rect = self.get_enemies_left_rect()

        self.in_magazine_text = self.get_in_magazine_text()
        self.in_magazine_rect = self.get_in_magazine_rect()

        self.ammo_icon = self.load_ammo_icon()
        self.ammo_icon_rect = self.get_ammo_icon_rect()

        self.to_reload_rect = self.get_to_reload_rect()
        self.to_reload_bar = self.get_to_reload_bar()

        self.lives_text = self.get_lives_text()
        self.lives_text_rect = self.get_lives_text_rect()

        self.lives_icon = self.load_lives_icon()
        self.lives_icon_rect = self.get_lives_icon_rect()

        self.health_bar = HealthBar(self)

    def refactor(self):
        self.big_font, self.middle_font, self.small_font = self.load_font()
        self.score_text = self.get_score_text()
        self.score_rect = self.get_score_rect()

        self.wave_text = self.get_wave_text()
        self.wave_rect = self.get_wave_rect()

        self.enemies_left_text = self.get_enemies_left_text()
        self.enemies_left_rect = self.get_enemies_left_rect()

        self.in_magazine_text = self.get_in_magazine_text()
        self.in_magazine_rect = self.get_in_magazine_rect()

        self.ammo_icon = self.load_ammo_icon()
        self.ammo_icon_rect = self.get_ammo_icon_rect()

        self.to_reload_rect = self.get_to_reload_rect()
        self.to_reload_bar = self.get_to_reload_bar()

        self.to_reload_rect = self.get_to_reload_rect()
        self.to_reload_bar = self.get_to_reload_bar()

        self.lives_text = self.get_lives_text()
        self.lives_text_rect = self.get_lives_text_rect()

        self.lives_icon = self.load_lives_icon()
        self.lives_icon_rect = self.get_lives_icon_rect()

        self.health_bar.refactor()

    def load_font(self):
        fonts_path = os.path.join("Data", "Fonts", "space-mission-font")
        font_name = "SpaceMission-rgyw9.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(128 * SETTINGS.SCALE))
        middle_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(50 * SETTINGS.SCALE))
        small_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(30 * SETTINGS.SCALE))

        return big_font, middle_font, small_font

    def get_score_text(self):
        score_text = self.middle_font.render(f"Score: {self.game.score}", True, (255, 255, 255))
        return score_text

    def get_score_rect(self):
        rect = self.score_text.get_rect()
        rect.topleft = (15 * SETTINGS.SCALE, 20 * SETTINGS.SCALE)
        return rect

    def get_wave_text(self):
        wave_text = self.middle_font.render(f"Wave {self.game.wave.wave_number}", True, (255, 255, 255))
        return wave_text

    def get_wave_rect(self):
        rect = self.wave_text.get_rect()
        rect.top = 20 * SETTINGS.SCALE
        rect.right = SETTINGS.WINDOW_WIDTH - 15 * SETTINGS.SCALE
        return rect

    def get_enemies_left_text(self):
        enemies_left_text = self.small_font.render(
            f"Enemies left {self.game.wave.enemies_to_spawn + len(self.game.wave.alive_enemies)}", True,
            (255, 255, 255))
        return enemies_left_text

    def get_enemies_left_rect(self):
        rect = self.enemies_left_text.get_rect()
        rect.top = 90 * SETTINGS.SCALE
        rect.right = SETTINGS.WINDOW_WIDTH - 15 * SETTINGS.SCALE
        return rect

    def get_in_magazine_text(self):
        in_magazine_text = self.middle_font.render(f"{self.game.ship.in_magazine}", True, (255, 255, 255))
        return in_magazine_text

    def get_in_magazine_rect(self):
        rect = self.in_magazine_text.get_rect()
        rect.left = 44 * SETTINGS.SCALE
        rect.top = 969 * SETTINGS.SCALE
        return rect

    def load_ammo_icon(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        filename = "bullet.png"
        icon = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        rect = icon.get_rect()
        icon = pygame.transform.smoothscale(icon, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE))
        return icon

    def get_ammo_icon_rect(self):
        rect = self.ammo_icon.get_rect()
        rect.topleft = (15 * SETTINGS.SCALE, 969 * SETTINGS.SCALE)
        return rect

    def get_lives_text(self):
        lives_text = self.middle_font.render(f"{self.game.ship.lives}", True, (255, 255, 255))
        return lives_text

    def get_lives_text_rect(self):
        rect = self.lives_text.get_rect()
        rect.right = 270 * SETTINGS.SCALE
        rect.top = 969 * SETTINGS.SCALE
        return rect

    def load_lives_icon(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        filename = "health.png"
        icon = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        rect = icon.get_rect()
        icon = pygame.transform.smoothscale(icon, (rect.width * SETTINGS.SCALE, rect.height * SETTINGS.SCALE))
        return icon

    def get_lives_icon_rect(self):
        rect = self.ammo_icon.get_rect()
        rect.top = 969 * SETTINGS.SCALE
        rect.right = 300 * SETTINGS.SCALE
        return rect

    def get_to_reload_rect(self):
        size = (
        300 * max(0, (self.game.ship.to_reload / self.game.ship.reload_time)) * SETTINGS.SCALE, 11 * SETTINGS.SCALE)
        rect = pygame.Rect((15 * SETTINGS.SCALE, 1053 * SETTINGS.SCALE), size)
        return rect

    def get_to_reload_bar(self):
        bar = pygame.Surface(self.to_reload_rect.size)
        bar.fill((226, 215, 82))
        return bar

    def update(self):
        self.score_text = self.get_score_text()
        self.wave_text = self.get_wave_text()
        self.enemies_left_text = self.get_enemies_left_text()
        self.in_magazine_text = self.get_in_magazine_text()
        self.lives_text = self.get_lives_text()

        if self.game.ship.reloading:
            self.to_reload_rect = self.get_to_reload_rect()
            self.to_reload_bar = self.get_to_reload_bar()

        self.health_bar.update()

    def draw(self, screen):
        screen.blit(self.score_text, self.score_rect)
        screen.blit(self.wave_text, self.wave_rect)
        screen.blit(self.enemies_left_text, self.enemies_left_rect)
        screen.blit(self.in_magazine_text, self.in_magazine_rect)
        screen.blit(self.ammo_icon, self.ammo_icon_rect)
        screen.blit(self.lives_text, self.lives_text_rect)
        screen.blit(self.lives_icon, self.lives_icon_rect)

        self.health_bar.draw(screen)

        if self.game.ship.reloading:
            screen.blit(self.to_reload_bar, self.to_reload_rect)


class HealthBar:
    def __init__(self, hud):
        self.hud = hud

        self.health_font = self.load_health_font()

        self.red_bar_rect = self.get_red_bar_rect()
        self.red_bar = self.get_red_bar()

        self.yellow_bar_rect = self.get_yellow_bar_rect()
        self.yellow_bar = self.get_yellow_bar()

        self.green_bar_rect = self.get_green_bar_rect()
        self.green_bar = self.get_green_bar()

        self.health_text = self.get_health_text()
        self.health_text_rect = self.get_health_rect()

    def refactor(self):
        self.health_font = self.load_health_font()
        # red bar done only once
        self.red_bar_rect = self.get_red_bar_rect()
        self.red_bar = self.get_red_bar()

        # yellow bar refactor in case
        self.yellow_bar_rect = self.get_yellow_bar_rect()
        self.yellow_bar = self.get_yellow_bar()

        self.green_bar_rect = self.get_green_bar_rect()

        self.health_text = self.get_health_text()
        self.health_text_rect = self.get_health_rect()

    def load_health_font(self):
        fonts_path = os.path.join("Data", "Fonts", "space-mission-font")
        font_name = "SpaceMission-rgyw9.otf"

        health_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(20 * SETTINGS.SCALE))

        return health_font

    def get_red_bar_rect(self):
        bar_rect = pygame.Rect((15 * SETTINGS.SCALE, 1017 * SETTINGS.SCALE),
                               (300 * SETTINGS.SCALE, 30 * SETTINGS.SCALE))
        return bar_rect

    def get_red_bar(self):
        bar = pygame.Surface(self.red_bar_rect.size)
        bar.fill((202, 34, 34))
        return bar

    def get_yellow_bar_rect(self):
        bar_rect = pygame.Rect((15 * SETTINGS.SCALE, 1017 * SETTINGS.SCALE),
                               (300 * SETTINGS.SCALE, 30 * SETTINGS.SCALE))
        return bar_rect

    def get_yellow_bar(self):
        bar = pygame.Surface(self.yellow_bar_rect.size)
        bar.fill((226, 215, 82))
        return bar

    def get_green_bar_rect(self):
        health_scale = self.hud.game.ship.current_health / self.hud.game.ship.health_capacity
        bar_rect = pygame.Rect((15 * SETTINGS.SCALE, 1017 * SETTINGS.SCALE),
                               (300 * SETTINGS.SCALE * health_scale, 30 * SETTINGS.SCALE))
        return bar_rect

    def get_green_bar(self):
        bar = pygame.Surface(self.green_bar_rect.size)
        bar.fill((69, 251, 78))
        return bar

    def get_health_text(self):
        health_text = self.health_font.render(f"{self.hud.game.ship.current_health}", True, (255, 255, 255))
        return health_text

    def get_health_rect(self):
        rect = self.health_text.get_rect()
        rect.centerx = self.red_bar_rect.centerx
        rect.centery = self.red_bar_rect.centery
        return rect

    def update(self):
        self.green_bar_rect = self.get_green_bar_rect()
        self.green_bar = self.get_green_bar()

        self.health_text = self.get_health_text()

        if self.hud.game.ship.current_health == self.hud.game.ship.health_capacity:
            self.yellow_bar_rect = self.get_yellow_bar_rect()
            self.yellow_bar = self.get_yellow_bar()

        elif self.green_bar_rect.width < self.yellow_bar_rect.width:
            if self.hud.game.ship.current_health <= 0:
                new_size = (max(0, self.yellow_bar_rect.width - 15 * SETTINGS.SCALE), self.yellow_bar_rect.height)
                self.yellow_bar_rect = pygame.Rect((self.yellow_bar_rect.x, self.yellow_bar_rect.y), new_size)
            else:
                new_size = (max(0, self.yellow_bar_rect.width - 3 * SETTINGS.SCALE), self.yellow_bar_rect.height)
                self.yellow_bar_rect = pygame.Rect((self.yellow_bar_rect.x, self.yellow_bar_rect.y), new_size)

            self.yellow_bar = pygame.Surface(self.yellow_bar_rect.size)
            self.yellow_bar.fill((226, 215, 82))

    def draw(self, screen):
        screen.blit(self.red_bar, self.red_bar_rect)
        screen.blit(self.yellow_bar, self.yellow_bar_rect)
        screen.blit(self.green_bar, self.green_bar_rect)
        screen.blit(self.health_text, self.health_text_rect)
