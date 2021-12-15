from Aliens.GameCore.background import EndlessBackground


class Game:
    def __init__(self, game_mode, ship):
        self.game_mode = game_mode
        # store current profile
        self.ship = ship
        # setup background
        self.background = EndlessBackground()

    def refactor(self):
        self.background.refactor()
        self.ship.refactor()

    def reset(self):
        self.background.reset()
        self.ship.reset_ship()

    def update(self):
        self.background.update()
        self.ship.update()

    def draw(self, screen):
        self.background.draw(screen)
        self.ship.draw(screen)

    def handle_event(self, event):
        self.ship.handle_event(event)
