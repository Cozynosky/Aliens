import pygame
import os.path

from Aliens import SETTINGS


class NextWaveScene:
    def __init__(self):
        pygame.font.init()
        self.font = self.prepare_font()
        self.text = self.prepare_text()
        self.text_rect = self.get_text_rect()
        self.real_x = self.text_rect.x
        self.speed = 50 * SETTINGS.SCALE
        self.stop_time = 0.3
        self.is_ready = False
        self.stop_made = False
        self.is_moving = True

    def refactor(self):
        self.font = self.prepare_font()
        self.text = self.prepare_text()
        self.text_rect = self.get_text_rect()
        self.speed = 50 * SETTINGS.SCALE

    def prepare_font(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        font = pygame.font.Font(os.path.join(fonts_path, font_name), int(150 * SETTINGS.SCALE))
        return font

    def prepare_text(self):
        text = self.font.render("Next Wave", True, (255, 255, 255))
        return text

    def get_text_rect(self):
        rect = self.text.get_rect()
        rect.right = 0
        rect.centery = SETTINGS.WINDOW_HEIGHT // 2
        return rect

    def reset(self):
        self.text_rect = self.get_text_rect()
        self.real_x = self.text_rect.x
        self.stop_time = 0.3
        self.is_ready = False
        self.stop_made = False
        self.is_moving = True

    def update(self):
        if self.is_moving:
            self.real_x += self.speed
            self.text_rect.x = self.real_x
            if self.text_rect.left >= SETTINGS.WINDOW_WIDTH:
                self.is_ready = True
            elif self.text_rect.centerx >= SETTINGS.WINDOW_WIDTH//2 and not self.stop_made:
                self.is_moving = False
        else:
            self.stop_time -= 0.016
            if self.stop_time <= 0:
                self.is_moving = True
                self.stop_made = True

    def render(self, screen):
        screen.blit(self.text, self.text_rect)
