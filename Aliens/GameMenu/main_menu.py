import pygame
import pygame_gui
from Aliens import app
from Aliens.scene import Scene
from Aliens.constraints import *
from sys import exit


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.Surface(WINDOW_SIZE)
        self.background.fill(pygame.Color('#FFFFFF'))
        self.manager = pygame_gui.UIManager(WINDOW_SIZE)
        # prepare buttons
        self.button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text="Press me", manager=self.manager)

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.background, (0, 0))
        self.manager.draw_ui(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60)/1000.0
        for event in events:
            if event.type == pygame.QUIT:
                app.is_running = False
                pygame.quit()
                exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.button:
                        print("hello world")
            self.manager.process_events(event)
        self.manager.update(time_delta)