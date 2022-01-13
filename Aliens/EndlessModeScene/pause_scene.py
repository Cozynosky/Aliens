import pygame
import pygame_gui
import os.path

from datetime import datetime
from Aliens import SETTINGS
from Aliens.EndlessGameCore.gamecore import GameState


class PauseScene:
    def __init__(self, parent_scene):
        pygame.font.init()
        self.parent_scene = parent_scene
        self.game = parent_scene.game
        self.manager = self.prepare_manager()
        self.pause_background, self.pause_background_rect = self.load_background()
        self.pause_text = self.get_pause_text()
        self.pause_text_rect = self.get_pause_text_rect()
        self.resume_button = self.prepare_resume_button()
        self.game_menu_button = self.prepare_game_menu_button()
        self.exit_game_button = self.prepare_exit_game_button()

    def prepare_manager(self):
        return pygame_gui.UIManager(SETTINGS.WINDOW_SIZE, 'Data/default_theme.json')

    def load_background(self):
        images_folder = os.path.join("Data", "Sprites", "Background")
        filename = "small_bg.png"
        background = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        rect = background.get_rect()
        rect.center = (SETTINGS.WINDOW_WIDTH // 2, SETTINGS.WINDOW_HEIGHT // 2)
        return background, rect

    def get_pause_text(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        pause_font = pygame.font.Font(os.path.join(fonts_path, font_name), 100)
        pause_text = pause_font.render("Pause", True, (255, 255, 255))
        return pause_text

    def get_pause_text_rect(self):
        rect = self.pause_text.get_rect()
        rect.centerx = self.pause_background_rect.centerx
        rect.y = self.pause_background_rect.top + 20

        return rect

    def prepare_resume_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.pause_background_rect.centerx - 150, self.pause_text_rect.bottom + 20, 300, 75),
            text="RESUME",
            manager=self.manager)
        return button

    def prepare_game_menu_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.pause_background_rect.centerx - 150, self.pause_text_rect.bottom + 105, 300, 75),
            text="GAME MENU",
            manager=self.manager)
        return button

    def prepare_exit_game_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.pause_background_rect.centerx - 150, self.pause_text_rect.bottom + 190, 300, 75),
            text="EXIT GAME",
            manager=self.manager)
        return button

    def refactor_ui(self):
        self.manager = self.prepare_manager()
        self.pause_background, self.pause_background_rect = self.load_background()
        self.pause_text = self.get_pause_text()
        self.pause_text_rect = self.get_pause_text_rect()
        self.resume_button = self.prepare_resume_button()
        self.game_menu_button = self.prepare_game_menu_button()
        self.exit_game_button = self.prepare_exit_game_button()

    def render(self, screen):
        screen.blit(self.pause_background, self.pause_background_rect)
        screen.blit(self.pause_text, self.pause_text_rect)
        self.manager.draw_ui(screen)

    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.resume_button:
                    pygame.mouse.set_visible(not pygame.mouse.get_visible())
                    self.game.paused = False
                    self.parent_scene.app.background.animate_background = True
                elif event.ui_element == self.game_menu_button:
                    self.game.state = GameState.GAME_OFF
                    self.game.paused = False
                elif event.ui_element == self.exit_game_button:
                    self.game.end_time = datetime.now()
                    self.game.save_progress()
                    self.parent_scene.app.close_app()
        self.manager.process_events(event)

