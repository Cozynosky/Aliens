import pygame
import os.path

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

        self.magazine_text = self.get_magazine_text()
        self.magazine_text_rect = self.get_magazine_rect()

        self.in_magazine_text = self.get_in_magazine_text()
        self.in_magazine_rect = self.get_in_magazine_rect()

        self.to_reload_rect = self.get_to_reload_rect()
        self.to_reload_bar = self.get_to_reload_bar()

    def refactor(self):
        self.big_font, self.middle_font, self.small_font = self.load_font()
        self.score_text = self.get_score_text()
        self.score_rect = self.get_score_rect()

        self.wave_text = self.get_wave_text()
        self.wave_rect = self.get_wave_rect()

        self.enemies_left_text = self.get_enemies_left_text()
        self.enemies_left_rect = self.get_enemies_left_rect()

        self.magazine_text = self.get_magazine_text()
        self.magazine_text_rect = self.get_magazine_rect()

        self.in_magazine_text = self.get_in_magazine_text()
        self.in_magazine_rect = self.get_in_magazine_rect()

        self.to_reload_rect = self.get_to_reload_rect()
        self.to_reload_bar = self.get_to_reload_bar()

    def load_font(self):
        fonts_path = os.path.join("Data", "Fonts", "space-mission-font")
        font_name = "SpaceMission-rgyw9.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(150 * SETTINGS.SCALE))
        middle_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(70 * SETTINGS.SCALE))
        small_font = pygame.font.Font(os.path.join(fonts_path, font_name), int(54 * SETTINGS.SCALE))

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
        rect.centerx = SETTINGS.WINDOW_WIDTH / 2
        return rect

    def get_enemies_left_text(self):
        enemies_left_text = self.small_font.render(f"Enemies left {self.game.wave.enemies_to_spawn + len(self.game.wave.alive_enemies)}", True, (255, 255, 255))
        return enemies_left_text

    def get_enemies_left_rect(self):
        rect = self.enemies_left_text.get_rect()
        rect.top = 90 * SETTINGS.SCALE
        rect.centerx = SETTINGS.WINDOW_WIDTH / 2
        return rect

    def get_magazine_text(self):
        magazine_text = self.small_font.render(f"Magazine", True, (255, 255, 255))
        return magazine_text

    def get_magazine_rect(self):
        rect = self.magazine_text.get_rect()
        rect.top = 913 * SETTINGS.SCALE
        rect.centerx = 1780 * SETTINGS.SCALE
        return rect

    def get_in_magazine_text(self):
        in_magazine_text = self.middle_font.render(f"{self.game.ship.in_magazine} / {self.game.ship.magazine_size}", True, (255, 255, 255))
        return in_magazine_text

    def get_in_magazine_rect(self):
        rect = self.in_magazine_text.get_rect()
        rect.centerx = self.magazine_text_rect.centerx
        rect.top = 965 * SETTINGS.SCALE
        return rect

    def get_to_reload_rect(self):
        size = (200 * (self.game.ship.to_reload / self.game.ship.reload_time) * SETTINGS.SCALE, 11 * SETTINGS.SCALE)
        rect = pygame.Rect((1675 * SETTINGS.SCALE, 1040 * SETTINGS.SCALE), size)
        return rect

    def get_to_reload_bar(self):
        bar = pygame.Surface(self.to_reload_rect.size)
        bar.fill((226, 215, 82))
        return bar

    def update(self):
        self.score_text = self.get_score_text()
        self.wave_text = self.get_wave_text()
        self.enemies_left_text = self.get_enemies_left_text()
        self.magazine_text = self.get_magazine_text()
        self.in_magazine_text = self.get_in_magazine_text()
        if self.game.ship.reloading:
            self.to_reload_rect = self.get_to_reload_rect()
            self.to_reload_bar = self.get_to_reload_bar()

    def draw(self, screen):
        screen.blit(self.score_text, self.score_rect)
        screen.blit(self.wave_text, self.wave_rect)
        screen.blit(self.enemies_left_text, self.enemies_left_rect)
        screen.blit(self.magazine_text, self.magazine_text_rect)
        screen.blit(self.in_magazine_text, self.in_magazine_rect)
        if self.game.ship.reloading:
            screen.blit(self.to_reload_bar, self.to_reload_rect)
