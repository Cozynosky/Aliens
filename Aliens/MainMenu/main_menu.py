import pygame
import pygame_gui

from Aliens import SETTINGS
from Aliens.scene import Scene
from sys import exit


class MainMenu(Scene):
    def __init__(self, parent):
        super(MainMenu, self).__init__(parent)
        pygame.font.init()
        # background
        self.background = self.prepare_background()
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()
        # ui manager
        self.manager = self.prepare_manager()
        # buttons
        self.play_button = self.prepare_play_button()
        self.settings_button = self.prepare_settings_button()
        self.instructions_button = self.prepare_instructions_button()
        self.exit_button = self.prepare_exit_button()

    def refactor_ui(self):
        # background
        self.background = self.prepare_background()
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()
        # ui manager
        self.manager = self.prepare_manager()
        # buttons
        self.play_button = self.prepare_play_button()
        self.settings_button = self.prepare_settings_button()
        self.instructions_button = self.prepare_instructions_button()
        self.exit_button = self.prepare_exit_button()

    def prepare_background(self):
        background = pygame.Surface(SETTINGS.WINDOW_SIZE)
        background.fill(pygame.Color('#DDDDDD'))
        return background

    def prepare_game_logo(self):
        game_logo = pygame.Surface((500, 200))
        game_logo.fill(pygame.Color('#808080'))
        game_logo_rect = game_logo.get_rect()
        game_logo_rect.centerx = self.app.screen.get_rect().centerx
        game_logo_rect.y = 50
        myfont = pygame.font.SysFont('Arial', 150)
        textsurface = myfont.render('Aliens!', True, (0, 0, 0))
        game_logo.blit(textsurface, (65, 10))
        return game_logo, game_logo_rect

    def prepare_manager(self):
        return pygame_gui.UIManager(SETTINGS.WINDOW_SIZE)

    def prepare_play_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 150, self.game_logo_rect.bottom + 50, 300, 75), text="PLAY",
            manager=self.manager)
        return button

    def prepare_settings_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 150, self.game_logo_rect.bottom + 125, 300, 75), text="SETTINGS",
            manager=self.manager)
        return button

    def prepare_instructions_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 150, self.game_logo_rect.bottom + 200, 300, 75), text="INSTRUCTIONS",
            manager=self.manager)
        return button

    def prepare_exit_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH - 125, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="EXIT",
            manager=self.manager)
        return button

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.game_logo, self.game_logo_rect)
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
                    if event.ui_element == self.play_button:
                        self.app.current_scene = self.app.game_scenes['GameMenu']
                    if event.ui_element == self.settings_button:
                        self.app.current_scene = self.app.game_scenes['SettingsMenu']
                    if event.ui_element == self.instructions_button:
                        pass
                    if event.ui_element == self.exit_button:
                        pygame.quit()
                        exit()
            self.manager.process_events(event)
        self.manager.update(time_delta)
