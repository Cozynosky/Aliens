import pygame
import pygame_gui
import os.path

from Aliens import SETTINGS
from Aliens.scene import Scene
from Aliens.Profile.save_profiles import save_profiles


class ProfileScene(Scene):
    def __init__(self, parent):
        super(ProfileScene, self).__init__(parent)
        self.parent = parent
        pygame.font.init()
        # prepare font
        self.banner_font = self.load_fonts()
        # banner at the top
        self.profiles_banner, self.profiles_banner_rect = self.prepare_profiles_banner()
        # profiles
        self.profile_1_banner = ProfileBanner(self.app, self.app.profiles[0], self.manager, self.profiles_banner_rect.bottom + 30)
        self.profile_2_banner = ProfileBanner(self.app, self.app.profiles[1], self.manager, self.profile_1_banner.banner_rect.bottom + 20)
        self.profile_3_banner = ProfileBanner(self.app, self.app.profiles[2], self.manager, self.profile_2_banner.banner_rect.bottom + 20)
        self.back_button = self.prepare_back_button()

    def refactor_ui(self):
        self.manager = self.prepare_manager()
        # prepare font
        self.banner_font = self.load_fonts()
        # banner at the top
        self.profiles_banner, self.profiles_banner_rect = self.prepare_profiles_banner()

        self.profile_1_banner.refactor(self.manager)
        self.profile_2_banner.refactor(self.manager)
        self.profile_3_banner.refactor(self.manager)
        self.back_button = self.prepare_back_button()

    def update(self):
        super(ProfileScene, self).update()
        self.profile_1_banner.update()
        self.profile_2_banner.update()
        self.profile_3_banner.update()
        if self.app.profile_selected:
            self.app.current_scene = self.app.game_scenes['GameMenuScene']

    def load_fonts(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), 60)

        return big_font

    def prepare_profiles_banner(self):
        background = pygame.Surface((SETTINGS.WINDOW_WIDTH, 70))
        background.fill(pygame.Color('#808080'))
        background_rect = background.get_rect()
        background_rect.x = 0
        background_rect.y = 50

        text = self.banner_font.render('Select profile', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 300 * SETTINGS.SCALE
        text_rect.centery = 35
        background.blit(text, text_rect)
        return background, background_rect

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)
        return button

    def render(self, screen):
        self.app.background.draw(screen)
        screen.blit(self.profiles_banner, self.profiles_banner_rect)
        self.profile_1_banner.draw(screen)
        self.profile_2_banner.draw(screen)
        self.profile_3_banner.draw(screen)
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
                        self.app.current_scene = self.app.game_scenes['MainMenuScene']

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes['MainMenuScene']

            self.profile_1_banner.handle_events(event)
            self.profile_2_banner.handle_events(event)
            self.profile_3_banner.handle_events(event)

            self.manager.process_events(event)
        self.manager.update(time_delta)


class ProfileBanner:
    def __init__(self, app, profile, manager, y):
        self.app = app
        self.profile = profile
        self.manager = manager
        self.font = self.load_fonts()

        self.banner = self.prepare_banner()
        self.banner_rect = self.get_banner_rect(y)
        self.name_entry = self.prepare_name_entry()
        self.time_in_text = self.get_time_in_text()
        self.time_in_text_rect = self.get_time_in_text_rect()
        self.coins_icon = self.prepare_coins_icon()
        self.coins_icon_rect = self.get_coins_icon_rect()
        self.coins_text = self.get_coins_text()
        self.coins_text_rect = self.get_coins_text_rect()
        self.select_button = self.prepare_select_button()
        self.delete_button = self.prepare_delete_button()
        self.edit_button = self.prepare_edit_button()

    def refactor(self, manager):
        self.manager = manager
        self.font = self.load_fonts()

        self.banner = self.prepare_banner()
        self.banner_rect = self.get_banner_rect(self.banner_rect.y)
        self.name_entry = self.prepare_name_entry()
        self.time_in_text = self.get_time_in_text()
        self.time_in_text_rect = self.get_time_in_text_rect()
        self.coins_icon = self.prepare_coins_icon()
        self.coins_icon_rect = self.get_coins_icon_rect()
        self.coins_text = self.get_coins_text()
        self.coins_text_rect = self.get_coins_text_rect()
        self.select_button = self.prepare_select_button()
        self.delete_button = self.prepare_delete_button()
        self.edit_button = self.prepare_edit_button()

    def load_fonts(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        font = pygame.font.Font(os.path.join(fonts_path, font_name), 15)

        return font

    def update(self):
        self.time_in_text = self.get_time_in_text()
        self.coins_text = self.get_coins_text()
        if not self.name_entry.is_focused and self.name_entry.get_text() == "":
            self.set_profile_name()

    def reload(self):
        if self.profile.name == "":
            self.name_entry.set_text("Enter name")
        else:
            self.name_entry.set_text(self.profile.name)
        self.name_entry.disable()
        if self.profile.empty_profile:
            self.edit_button.visible = 0
        else:
            self.edit_button.visible = 1

    def prepare_banner(self):
        banner = pygame.surface.Surface((600, 100))
        banner.fill((128, 128, 128))
        return banner

    def get_banner_rect(self, y):
        rect = self.banner.get_rect()
        rect.centerx = SETTINGS.WINDOW_WIDTH//2
        rect.y = y
        return rect

    def prepare_name_entry(self):
        entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(self.banner_rect.left + 10, self.banner_rect.top + 10, 210, 120), manager=self.manager)
        entry.set_text_length_limit(10)
        if self.profile.name == "":
            entry.set_text("Enter name")
        else:
            entry.set_text(self.profile.name)
        entry.disable()
        return entry

    def get_time_in_text(self):
        time_spent = self.profile.total_time
        days, hours, minutes, seconds = str(time_spent.days).zfill(2), str(time_spent.seconds // 3600 % 24).zfill(2), str(time_spent.seconds // 60 % 60).zfill(2), str(time_spent.seconds % 60).zfill(2)

        text = self.font.render(f"Time in: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", True, (255, 255, 255))
        return text

    def get_time_in_text_rect(self):
        rect = self.time_in_text.get_rect()
        rect.left = self.banner_rect.left + 10
        rect.bottom = self.banner_rect.bottom - 10
        return rect

    def prepare_coins_icon(self):
        images_folder = os.path.join("Data", "Sprites", "HUD")
        filename = "coin.png"
        icon = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        icon = pygame.transform.smoothscale(icon, (16, 16))
        return icon

    def get_coins_icon_rect(self):
        rect = self.coins_icon.get_rect()
        rect.left = self.banner_rect.left + 10
        rect.bottom = self.time_in_text_rect.top - 5
        return rect

    def get_coins_text(self):
        text = self.font.render(f"{self.profile.coins}", True, (255, 255, 255))
        return text

    def get_coins_text_rect(self):
        rect = self.coins_text.get_rect()
        rect.y = self.coins_icon_rect.y
        rect.left = self.coins_icon_rect.right + 5
        return rect

    def prepare_select_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.banner_rect.right - 110, self.banner_rect.bottom - 50, 100, 40), text="Select",
            manager=self.manager, object_id=pygame_gui.core.ObjectID(object_id="@select_profile_button", class_id="@select_profile_button"))
        return button

    def prepare_delete_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.banner_rect.right - 150, self.banner_rect.bottom - 50, 40, 40),
            text="X", manager=self.manager, object_id=pygame_gui.core.ObjectID(object_id="@delete_profile_button", class_id="@delete_profile_button")
        )
        return button

    def prepare_edit_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.banner_rect.left + 220, self.banner_rect.top + 10, 60, 40),
            text="edit", manager=self.manager, object_id=pygame_gui.core.ObjectID(object_id="@edit_profile_button", class_id="@edit_profile_button")
        )
        if self.profile.empty_profile:
            button.visible = 0
        return button

    def draw(self, screen):
        screen.blit(self.banner, self.banner_rect)
        if not self.profile.empty_profile:
            screen.blit(self.time_in_text, self.time_in_text_rect)
            screen.blit(self.coins_icon, self.coins_icon_rect)
            screen.blit(self.coins_text, self.coins_text_rect)

    def set_profile_name(self):
        entered_name = self.name_entry.get_text()
        if entered_name != "" and entered_name != "Enter name":
            self.profile.name = entered_name
            self.profile.empty_profile = False
            self.edit_button.visible = 1
            self.name_entry.disable()
        else:
            if self.profile.name == "":
                self.name_entry.set_text("Enter name")
            else:
                self.name_entry.set_text(self.profile.name)
        self.name_entry.unfocus()

    def profile_selected(self):
        self.set_profile_name()
        if self.profile.empty_profile:
            self.manager.set_focus_set(self.name_entry)
            self.name_entry.set_text("")
            self.name_entry.enable()
        else:
            self.app.profile_selected = True
            self.app.current_profile = self.profile
            save_profiles(self.app.profiles)

    def delete_profile(self):
        self.profile.reset_profile()
        self.reload()

    def edit_profile_name(self):
        self.manager.set_focus_set(self.name_entry)
        self.name_entry.set_text("")
        self.name_entry.enable()

    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == self.name_entry:
                    self.set_profile_name()

            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.select_button:
                    self.profile_selected()

                if event.ui_element == self.delete_button:
                    self.delete_profile()

                if event.ui_element == self.edit_button:
                    self.edit_profile_name()
