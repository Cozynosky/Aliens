import pygame
import pygame_gui
from Aliens import app
from Aliens.scene import Scene
from Aliens.constraints import *
from sys import exit


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        # background
        self.background = pygame.Surface(WINDOW_SIZE)
        self.background.fill(pygame.Color('#FFFFFF'))
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
        self.play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_SIZE[0] // 2 - 150, 300, 300, 75), text="PLAY",
            manager=self.manager)
        self.settings_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_SIZE[0] // 2 - 150, 375, 300, 75), text="SETTINGS",
            manager=self.manager)
        self.instructions_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_SIZE[0] // 2 - 150, 450, 300, 75),
            text="INSTRUCTIONS",
            manager=self.manager)
        self.exit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(WINDOW_SIZE[0] - 125, WINDOW_SIZE[1] - 75, 100, 50), text="EXIT",
            manager=self.manager)

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.game_logo, (WINDOW_SIZE[0] // 2 - 250, 90))
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
                    if event.ui_element == self.play_button:
                        pass
                    if event.ui_element == self.settings_button:
                        pass
                    if event.ui_element == self.instructions_button:
                        pass
                    if event.ui_element == self.exit_button:
                        pygame.quit()
                        exit()
            self.manager.process_events(event)
        self.manager.update(time_delta)
