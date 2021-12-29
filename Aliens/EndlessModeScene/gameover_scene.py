import pygame
import pygame_gui
import os.path

from datetime import datetime
from Aliens import SETTINGS
from Aliens.EndlessGameCore.gamecore import GameState


class GameOverScene:
    def __init__(self, game):
        pygame.font.init()
        self.game = game
        self.manager = self.prepare_manager()
        self.game_over_background, self.game_over_background_rect = self.load_background()
        self.big_font, self.small_font = self.load_fonts()

        self.game_over_text = self.get_game_over_text()
        self.game_over_text_rect = self.get_game_over_text_rect()
        self.score_text = self.get_score_text()
        self.score_text_rect = self.get_score_text_rect()
        self.wave_text = self.get_wave_text()
        self.wave_text_rect = self.get_wave_text_rect()
        self.coins_text = self.get_coins_text()
        self.coins_text_rect = self.get_coins_text_rect()
        self.total_killed_text = self.get_total_killed_text()
        self.total_killed_text_rect = self.get_total_killed_text_rect()
        self.time_spent_text = self.get_time_spent_text()
        self.time_spent_text_rect = self.get_time_spent_text_rect()

        self.game_menu_button = self.prepare_game_menu_button()
        self.play_again_button = self.prepare_play_again_button()

    def refactor_ui(self):
        self.manager = self.prepare_manager()
        self.game_over_background, self.game_over_background_rect = self.load_background()
        self.big_font, self.small_font = self.load_fonts()

        self.game_over_text = self.get_game_over_text()
        self.game_over_text_rect = self.get_game_over_text_rect()
        self.score_text = self.get_score_text()
        self.score_text_rect = self.get_score_text_rect()
        self.wave_text = self.get_wave_text()
        self.wave_text_rect = self.get_wave_text_rect()
        self.coins_text = self.get_coins_text()
        self.coins_text_rect = self.get_coins_text_rect()
        self.total_killed_text = self.get_total_killed_text()
        self.total_killed_text_rect = self.get_total_killed_text_rect()
        self.time_spent_text = self.get_time_spent_text()
        self.time_spent_text_rect = self.get_time_spent_text_rect()

        self.game_menu_button = self.prepare_game_menu_button()
        self.play_again_button = self.prepare_play_again_button()

    def update(self):
        self.game_over_text = self.get_game_over_text()
        self.score_text = self.get_score_text()
        self.wave_text = self.get_wave_text()
        self.coins_text = self.get_coins_text()
        self.total_killed_text = self.get_total_killed_text()
        self.time_spent_text = self.get_time_spent_text()

    def prepare_manager(self):
        return pygame_gui.UIManager(SETTINGS.WINDOW_SIZE, 'Data/gui_theme.json')

    def load_background(self):
        images_folder = os.path.join("Data", "Sprites", "Background")
        filename = "small_bg.png"
        background = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        rect = background.get_rect()
        rect.center = (SETTINGS.WINDOW_WIDTH // 2, SETTINGS.WINDOW_HEIGHT // 2)
        return background, rect

    def load_fonts(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), 80)
        small_font = pygame.font.Font(os.path.join(fonts_path, font_name), 30)

        return big_font, small_font

    def get_game_over_text(self):
        text = self.big_font.render("Game Over", True, (255, 255, 255))
        return text

    def get_game_over_text_rect(self):
        rect = self.game_over_text.get_rect()
        rect.centerx = self.game_over_background_rect.centerx
        rect.y = self.game_over_background_rect.top + 20
        return rect

    def get_score_text(self):
        text = self.small_font.render(f"Score: {self.game.score}", True, (255, 255, 255))
        return text

    def get_score_text_rect(self):
        rect = self.score_text.get_rect()
        rect.top = self.game_over_text_rect.bottom + 10
        rect.left = self.game_over_background_rect.left + 40
        return rect

    def get_wave_text(self):
        text = self.small_font.render(f"Wave: {self.game.wave.wave_number}", True, (255, 255, 255))
        return text

    def get_wave_text_rect(self):
        rect = self.score_text.get_rect()
        rect.top = self.score_text_rect.bottom + 10
        rect.left = self.game_over_background_rect.left + 40
        return rect

    def get_coins_text(self):
        text = self.small_font.render(f"Coins: {self.game.coins_earned}", True, (255, 255, 255))
        return text

    def get_coins_text_rect(self):
        rect = self.score_text.get_rect()
        rect.top = self.wave_text_rect.bottom + 10
        rect.left = self.game_over_background_rect.left + 40
        return rect

    def get_total_killed_text(self):
        text = self.small_font.render(f"Total killed: {self.game.total_killed}", True, (255, 255, 255))
        return text

    def get_total_killed_text_rect(self):
        rect = self.score_text.get_rect()
        rect.top = self.coins_text_rect.bottom + 10
        rect.left = self.game_over_background_rect.left + 40
        return rect

    def get_time_spent_text(self):
        now = datetime.now()
        time_spent = now - self.game.start_time
        hours, minutes, seconds = str(time_spent.seconds // 3600).zfill(2), str(time_spent.seconds // 60 % 60).zfill(2), str(time_spent.seconds).zfill(2)

        text = self.small_font.render(f"Time spent: {hours}:{minutes}:{seconds}", True, (255, 255, 255))
        return text

    def get_time_spent_text_rect(self):
        rect = self.score_text.get_rect()
        rect.top = self.total_killed_text_rect.bottom + 10
        rect.left = self.game_over_background_rect.left + 40
        return rect

    def prepare_game_menu_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.game_over_background_rect.centerx - 210, self.game_over_background_rect.bottom - 95, 200, 75), text="GAME MENU",
            manager=self.manager)
        return button

    def prepare_play_again_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.game_over_background_rect.centerx + 10, self.game_over_background_rect.bottom - 95, 200, 75), text="PLAY AGAIN",
            manager=self.manager)
        return button

    def render(self, screen):
        screen.blit(self.game_over_background, self.game_over_background_rect)
        screen.blit(self.game_over_text, self.game_over_text_rect)
        screen.blit(self.score_text, self.score_text_rect)
        screen.blit(self.wave_text, self.wave_text_rect)
        screen.blit(self.coins_text, self.coins_text_rect)
        screen.blit(self.total_killed_text, self.total_killed_text_rect)
        screen.blit(self.time_spent_text, self.time_spent_text_rect)
        self.manager.draw_ui(screen)

    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.game_menu_button:
                    self.game.state = GameState.GAME_OFF
                elif event.ui_element == self.play_again_button:
                    self.game.save_progress()
                    self.game.new_game()
                    self.game.state = GameState.GAME_ON
        self.manager.process_events(event)
