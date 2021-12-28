from Aliens.Ship.player_ship import PlayerShip


class Profile:
    def __init__(self, name="Empty"):
        self.name = name
        self.currency = 0
        self.ship = PlayerShip()
        self.drop_rate = 1.0
        self.coin_value = 1
