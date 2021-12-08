import pygame
import pygame_gui
from Aliens import app
from Aliens.scene import Scene
from Aliens.settings import *
from sys import exit


class Settings(Scene):
    def __init__(self, parent):
        super(Settings, self).__init__(parent)
        # background
        self.background = pygame.Surface(WINDOW_SIZE)
        self.background.fill(pygame.Color('#DDDDDD'))
        # game logo
        pygame.font.init()
        self.game_logo = pygame.Surface((400, 150))
        self.game_logo.fill(pygame.Color('#808080'))
        # logo text
        myfont = pygame.font.SysFont('Arial', 100)
        textsurface = myfont.render('Settings', True, (0, 0, 0))
        self.game_logo.blit(textsurface, (50, 10))
        # init prepare manager
        self.manager = pygame_gui.UIManager(WINDOW_SIZE)
        # prepare buttons
        self.resolution_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(450, 300, 100, 40), text="Resolution", manager=self.manager)
        self.resolution_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(600, 300, 250, 40), manager=self.manager, options_list=["opt a", "opt b"], starting_option="opt a")
        self.fullscreen_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(450, 350, 100, 40),
                                                            text="Fullscreen", manager=self.manager)
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, WINDOWS_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.game_logo, (WINDOW_WIDTH // 2 - 200, 50))
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
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.game_scenes['MainMenu']
            self.manager.process_events(event)
        self.manager.update(time_delta)
