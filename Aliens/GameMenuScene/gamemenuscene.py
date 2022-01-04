import pygame
import pygame_gui
import os.path

from Aliens.scene import Scene
from Aliens import SETTINGS
from Aliens.Profile.save_profiles import save_profiles


class GameMenuScene(Scene):
    def __init__(self, parent):
        super(GameMenuScene, self).__init__(parent)
        pygame.font.init()
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()

        # prepare buttons
        self.adventure_button = self.prepare_adventure_button()
        self.endless_button = self.prepare_endless_button()
        self.upgrades_button = self.prepare_upgrades_button()
        self.statistics_button = self.prepare_statistics_button()
        self.logout_button = self.prepare_logout_button()
        self.save_button = self.prepare_save_button()
        self.game_saved_text = self.prepare_game_saved_text()
        self.game_saved_text_rect = self.prepare_game_saved_text_rect()
        self.back_button = self.prepare_back_button()
        self.exit_button = self.prepare_exit_button()

    def refactor_ui(self):
        # ui manager
        self.manager = self.prepare_manager()
        # game logo
        self.game_logo, self.game_logo_rect = self.prepare_game_logo()

        # prepare buttons
        self.adventure_button = self.prepare_adventure_button()
        self.endless_button = self.prepare_endless_button()
        self.upgrades_button = self.prepare_upgrades_button()
        self.statistics_button = self.prepare_statistics_button()
        self.logout_button = self.prepare_logout_button()
        self.save_button = self.prepare_save_button()
        self.game_saved_text = self.prepare_game_saved_text()
        self.game_saved_text_rect = self.prepare_game_saved_text_rect()
        self.back_button = self.prepare_back_button()
        self.exit_button = self.prepare_exit_button()

    def prepare_game_logo(self):
        game_logo = pygame.Surface((500, 200))
        game_logo.fill(pygame.Color('#808080'))
        game_logo_rect = game_logo.get_rect()
        game_logo_rect.centerx = SETTINGS.WINDOW_WIDTH // 2
        game_logo_rect.y = 50

        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"
        myfont = pygame.font.Font(os.path.join(fonts_path, font_name), 125)
        text = myfont.render('Aliens!', True, (255, 255, 255))
        text_rect = game_logo.get_rect()
        text_rect.x = 25
        text_rect.y = 30
        game_logo.blit(text, text_rect)
        return game_logo, game_logo_rect

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

    def prepare_logout_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, 25, 80, 32),
            text="Logout", manager=self.manager, object_id=pygame_gui.core.ObjectID(class_id="@logout_button", object_id="@logout_button")
        )
        return button

    def prepare_save_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, 58, 80, 32),
            text="Save", manager=self.manager, object_id=pygame_gui.core.ObjectID(class_id="@save_button", object_id="@save_button")
        )
        return button

    def prepare_game_saved_text(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"
        myfont = pygame.font.Font(os.path.join(fonts_path, font_name), 15)
        text = myfont.render("Game saved", True, (255, 255, 255))
        text.set_alpha(0)
        return text

    def prepare_game_saved_text_rect(self):
        rect = self.game_saved_text.get_rect()
        rect.centery = 74
        rect.x = 110
        return rect

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
        super(GameMenuScene, self).update()
        alpha = self.game_saved_text.get_alpha()
        if alpha > 0:
            self.game_saved_text.set_alpha(alpha - 5)

    def render(self, screen):
        self.app.background.draw(screen)
        screen.blit(self.game_logo, (SETTINGS.WINDOW_WIDTH // 2 - 250, 50))
        screen.blit(self.game_saved_text, self.game_saved_text_rect)
        self.manager.draw_ui(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                self.app.close_app()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes["MainMenuScene"]
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.endless_button:
                        self.app.current_scene = self.app.game_scenes['EndlessModeScene']
                        self.app.current_scene.game.new_game()
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.game_scenes['MainMenuScene']
                    if event.ui_element == self.upgrades_button:
                        self.app.current_scene = self.app.game_scenes['UpgradesScene']
                    if event.ui_element == self.statistics_button:
                        self.app.current_scene = self.app.game_scenes['StatisticsScene']
                    if event.ui_element == self.logout_button:
                        self.app.profile_selected = False
                        self.app.current_scene = self.app.game_scenes['ProfileScene']
                    if event.ui_element == self.save_button:
                        save_profiles(self.app.profiles)
                        self.game_saved_text.set_alpha(256)
                    if event.ui_element == self.exit_button:
                        self.app.close_app()
            self.manager.process_events(event)
        self.manager.update(time_delta)
