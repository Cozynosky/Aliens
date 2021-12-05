import pygame
import pygame_gui
from Aliens import app
from Aliens.scene import Scene
from Aliens.settings import *
from sys import exit


class GameMenu(Scene):
    def __init__(self, parent):
        super(GameMenu, self).__init__(parent)
        # background
        self.background = pygame.Surface(WINDOW_SIZE)
        self.background.fill(pygame.Color('#DDDDDD'))
        # game logo
        pygame.font.init()
        self.game_logo = pygame.Surface((500, 200))
        self.game_logo.fill(pygame.Color('#808080'))
        # logo text
        myfont = pygame.font.SysFont('Arial', 150)
        textsurface = myfont.render('Aliens!', True, (0, 0, 0))
        self.game_logo.blit(textsurface, (65, 10))
        # init prepare manager
        self.manager = pygame_gui.UIManager(WINDOW_SIZE)
        # prepare buttons
        self.adventure_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_WIDTH // 2 - 150, 300, 300, 75), text="ADVENTURE MODE",
            manager=self.manager)
        self.endless_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_WIDTH // 2 - 150, 375, 300, 75), text="ENDLESS MODE",
            manager=self.manager)
        self.upgrades_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_WIDTH // 2 - 150, 450, 300, 75),
            text="UPGRADES",
            manager=self.manager)
        self.statistics_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_WIDTH // 2 - 150, 525, 300, 75),
            text="STATISTICS",
            manager=self.manager)
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, WINDOWS_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)
        self.exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_WIDTH - 125, WINDOWS_HEIGHT - 75, 100, 50), text="EXIT",
            manager=self.manager)

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.game_logo, (WINDOW_WIDTH // 2 - 250, 50))
        self.manager.draw_ui(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                app.is_running = False
                pygame.quit()
                exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.endless_button:
                        self.app.current_scene = self.app.game_scenes['EndlessMode']
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.game_scenes['MainMenu']
                    if event.ui_element == self.exit_button:
                        pygame.quit()
                        exit()
            self.manager.process_events(event)
        self.manager.update(time_delta)
