import pygame
import pygame_gui

from Aliens.scene import Scene
from Aliens import SETTINGS
from sys import exit


class GameMenu(Scene):
    def __init__(self, parent):
        super(GameMenu, self).__init__(parent)
        pygame.font.init()
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()
        # ui manager
        self.manager = self.prepare_manager()

        # prepare buttons
        self.adventure_button = self.prepare_adventure_button()
        self.endless_button = self.prepare_endless_button()
        self.upgrades_button = self.prepare_upgrades_button()
        self.statistics_button = self.prepare_statistics_button()
        self.back_button = self.prepare_back_button()
        self.exit_button = self.prepare_exit_button()

    def refactor_ui(self):
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()
        # ui manager
        self.manager = self.prepare_manager()

        # prepare buttons
        self.adventure_button = self.prepare_adventure_button()
        self.endless_button = self.prepare_endless_button()
        self.upgrades_button = self.prepare_upgrades_button()
        self.statistics_button = self.prepare_statistics_button()
        self.back_button = self.prepare_back_button()
        self.exit_button = self.prepare_exit_button()

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

    def prepare_adventure_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 150, 300, 300, 75), text="ADVENTURE MODE",
            manager=self.manager)

        return button

    def prepare_endless_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 150, 375, 300, 75), text="ENDLESS MODE",
            manager=self.manager)

        return button

    def prepare_upgrades_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 150, 450, 300, 75),
            text="UPGRADES",
            manager=self.manager)

        return button

    def prepare_statistics_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 150, 525, 300, 75),
            text="STATISTICS",
            manager=self.manager)

        return button

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
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
        self.app.background.draw(screen)
        screen.blit(self.game_logo, (SETTINGS.WINDOW_WIDTH // 2 - 250, 50))
        self.manager.draw_ui(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                self.app.is_running = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes["MainMenu"]
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.endless_button:
                        self.app.game_scenes['EndlessMode'].game.new_game()
                        self.app.current_scene = self.app.game_scenes['EndlessMode']
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.game_scenes['MainMenu']
                    if event.ui_element == self.exit_button:
                        pygame.quit()
                        exit()
            self.manager.process_events(event)
        self.manager.update(time_delta)
