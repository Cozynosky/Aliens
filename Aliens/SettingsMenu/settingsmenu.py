from sys import exit

import pygame
import pygame_gui

from Aliens import SETTINGS

from Aliens.scene import Scene


class SettingsMenu(Scene):
    def __init__(self, parent):
        super(SettingsMenu, self).__init__(parent)
        pygame.font.init()
        # background
        self.background = self.prepare_background()
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()
        # ui manager
        self.manager = self.prepare_manager()
        # labels
        self.resolution_label = self.prepare_resolution_label()
        self.fullscreen_label = self.prepare_fullscreen_label()
        # dropdown
        self.resolution_dropdown = self.prepare_resolution_dropdown()
        # button
        self.fullscreen_button = self.prepare_fullscreen_button()
        self.back_button = self.prepare_back_button()

    def refactor_ui(self):
        # background
        self.background = self.prepare_background()
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()
        # ui manager
        self.manager = self.prepare_manager()
        # labels
        self.resolution_label = self.prepare_resolution_label()
        self.fullscreen_label = self.prepare_fullscreen_label()
        # dropdown
        self.resolution_dropdown = self.prepare_resolution_dropdown()
        # button
        self.fullscreen_button = self.prepare_fullscreen_button()
        self.back_button = self.prepare_back_button()

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

    def prepare_resolution_label(self):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(450, 300, 100, 40),
                                                       text="Resolution", manager=self.manager)
        return label

    def prepare_fullscreen_label(self):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(450, 350, 100, 40),
                                                            text="Fullscreen", manager=self.manager)
        return label

    def prepare_resolution_dropdown(self):
        resolution_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(600, 300, 250, 40),
                                                                 manager=self.manager,
                                                                 options_list=SETTINGS.RESOLUTIONS.keys(),
                                                                 starting_option=f"{SETTINGS.WINDOW_WIDTH} x {SETTINGS.WINDOW_HEIGHT}")
        return resolution_dropdown

    def prepare_fullscreen_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(600, 350, 100, 40), text=f"{SETTINGS.FULLSCREEN}",
            manager=self.manager)
        return button

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
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
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.game_scenes['MainMenu']
                    if event.ui_element == self.fullscreen_button:
                        SETTINGS.FULLSCREEN = not SETTINGS.FULLSCREEN
                        self.app.refactor_ui()

                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    SETTINGS.WINDOW_SIZE = (SETTINGS.RESOLUTIONS[event.text]["width"], SETTINGS.RESOLUTIONS[event.text]["height"])
                    SETTINGS.WINDOW_WIDTH = int(event.text.split(" x ")[0])
                    SETTINGS.WINDOW_HEIGHT = int(event.text.split(" x ")[1])
                    SETTINGS.SCALE = SETTINGS.prepare_scale()
                    self.app.refactor_ui()
            self.manager.process_events(event)
        self.manager.update(time_delta)
