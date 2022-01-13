import pygame
import pygame_gui
import os.path

from Aliens import SETTINGS, SOUNDS

from Aliens.scene import Scene


class SettingsScene(Scene):
    def __init__(self, parent):
        super(SettingsScene, self).__init__(parent)
        pygame.font.init()
        # game logo
        self.settings_text, self.settings_text_rect = self.prepare_settings_text()
        # settings bg
        self.settings_background, self.settings_background_rect = self.prepare_settings_background()
        # labels
        self.resolution_label = self.prepare_resolution_label()
        self.fullscreen_label = self.prepare_fullscreen_label()
        self.auto_save_label = self.prepare_auto_save_label()
        self.music_volume_label = self.prepare_music_volume_label()
        self.sounds_volume_label = self.prepare_sounds_volume_label()
        # dropdown
        self.resolution_dropdown = self.prepare_resolution_dropdown()
        # button
        self.fullscreen_button = self.prepare_fullscreen_button()
        self.auto_save_button = self.prepare_auto_save_button()
        self.back_button = self.prepare_back_button()
        #sliders
        self.music_volume_slider = self.prepare_music_volume_slider()
        self.sounds_volume_slider = self.prepare_sounds_volume_slider()

    def refactor_ui(self):
        self.manager = self.prepare_manager()
        # game logo
        self.settings_text, self.settings_text_rect = self.prepare_settings_text()
        # settings bg
        self.settings_background, self.settings_background_rect = self.prepare_settings_background()
        # labels
        self.resolution_label = self.prepare_resolution_label()
        self.fullscreen_label = self.prepare_fullscreen_label()
        self.auto_save_label = self.prepare_auto_save_label()
        self.music_volume_label = self.prepare_music_volume_label()
        self.sounds_volume_label = self.prepare_sounds_volume_label()
        # dropdown
        self.resolution_dropdown = self.prepare_resolution_dropdown()
        # button
        self.fullscreen_button = self.prepare_fullscreen_button()
        self.auto_save_button = self.prepare_auto_save_button()
        self.back_button = self.prepare_back_button()
        #sliders
        self.music_volume_slider = self.prepare_music_volume_slider()
        self.sounds_volume_slider = self.prepare_sounds_volume_slider()

    def update(self):
        super(SettingsScene, self).update()
        value = round(self.music_volume_slider.get_current_value(), 2)
        SETTINGS.MUSIC_VOLUME = value
        SOUNDS.set_playback_volume(value)

        value = round(self.sounds_volume_slider.get_current_value(), 2)
        SETTINGS.SOUNDS_VOLUME = value
        SOUNDS.set_sounds_volume(value)

    def prepare_settings_background(self):
        images_folder = os.path.join("Data", "Sprites", "Background")
        filename = "small_bg.png"
        background = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        rect = background.get_rect()
        rect.centerx = SETTINGS.WINDOW_WIDTH // 2
        rect.top = self.settings_text_rect.bottom + 20

        return background, rect

    def prepare_settings_text(self):
        background = pygame.Surface((SETTINGS.WINDOW_WIDTH, 70))
        background.fill(pygame.Color('#808080'))
        background_rect = background.get_rect()
        background_rect.x = 0
        background_rect.y = 50

        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"
        myfont = pygame.font.Font(os.path.join(fonts_path, font_name), 60)
        text = myfont.render('Settings', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 300 * SETTINGS.SCALE
        text_rect.centery = 35
        background.blit(text, text_rect)
        return background, background_rect

    def prepare_resolution_label(self):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 200, self.settings_text_rect.bottom + 50, 130, 40),
                                                       text="Resolution", manager=self.manager)
        return label

    def prepare_fullscreen_label(self):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 200, self.settings_text_rect.bottom + 100, 130, 40),
                                                            text="Fullscreen", manager=self.manager)
        return label

    def prepare_auto_save_label(self):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 200, self.settings_text_rect.bottom + 150, 130, 40),
                                                            text="Auto save", manager=self.manager)
        return label

    def prepare_music_volume_label(self):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 200, self.settings_text_rect.bottom + 200, 130, 40),
                                                            text="Music volume", manager=self.manager)
        return label

    def prepare_sounds_volume_label(self):
        label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 200, self.settings_text_rect.bottom + 250, 130, 40),
                                                            text="Sounds volume", manager=self.manager)
        return label

    def prepare_resolution_dropdown(self):
        resolution_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 50, self.settings_text_rect.bottom + 50, 250, 40),
                                                                 manager=self.manager,
                                                                 options_list=SETTINGS.RESOLUTIONS.keys(),
                                                                 starting_option=f"{SETTINGS.WINDOW_WIDTH} x {SETTINGS.WINDOW_HEIGHT}")
        return resolution_dropdown

    def prepare_fullscreen_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 50, self.settings_text_rect.bottom + 100, 120, 40), text=f"{SETTINGS.FULLSCREEN}",
            manager=self.manager)
        return button

    def prepare_auto_save_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 50, self.settings_text_rect.bottom + 150, 120, 40), text=f"{SETTINGS.AUTO_SAVE}",
            manager=self.manager)
        return button

    def prepare_music_volume_slider(self):
        slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 50, self.settings_text_rect.bottom + 200, 250, 40),
            start_value=SETTINGS.MUSIC_VOLUME,
            value_range=(0.0, 0.5),
            manager=self.manager
        )
        return slider

    def prepare_sounds_volume_slider(self):
        slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(SETTINGS.WINDOW_WIDTH // 2 - 50, self.settings_text_rect.bottom + 250, 250, 40),
            start_value=SETTINGS.SOUNDS_VOLUME,
            value_range=(0.0, 0.5),
            manager=self.manager
        )
        return slider

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)
        return button

    def render(self, screen):
        self.app.background.draw(screen)
        screen.blit(self.settings_background, self.settings_background_rect)
        screen.blit(self.settings_text, self.settings_text_rect)
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
                        SOUNDS.button_click.play()
                        self.app.current_scene = self.app.game_scenes['MainMenuScene']
                    if event.ui_element == self.fullscreen_button:
                        SETTINGS.FULLSCREEN = not SETTINGS.FULLSCREEN
                        self.app.refactor_ui()
                    if event.ui_element == self.auto_save_button:
                        SETTINGS.AUTO_SAVE = not SETTINGS.AUTO_SAVE
                        self.auto_save_button.set_text(f"{SETTINGS.AUTO_SAVE}")
                        SETTINGS.save_settings()

                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    SETTINGS.WINDOW_SIZE = (SETTINGS.RESOLUTIONS[event.text]["width"], SETTINGS.RESOLUTIONS[event.text]["height"])
                    SETTINGS.WINDOW_WIDTH = int(event.text.split(" x ")[0])
                    SETTINGS.WINDOW_HEIGHT = int(event.text.split(" x ")[1])
                    SETTINGS.SCALE = SETTINGS.prepare_scale()
                    self.app.refactor_ui()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes['MainMenuScene']

            self.manager.process_events(event)
        self.manager.update(time_delta)
