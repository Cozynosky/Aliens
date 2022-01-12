import pygame
import pygame_gui
import os.path

from Aliens.OnlineScores.onlinescores import get_highscores
from Aliens import SETTINGS, SOUNDS
from Aliens.scene import Scene


class OnlineHighScoresScene(Scene):
    def __init__(self, parent):
        super(OnlineHighScoresScene, self).__init__(parent)
        self.parent = parent
        pygame.font.init()
        self.high_scores = []
        # prepare font
        self.big_font, self.small_font = self.load_fonts()
        # banner at the top
        self.scores_text, self.scores_text_rect = self.prepare_scores_text()
        #buttons
        self.back_button = self.prepare_back_button()

    def refactor_ui(self):
        # ui manager
        self.manager = self.prepare_manager()
        # banner at the top
        self.scores_text, self.scores_text_rect = self.prepare_scores_text()
        #buttons
        self.back_button = self.prepare_back_button()

    def prepare_highscores(self):
        online_high_scores = get_highscores()
        prepared_highscores = []
        for i in range(len(online_high_scores)):
            single = HighScoreSingle(i+1, online_high_scores[i]['Name'], online_high_scores[i]['Score'], self.scores_text_rect.bottom + 20 + (50 * i))
            prepared_highscores.append(single)
        self.high_scores = prepared_highscores

    def update(self):
        super(OnlineHighScoresScene, self).update()

    def load_fonts(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        big_font = pygame.font.Font(os.path.join(fonts_path, font_name), 60)
        small_font = pygame.font.Font(os.path.join(fonts_path, font_name), 30)

        return big_font, small_font

    def prepare_scores_text(self):
        background = pygame.Surface((SETTINGS.WINDOW_WIDTH, 70))
        background.fill(pygame.Color('#dab600'))
        background_rect = background.get_rect()
        background_rect.x = 0
        background_rect.y = 50

        text = self.big_font.render('Online High Scores', True, (255, 255, 255))
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
        screen.blit(self.scores_text, self.scores_text_rect)
        for highscore in self.high_scores:
            highscore.render(screen)
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
                        self.app.current_scene = self.app.game_scenes['GameMenuScene']

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.current_scene = self.app.game_scenes['GameMenuScene']

            self.manager.process_events(event)
        self.manager.update(time_delta)


class HighScoreSingle:
    def __init__(self, place, name, score,  y):
        self.place = place
        self.name = name
        self.score = score
        self.y = y
        self.x = SETTINGS.WINDOW_WIDTH // 2
        self.font = self.prepare_font()
        self.text = self.prepare_text()
        self.text_rect = self.prepare_text_rect()

    def prepare_font(self):
        fonts_path = os.path.join("Data", "Fonts", "alien_eclipse")
        font_name = "Alien Eclipse.otf"

        font = pygame.font.Font(os.path.join(fonts_path, font_name), 50)

        return font

    def prepare_text(self):
        if self.name == "":
            text = f"{self.place}."
        else:
            text = f"{self.place}. {self.name} - Score: {self.score}"
        rendered_text = self.font.render(text, True, (255, 255, 255))
        return rendered_text

    def prepare_text_rect(self):
        rect = self.text.get_rect()
        rect.centerx = self.x
        rect.y = self.y
        return rect

    def render(self, screen):
        screen.blit(self.text, self.text_rect)