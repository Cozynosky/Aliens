import pygame
import pygame_gui
import os.path

from Aliens import SETTINGS
from Aliens.scene import Scene


class UpgradesScene(Scene):
    def __init__(self, parent):
        super(UpgradesScene, self).__init__(parent)
        self.parent = parent
        pygame.font.init()
        # prepare font
        self.banner_font = self.load_fonts()
        # banner at the top
        self.upgrades_banner, self.upgrades_banner_rect = self.prepare_upgrades_banner()
        # coins
        self.coin_icon = self.prepare_coin_icon()
        self.coin_icon_rect = self.get_coin_icon_rect()
        self.coin_text = self.prepare_coin_text()
        self.coin_text_rect = self.get_coin_text_rect()
        self.back_button = self.prepare_back_button()

    def refactor_ui(self):
        self.manager = self.prepare_manager()
        # prepare font
        self.banner_font = self.load_fonts()
        # banner at the top
        self.upgrades_banner, self.upgrades_banner_rect = self.prepare_upgrades_banner()
        # coins
        self.coin_icon = self.prepare_coin_icon()
        self.coin_icon_rect = self.get_coin_icon_rect()
        self.coin_text = self.prepare_coin_text()
        self.coin_text_rect = self.get_coin_text_rect()
        self.back_button = self.prepare_back_button()

    def update(self):
        super(UpgradesScene, self).update()

    def load_fonts(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), 60)

        return big_font

    def prepare_upgrades_banner(self):
        # banner
        background = pygame.Surface((SETTINGS.WINDOW_WIDTH, 70))
        background.fill(pygame.Color('#808080'))
        background_rect = background.get_rect()
        background_rect.x = 0
        background_rect.y = 50

        # text
        text = self.banner_font.render('Upgrades', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 300 * SETTINGS.SCALE
        text_rect.centery = 35
        background.blit(text, text_rect)

        return background, background_rect

    def prepare_coin_icon(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        coin = pygame.image.load(os.path.join(images_folder, "coin.png")).convert_alpha()
        return coin

    def get_coin_icon_rect(self):
        rect = self.coin_icon.get_rect()
        rect.centery = self.upgrades_banner_rect.centery
        rect.x = 850 * SETTINGS.SCALE
        return rect

    def prepare_coin_text(self):
        text = self.banner_font.render(f'{self.parent.current_profile.coins}', True, (255, 255, 255))
        return text

    def get_coin_text_rect(self):
        rect = self.coin_text.get_rect()
        rect.centery = self.upgrades_banner_rect.centery
        rect.x = 930 * SETTINGS.SCALE
        return rect

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)
        return button

    def render(self, screen):
        self.app.background.draw(screen)
        screen.blit(self.upgrades_banner, self.upgrades_banner_rect)
        screen.blit(self.coin_icon, self.coin_icon_rect)
        screen.blit(self.coin_text, self.coin_text_rect)
        self.manager.draw_ui(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                self.app.close_app()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.game_scenes['GameMenuScene']

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes['GameMenuScene']

            self.manager.process_events(event)
        self.manager.update(time_delta)
