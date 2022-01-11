import os.path

import pygame

from Aliens import SETTINGS
from Aliens.EndlessGameCore.enums import UIState


class GameUI:
    def __init__(self, gamecore):
        pygame.init()
        self.state = UIState.SHOWING_UP
        self.showing_speed = 4 * SETTINGS.SCALE
        self.game = gamecore

        self.big_font, self.middle_font, self.small_font = self.load_font()

        self.bottom_hud_bg = self.load_bottom_hud_bg()
        self.bottom_hud_bg_rect = self.get_bottom_hud_bg_rect()
        self.bottom_hud_bg_mask = self.get_bottom_hud_bg_mask()

        self.bottom_hud_fg = self.load_bottom_hud_fg()
        self.bottom_hud_fg_rect = self.get_bottom_hud_fg_rect()

        self.top_hud_bg = self.load_top_hud_bg()
        self.top_hud_bg_rect = self.get_top_hud_bg_rect()
        self.top_hud_bg_mask = self.get_top_hud_bg_mask()

        self.top_hud_fg = self.load_top_hud_fg()
        self.top_hud_fg_rect = self.get_top_hud_fg_rect()

        self.score_text = self.get_score_text()
        self.score_rect = self.get_score_rect()

        self.coins_earned_text = self.get_coins_earned_text()
        self.coins_earned_text_rect = self.get_coins_earned_text_rect()

        self.wave_text = self.get_wave_text()
        self.wave_rect = self.get_wave_rect()

        self.enemies_left_text = self.get_enemies_left_text()
        self.enemies_left_rect = self.get_enemies_left_rect()

        self.in_magazine_text = self.get_in_magazine_text()
        self.in_magazine_rect = self.get_in_magazine_rect()

        self.to_reload_rect = self.get_to_reload_rect()
        self.to_reload_bar = self.get_to_reload_bar()

        self.lives_text = self.get_lives_text()
        self.lives_text_rect = self.get_lives_text_rect()

        self.health_bar = HealthBar(self)

        self.top_alpha = 255
        self.bottom_alpha = 255

    def refactor(self):
        self.showing_speed = 4 * SETTINGS.SCALE
        self.big_font, self.middle_font, self.small_font = self.load_font()

        self.bottom_hud_bg = self.load_bottom_hud_bg()
        self.bottom_hud_bg_rect = self.get_bottom_hud_bg_rect()
        self.bottom_hud_bg_mask = self.get_bottom_hud_bg_mask()

        self.bottom_hud_fg = self.load_bottom_hud_fg()
        self.bottom_hud_fg_rect = self.get_bottom_hud_fg_rect()

        self.top_hud_bg = self.load_top_hud_bg()
        self.top_hud_bg_rect = self.get_top_hud_bg_rect()
        self.top_hud_bg_mask = self.get_top_hud_bg_mask()

        self.top_hud_fg = self.load_top_hud_fg()
        self.top_hud_fg_rect = self.get_top_hud_fg_rect()

        self.score_text = self.get_score_text()
        self.score_rect = self.get_score_rect()

        self.coins_earned_text = self.get_coins_earned_text()
        self.coins_earned_text_rect = self.get_coins_earned_text_rect()

        self.wave_text = self.get_wave_text()
        self.wave_rect = self.get_wave_rect()

        self.enemies_left_text = self.get_enemies_left_text()
        self.enemies_left_rect = self.get_enemies_left_rect()

        self.in_magazine_text = self.get_in_magazine_text()
        self.in_magazine_rect = self.get_in_magazine_rect()

        self.to_reload_rect = self.get_to_reload_rect()
        self.to_reload_bar = self.get_to_reload_bar()

        self.lives_text = self.get_lives_text()
        self.lives_text_rect = self.get_lives_text_rect()

        self.health_bar = HealthBar(self)

        self.top_alpha = 255
        self.bottom_alpha = 255

    def reset(self):
        self.state = UIState.SHOWING_UP
        self.top_hud_bg_rect = self.get_top_hud_bg_rect()
        self.bottom_hud_bg_rect = self.get_bottom_hud_bg_rect()

    def load_font(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(56 * SETTINGS.SCALE))
        middle_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(35 * SETTINGS.SCALE))
        small_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(30 * SETTINGS.SCALE))

        return big_font, middle_font, small_font

    def load_bottom_hud_bg(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        bottom_hud_back = pygame.image.load(os.path.join(images_folder, "bottom_hud_back.png")).convert_alpha()
        rect = bottom_hud_back.get_rect()
        bottom_hud_back = pygame.transform.smoothscale(bottom_hud_back, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE)))
        return bottom_hud_back

    def get_bottom_hud_bg_rect(self):
        rect = self.bottom_hud_bg.get_rect()
        rect.centerx = SETTINGS.WINDOW_WIDTH // 2
        rect.top = SETTINGS.WINDOW_HEIGHT
        return rect

    def get_bottom_hud_bg_mask(self):
        mask = pygame.mask.from_surface(self.bottom_hud_bg)
        return mask

    def load_bottom_hud_fg(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        front_hud_back = pygame.image.load(os.path.join(images_folder, "bottom_hud_front.png")).convert_alpha()
        rect = front_hud_back.get_rect()
        front_hud_back = pygame.transform.smoothscale(front_hud_back, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE)))
        return front_hud_back

    def get_bottom_hud_fg_rect(self):
        rect = self.bottom_hud_fg.get_rect()
        rect.x = 0
        rect.y = 0
        return rect

    def load_top_hud_bg(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        top_hud_bg= pygame.image.load(os.path.join(images_folder, "top_hud_back.png")).convert_alpha()
        rect = top_hud_bg.get_rect()
        top_hud_bg = pygame.transform.smoothscale(top_hud_bg, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE)))
        return top_hud_bg

    def get_top_hud_bg_rect(self):
        rect = self.top_hud_bg.get_rect()
        rect.centerx = SETTINGS.WINDOW_WIDTH // 2 - (70 * SETTINGS.SCALE)
        rect.bottom = 0
        return rect

    def get_top_hud_bg_mask(self):
        mask = pygame.mask.from_surface(self.top_hud_bg)
        return mask

    def load_top_hud_fg(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        fg = pygame.image.load(os.path.join(images_folder, "top_hud_front.png")).convert_alpha()
        rect = fg.get_rect()
        fg = pygame.transform.smoothscale(fg, (int(rect.width * SETTINGS.SCALE), int(rect.height * SETTINGS.SCALE)))
        return fg

    def get_top_hud_fg_rect(self):
        rect = self.top_hud_fg.get_rect()
        rect.x = 0
        rect.top = 0
        return rect

    def get_score_text(self):
        score_text = self.big_font.render(f"{self.game.score}", True, (255, 255, 255))
        return score_text

    def get_score_rect(self):
        rect = self.score_text.get_rect()
        rect.top = 56 * SETTINGS.SCALE
        rect.centerx = 381 * SETTINGS.SCALE
        return rect

    def get_coins_earned_text(self):
        text = self.middle_font.render(f"{self.game.coins_earned}", True, (255, 255, 255))
        return text

    def get_coins_earned_text_rect(self):
        rect = self.coins_earned_text.get_rect()
        rect.top = 4 * SETTINGS.SCALE
        rect.left = 81 * SETTINGS.SCALE
        return rect

    def get_wave_text(self):
        wave_text = self.middle_font.render(f"Wave {self.game.wave.wave_number}", True, (255, 255, 255))
        return wave_text

    def get_wave_rect(self):
        rect = self.wave_text.get_rect()
        rect.top = 12 * SETTINGS.SCALE
        rect.left = 213 * SETTINGS.SCALE
        return rect

    def get_enemies_left_text(self):
        enemies_left_text = self.middle_font.render(
            f"{self.game.wave.enemies_left}", True,
            (255, 255, 255))
        return enemies_left_text

    def get_enemies_left_rect(self):
        rect = self.enemies_left_text.get_rect()
        rect.top = 12 * SETTINGS.SCALE
        rect.right = 507 * SETTINGS.SCALE
        return rect

    def get_in_magazine_text(self):
        in_magazine_text = self.middle_font.render(f"{self.game.ship.in_magazine}", True, (255, 255, 255))
        return in_magazine_text

    def get_in_magazine_rect(self):
        rect = self.in_magazine_text.get_rect()
        rect.right = 211 * SETTINGS.SCALE
        rect.top = 21 * SETTINGS.SCALE
        return rect

    def get_lives_text(self):
        lives_text = self.middle_font.render(f"{self.game.ship.lives}", True, (255, 255, 255))
        return lives_text

    def get_lives_text_rect(self):
        rect = self.lives_text.get_rect()
        rect.left = 285 * SETTINGS.SCALE
        rect.top = 21 * SETTINGS.SCALE
        return rect

    def get_to_reload_rect(self):
        size = (
            int(400 * max(0, (self.game.ship.to_reload / self.game.ship.reload_time)) * SETTINGS.SCALE), int(15 * SETTINGS.SCALE))
        rect = pygame.Rect((49 * SETTINGS.SCALE, 69 * SETTINGS.SCALE), size)
        return rect

    def get_to_reload_bar(self):
        bar = pygame.Surface(self.to_reload_rect.size)
        bar.fill((226, 215, 82))
        return bar

    def update(self):
        if self.state == UIState.SHOWING_UP:
            if self.bottom_hud_bg_rect.bottom > SETTINGS.WINDOW_HEIGHT:
                self.bottom_hud_bg_rect.bottom -= self.showing_speed
            if self.top_hud_bg_rect.top < 0:
                self.top_hud_bg_rect.top += self.showing_speed

            if self.bottom_hud_bg_rect.bottom <= SETTINGS.WINDOW_HEIGHT and self.top_hud_bg_rect.top >=0:
                self.state = UIState.SHOWED

        self.bottom_alpha = 255
        self.top_alpha = 255
        self.score_text = self.get_score_text()
        self.score_rect = self.get_score_rect()
        self.coins_earned_text = self.get_coins_earned_text()
        self.wave_text = self.get_wave_text()
        self.wave_rect = self.get_wave_rect()
        self.enemies_left_text = self.get_enemies_left_text()
        self.enemies_left_rect = self.get_enemies_left_rect()
        self.in_magazine_text = self.get_in_magazine_text()
        self.lives_text = self.get_lives_text()
        self.lives_text_rect = self.get_lives_text_rect()

        if self.game.ship.reloading:
            self.to_reload_rect = self.get_to_reload_rect()
            self.to_reload_bar = self.get_to_reload_bar()

        self.health_bar.update()

    def draw(self, screen):
        self.top_hud_bg = self.load_top_hud_bg()
        self.top_hud_bg.blit(self.score_text, self.score_rect)
        self.top_hud_bg.blit(self.coins_earned_text, self.coins_earned_text_rect)
        self.top_hud_bg.blit(self.wave_text, self.wave_rect)
        self.top_hud_bg.blit(self.enemies_left_text, self.enemies_left_rect)
        self.top_hud_bg.blit(self.top_hud_fg, self.top_hud_fg_rect)
        self.top_hud_bg.set_alpha(self.top_alpha)
        screen.blit(self.top_hud_bg, self.top_hud_bg_rect)

        self.bottom_hud_bg = self.load_bottom_hud_bg()
        self.bottom_hud_bg.blit(self.in_magazine_text, self.in_magazine_rect)
        self.bottom_hud_bg.blit(self.lives_text, self.lives_text_rect)
        self.health_bar.draw(self.bottom_hud_bg)
        if self.game.ship.reloading:
            self.bottom_hud_bg.blit(self.to_reload_bar, self.to_reload_rect)
        self.bottom_hud_bg.blit(self.bottom_hud_fg, self.bottom_hud_fg_rect)

        self.bottom_hud_bg.set_alpha(self.bottom_alpha)
        screen.blit(self.bottom_hud_bg, self.bottom_hud_bg_rect)

    def hide_top_hud(self):
        self.top_alpha = 128

    def hide_bottom_hud(self):
        self.bottom_alpha = 128


class HealthBar:
    def __init__(self, hud):
        self.hud = hud

        self.red_bar_rect = self.get_red_bar_rect()
        self.red_bar = self.get_red_bar()

        self.yellow_bar_rect = self.get_yellow_bar_rect()
        self.yellow_bar = self.get_yellow_bar()

        self.green_bar_rect = self.get_green_bar_rect()
        self.green_bar = self.get_green_bar()

    def refactor(self):
        # red bar done only once
        self.red_bar_rect = self.get_red_bar_rect()
        self.red_bar = self.get_red_bar()

        # yellow bar refactor in case
        self.yellow_bar_rect = self.get_yellow_bar_rect()
        self.yellow_bar = self.get_yellow_bar()

        self.green_bar_rect = self.get_green_bar_rect()

    def get_red_bar_rect(self):
        bar_rect = pygame.Rect(((32 * SETTINGS.SCALE), (91 * SETTINGS.SCALE)),
                               (434 * SETTINGS.SCALE, 25 * SETTINGS.SCALE))
        return bar_rect

    def get_red_bar(self):
        bar = pygame.Surface(self.red_bar_rect.size)
        bar.fill((202, 34, 34))
        return bar

    def get_yellow_bar_rect(self):
        bar_rect = pygame.Rect(((32 * SETTINGS.SCALE), (91 * SETTINGS.SCALE)),
                               (434 * SETTINGS.SCALE, 25 * SETTINGS.SCALE))
        return bar_rect

    def get_yellow_bar(self):
        bar = pygame.Surface(self.yellow_bar_rect.size)
        bar.fill((226, 215, 82))
        return bar

    def get_green_bar_rect(self):
        health_scale = self.hud.game.ship.current_health / self.hud.game.ship.health_capacity
        bar_rect = pygame.Rect(((32 * SETTINGS.SCALE), + (91 * SETTINGS.SCALE)),
                               (434 * SETTINGS.SCALE * health_scale,  25 * SETTINGS.SCALE))
        return bar_rect

    def get_green_bar(self):
        bar = pygame.Surface(self.green_bar_rect.size)
        bar.fill((69, 251, 78))
        return bar

    def update(self):
        self.green_bar_rect = self.get_green_bar_rect()
        self.green_bar = self.get_green_bar()

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
