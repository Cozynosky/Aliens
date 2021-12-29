from sys import exit

import pygame
import pygame_gui
import os.path

from Aliens import SETTINGS
from Aliens.scene import Scene


class StatisticsScene(Scene):
    def __init__(self, parent):
        super(StatisticsScene, self).__init__(parent)
        self.parent = parent
        pygame.font.init()
        # prepare font
        self.big_font, self.small_font = self.load_fonts()
        # banner at the top
        self.statistics_text, self.statistics_text_rect = self.prepare_statistics_text()
        # small bg
        self.statistics_background, self.statistics_background_rect = self.prepare_statistics_background()
        # statistics texts
        self.highest_score_text = self.get_highest_score_text()
        self.highest_score_text_rect = self.get_highest_score_text_rect()
        self.highest_wave_text = self.get_highest_wave_text()
        self.highest_wave_text_rect = self.get_highest_wave_text_rect()
        self.total_enemies_killed_text = self.get_total_enemies_killed_text()
        self.total_enemies_killed_text_rect = self.get_total_enemies_killed_text_rect()
        self.total_coins_earned_text = self.get_total_coins_earned_text()
        self.total_coins_earned_text_rect = self.get_total_coins_earned_text_rect()
        self.time_text = self.get_time_text()
        self.time_text_rect = self.get_time_text_rect()
        #buttons
        self.back_button = self.prepare_back_button()

    def refactor_ui(self):
        # ui manager
        self.manager = self.prepare_manager()
        # prepare font
        self.big_font, self.small_font = self.load_fonts()
        # banner at the top
        self.statistics_text, self.statistics_text_rect = self.prepare_statistics_text()
        # small bg
        self.statistics_background, self.statistics_background_rect = self.prepare_statistics_background()
        # statistics texts
        self.highest_score_text = self.get_highest_score_text()
        self.highest_score_text_rect = self.get_highest_score_text_rect()
        self.highest_wave_text = self.get_highest_wave_text()
        self.highest_wave_text_rect = self.get_highest_wave_text_rect()
        self.total_enemies_killed_text = self.get_total_enemies_killed_text()
        self.total_enemies_killed_text_rect = self.get_total_enemies_killed_text_rect()
        self.total_coins_earned_text = self.get_total_coins_earned_text()
        self.total_coins_earned_text_rect = self.get_total_coins_earned_text_rect()
        self.time_text = self.get_time_text()
        self.time_text_rect = self.get_time_text_rect()
        #buttons
        self.back_button = self.prepare_back_button()

    def update(self):
        self.highest_score_text = self.get_highest_score_text()
        self.highest_wave_text = self.get_highest_wave_text()
        self.total_enemies_killed_text = self.get_total_enemies_killed_text()
        self.total_coins_earned_text = self.get_total_coins_earned_text()
        self.time_text = self.get_time_text()

    def load_fonts(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), 60)
        small_font = pygame.font.Font(os.path.join(fonts_path, font_name), 30)

        return big_font, small_font

    def prepare_statistics_text(self):
        background = pygame.Surface((SETTINGS.WINDOW_WIDTH, 70))
        background.fill(pygame.Color('#808080'))
        background_rect = background.get_rect()
        background_rect.x = 0
        background_rect.y = 50

        text = self.big_font.render('Statistics', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 300 * SETTINGS.SCALE
        text_rect.centery = 35
        background.blit(text, text_rect)
        return background, background_rect

    def prepare_statistics_background(self):
        images_folder = os.path.join("Data", "Sprites", "Background")
        filename = "small_bg.png"
        background = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        rect = background.get_rect()
        rect.centerx = SETTINGS.WINDOW_WIDTH // 2
        rect.top = self.statistics_text_rect.bottom + 20

        return background, rect

    def get_highest_score_text(self):
        text = self.small_font.render(f"Highest score: {self.parent.current_profile.highest_score}", True, (255, 255, 255))
        return text

    def get_highest_score_text_rect(self):
        rect = self.highest_score_text.get_rect()
        rect.top = self.statistics_background_rect.top + 30
        rect.left = self.statistics_background_rect.left + 30
        return rect

    def get_highest_wave_text(self):
        text = self.small_font.render(f"Highest wave: {self.parent.current_profile.highest_wave}", True, (255, 255, 255))
        return text

    def get_highest_wave_text_rect(self):
        rect = self.highest_score_text.get_rect()
        rect.top = self.highest_score_text_rect.bottom + 10
        rect.left = self.statistics_background_rect.left + 30
        return rect

    def get_total_enemies_killed_text(self):
        text = self.small_font.render(f"Total enemies killed: {self.parent.current_profile.total_enemies_killed}", True, (255, 255, 255))
        return text

    def get_total_enemies_killed_text_rect(self):
        rect = self.total_enemies_killed_text.get_rect()
        rect.top = self.highest_wave_text_rect.bottom + 10
        rect.left = self.statistics_background_rect.left + 30
        return rect

    def get_total_coins_earned_text(self):
        text = self.small_font.render(f"Total coins earned: {self.parent.current_profile.total_coins_earned}", True, (255, 255, 255))
        return text

    def get_total_coins_earned_text_rect(self):
        rect = self.total_enemies_killed_text.get_rect()
        rect.top = self.total_enemies_killed_text_rect.bottom + 10
        rect.left = self.statistics_background_rect.left + 30
        return rect

    def get_time_text(self):
        time_spent = self.parent.current_profile.total_time
        days, hours, minutes, seconds = str(time_spent.days).zfill(2), str(time_spent.seconds // 3600).zfill(2), str(time_spent.seconds // 60 % 60).zfill(2), str(time_spent.seconds).zfill(2)

        text = self.small_font.render(f"Time spent: {days}:{hours}:{minutes}:{seconds}.s", True, (255, 255, 255))
        return text

    def get_time_text_rect(self):
        rect = self.total_enemies_killed_text.get_rect()
        rect.top = self.total_coins_earned_text_rect.bottom + 10
        rect.left = self.statistics_background_rect.left + 30
        return rect

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)
        return button

    def render(self, screen):
        self.app.background.draw(screen)
        screen.blit(self.statistics_text, self.statistics_text_rect)
        screen.blit(self.statistics_background, self.statistics_background_rect)
        screen.blit(self.highest_score_text, self.highest_score_text_rect)
        screen.blit(self.highest_wave_text, self.highest_wave_text_rect)
        screen.blit(self.total_enemies_killed_text, self.total_enemies_killed_text_rect)
        screen.blit(self.total_coins_earned_text, self.total_coins_earned_text_rect)
        screen.blit(self.time_text, self.time_text_rect)
        self.manager.draw_ui(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                self.app.is_running = False
                pygame.quit()
                exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.previous_scene

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes['GameMenuScene']

            self.manager.process_events(event)
        self.manager.update(time_delta)
