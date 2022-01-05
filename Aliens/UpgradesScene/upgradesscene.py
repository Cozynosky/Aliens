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
        self.banner_text = self.prepare_banner_text()
        self.banner_text_rect = self.get_banner_text_rect()
        # upgrades
        self.upgrades_cards = UpgradesCardsGroup(self.manager, self.parent)
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
        # upgrades
        self.upgrades_cards.refactor(self.manager)
        # coins
        self.coin_icon = self.prepare_coin_icon()
        self.coin_icon_rect = self.get_coin_icon_rect()
        self.coin_text = self.prepare_coin_text()
        self.coin_text_rect = self.get_coin_text_rect()
        self.back_button = self.prepare_back_button()

    def update(self):
        super(UpgradesScene, self).update()
        self.coin_text = self.prepare_coin_text()
        self.upgrades_cards.update()

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

        return background, background_rect

    def prepare_banner_text(self):
        text = self.banner_font.render('Upgrades', True, (255, 255, 255))
        return text

    def get_banner_text_rect(self):
        rect = self.banner_text.get_rect()
        rect.x = 300 * SETTINGS.SCALE
        rect.centery = self.upgrades_banner_rect.centery

        return rect

    def prepare_coin_icon(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        coin = pygame.image.load(os.path.join(images_folder, "coin.png")).convert_alpha()
        return coin

    def get_coin_icon_rect(self):
        rect = self.coin_icon.get_rect()
        rect.centery = self.upgrades_banner_rect.centery
        rect.x = self.banner_text_rect.right + 40
        return rect

    def prepare_coin_text(self):
        text = self.banner_font.render(f'{self.parent.current_profile.coins}', True, (255, 255, 255))
        return text

    def get_coin_text_rect(self):
        rect = self.coin_text.get_rect()
        rect.centery = self.upgrades_banner_rect.centery
        rect.x = self.coin_icon_rect.right + 10
        return rect

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)
        return button

    def render(self, screen):
        self.app.background.draw(screen)
        screen.blit(self.upgrades_banner, self.upgrades_banner_rect)
        screen.blit(self.banner_text, self.banner_text_rect)
        screen.blit(self.coin_icon, self.coin_icon_rect)
        screen.blit(self.coin_text, self.coin_text_rect)
        self.upgrades_cards.render(screen)
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

            self.upgrades_cards.handle_events(event)
            self.manager.process_events(event)
        self.manager.update(time_delta)
        self.upgrades_cards.update_manager(time_delta)


class UpgradesCardsGroup:
    def __init__(self, manager, app):
        self.manager = manager
        self.app = app
        self.cards_surface_rect = self.get_cards_surface_rect()
        self.cards = [
            UpgradeCard(0, 0, "ship_speed.png", self.manager, self.app.current_profile.ship_speed, self.cards_surface_rect, self.app),
            UpgradeCard(0, 0 + 175, "health_capacity.png", self.manager,self.app.current_profile.health_capacity, self.cards_surface_rect, self.app),
            UpgradeCard(0, 0 + 350, "lives.png", self.manager, self.app.current_profile.lives, self.cards_surface_rect, self.app),
            UpgradeCard(0 + 130, 0, "bullet_speed.png", self.manager,self.app.current_profile.bullet_speed, self.cards_surface_rect, self.app),
            UpgradeCard(0 + 130, 0 + 175, "bullet_damage.png", self.manager, self.app.current_profile.bullet_damage, self.cards_surface_rect, self.app),
            UpgradeCard(0 + 130, 0 + 350, "bullets_in_shot.png", self.manager, self.app.current_profile.bullets_in_shot, self.cards_surface_rect, self.app),
            UpgradeCard(0 + 260, 0 + 175, "magazine_size.png", self.manager, self.app.current_profile.magazine_size, self.cards_surface_rect, self.app),
            UpgradeCard(0 + 260, 0, "reload_time.png", self.manager, self.app.current_profile.reload_time, self.cards_surface_rect, self.app),
            UpgradeCard(0 + 390, 0, "drop_rate.png", self.manager, self.app.current_profile.drop_rate, self.cards_surface_rect, self.app),
            UpgradeCard(0 + 390, 0 + 175, "coin_value.png", self.manager, self.app.current_profile.coin_value, self.cards_surface_rect, self.app)

        ]

    def get_cards_surface_rect(self):
        rect = pygame.rect.Rect(SETTINGS.WINDOW_WIDTH / 2 - 235, 240 * SETTINGS.SCALE, 470, 500)
        return rect

    def update(self):
        for card in self.cards:
            card.update()

    def handle_events(self, event):
        for card in self.cards:
            card.handle_events(event)

    def update_manager(self, timedelta):
        for card in self.cards:
            card.update_manager(timedelta)

    def refactor(self, manager):
        self.manager = manager
        self.cards_surface_rect.centerx = SETTINGS.WINDOW_WIDTH / 2
        self.cards_surface_rect.y = 240 * SETTINGS.SCALE
        for card in self.cards:
            card.manager = self.manager
            card.parent_rect = self.cards_surface_rect
            card.refactor()

    def render(self, screen):
        for upgrade in self.cards:
            upgrade.render(screen)


class UpgradeCard:
    def __init__(self, x, y, file_name, manager, upgrade, parent_rect, app):
        self.app = app
        self.parent_rect = parent_rect
        self.upgrade = upgrade
        self.manager = manager
        self.filename = file_name
        self.x = x
        self.y = y
        self.font = self.prepare_font()

        self.image = self.load_image()
        self.image_rect = self.get_image_rect(self.x, self.y)
        self.level_text = self.prepare_level_text()
        self.level_text_rect = self.get_level_text_rect()
        self.value_text = self.prepare_value_text()
        self.value_text_rect = self.get_value_text_rect()
        self.cost_text = self.prepare_cost_text()
        self.cost_text_rect = self.get_cost_text_rect()
        self.coin_icon = self.prepare_coin_icon()
        self.coin_icon_rect = self.get_coin_icon_rect()
        self.buy_button = self.prepare_buy_button()

    def refactor(self):
        self.buy_button = self.prepare_buy_button()

    def update(self):
        if self.upgrade.get_cost() > self.app.current_profile.coins or self.upgrade.is_max():
            self.buy_button.disable()
        else:
            self.buy_button.enable()

        self.level_text = self.prepare_level_text()
        self.level_text_rect = self.get_level_text_rect()
        self.value_text = self.prepare_value_text()
        self.value_text_rect = self.get_value_text_rect()
        self.cost_text = self.prepare_cost_text()
        self.cost_text_rect = self.get_cost_text_rect()
        self.coin_icon = self.prepare_coin_icon()
        self.coin_icon_rect = self.get_coin_icon_rect()

    def prepare_font(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"
        font = pygame.font.Font(os.path.join(fonts_path, font_name), 20)
        return font

    def load_image(self):
        images_folder = os.path.join("Data", "Sprites", "Upgrades")
        try:
            image = pygame.image.load(os.path.join(images_folder, f"{self.filename}")).convert_alpha()
        except Exception:
            image = pygame.image.load(os.path.join(images_folder, "bg.png")).convert_alpha()
        return image

    def get_image_rect(self, x, y):
        rect = self.image.get_rect()
        rect.x = x
        rect.y = y
        return rect

    def prepare_level_text(self):
        if self.upgrade.is_max():
            text = "Max lvl"
        else:
            text = f'{self.upgrade.get_level()} lvl'
        text = self.font.render(text, True, (255, 255, 255))
        text = pygame.transform.rotate(text, 45)
        return text

    def get_level_text_rect(self):
        rect = self.level_text.get_rect()
        rect.centerx = self.image_rect.left + 10
        rect.centery = self.image_rect.top + 10
        return rect

    def prepare_value_text(self):
        text = self.font.render(f'{self.upgrade.get_value()}', True, (255, 255, 255))
        return text

    def get_value_text_rect(self):
        rect = self.value_text.get_rect()
        rect.centerx = self.image_rect.centerx
        rect.bottom = self.image_rect.bottom - 10
        return rect

    def prepare_cost_text(self):
        text = self.font.render(f'{self.upgrade.get_cost()}', True, (255, 255, 255))
        return text

    def get_cost_text_rect(self):
        rect = self.cost_text.get_rect()
        rect.centerx = self.image_rect.centerx + 15
        rect.y = self.image_rect.bottom + 8
        return rect

    def prepare_coin_icon(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        coin = pygame.image.load(os.path.join(images_folder, "coin.png")).convert_alpha()
        coin = pygame.transform.smoothscale(coin, (20, 20))
        return coin

    def get_coin_icon_rect(self):
        rect = self.coin_icon.get_rect()
        rect.centery = self.cost_text_rect.centery
        rect.right = self.cost_text_rect.left - 10
        return rect

    def prepare_buy_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                self.image_rect.x + self.parent_rect.x,
                self.cost_text_rect.bottom + 8 + self.parent_rect.y,
                self.image_rect.width, 32),
            text="Buy", object_id=pygame_gui.core.ObjectID(object_id="@buy_upgrade_button", class_id="@buy_upgrade_button"),
            manager=self.manager)
        return button

    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.buy_button:
                    self.app.current_profile.coins -= self.upgrade.get_cost()
                    self.upgrade.upgrade_bought()
            self.manager.process_events(event)

    def update_manager(self, timedelta):
        self.manager.update(timedelta)

    def render(self, screen):
        screen.blit(self.image, (self.parent_rect.x + self.image_rect.x, self.parent_rect.y + self.image_rect.y))
        screen.blit(self.level_text, (self.parent_rect.x + self.level_text_rect.x, self.parent_rect.y + self.level_text_rect.y))
        screen.blit(self.value_text, (self.parent_rect.x + self.value_text_rect.x, self.parent_rect.y + self.value_text_rect.y))
        screen.blit(self.cost_text, (self.parent_rect.x + self.cost_text_rect.x, self.parent_rect.y + self.cost_text_rect.y))
        screen.blit(self.coin_icon, (self.parent_rect.x + self.coin_icon_rect.x, self.parent_rect.y + self.coin_icon_rect.y))
