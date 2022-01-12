import pygame
import pygame_gui
import os.path

from Aliens import SETTINGS, SOUNDS
from Aliens.scene import Scene


class InstructionsScene(Scene):
    def __init__(self, parent):
        super(InstructionsScene, self).__init__(parent)
        self.parent = parent
        pygame.font.init()
        # prepare font
        self.big_font, self.small_font = self.load_fonts()
        # banner at the top
        self.instruction_text, self.instruction_text_rect = self.prepare_instruction_text()
        self.image, self.image_rect = self.prepare_image()
        #buttons
        self.back_button = self.prepare_back_button()

    def refactor_ui(self):
        # ui manager
        self.manager = self.prepare_manager()
        # prepare font
        self.big_font, self.small_font = self.load_fonts()
        # banner at the top
        self.instruction_text, self.instruction_text_rect = self.prepare_instruction_text()
        self.image, self.image_rect = self.prepare_image()
        #buttons
        self.back_button = self.prepare_back_button()

    def load_fonts(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), 60)
        small_font = pygame.font.Font(os.path.join(fonts_path, font_name), 30)

        return big_font, small_font

    def prepare_instruction_text(self):
        background = pygame.Surface((SETTINGS.WINDOW_WIDTH, 70))
        background.fill(pygame.Color('#808080'))
        background_rect = background.get_rect()
        background_rect.x = 0
        background_rect.y = 50

        text = self.big_font.render('Instruction', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 300 * SETTINGS.SCALE
        text_rect.centery = 35
        background.blit(text, text_rect)
        return background, background_rect

    def prepare_image(self):
        images_folder = os.path.join("Data", "Sprites", "Background")
        filename = "instructions.png"
        background = pygame.image.load(os.path.join(images_folder, filename)).convert_alpha()
        rect = background.get_rect()
        rect.centerx = SETTINGS.WINDOW_WIDTH // 2
        rect.top = self.instruction_text_rect.bottom + 20

        return background, rect

    def prepare_back_button(self):
        button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(25, SETTINGS.WINDOW_HEIGHT - 75, 100, 50), text="BACK",
            manager=self.manager)
        return button

    def render(self, screen):
        self.app.background.draw(screen)
        screen.blit(self.instruction_text, self.instruction_text_rect)
        screen.blit(self.image, self.image_rect)
        self.manager.draw_ui(screen)
        pygame.display.update()

    def handle_events(self, events):
        time_delta = self.clock.tick(60) / 1000.0
        for event in events:
            if event.type == pygame.QUIT:
                self.app.close_app()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    SOUNDS.button_click.play()
                    if event.ui_element == self.back_button:
                        self.app.current_scene = self.app.game_scenes['MainMenuScene']

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes['MainMenuScene']

            self.manager.process_events(event)
        self.manager.update(time_delta)
