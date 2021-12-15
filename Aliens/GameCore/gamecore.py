class Game:
    def __init__(self, game_mode, ship):
        self.game_mode = game_mode
        # store current profile
        self.ship = ship
        # setup background

    def refactor(self):
        self.ship.refactor()

    def reset(self):
        self.ship.reset_ship()

    def update(self):
        self.ship.update()

    def draw(self, screen):
        self.ship.draw(screen)

    def handle_event(self, event):
        self.ship.handle_event(event)
