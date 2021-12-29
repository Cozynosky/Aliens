from Aliens.Ship.player_ship import PlayerShip
from datetime import timedelta


class Profile:
    def __init__(self, name="Empty"):
        # profile name
        self.name = name
        # ship
        self.ship = PlayerShip()
        # earned coins
        self.coins = 0
        # upgradable values
        self.drop_rate = 1.0
        self.coin_value = 1
        # statistics
        self.highest_score = 0
        self.highest_wave = 0
        self.total_enemies_killed = 0
        self.total_time = timedelta(0, 0, 0, 0, 0, 0, 0)
        self.total_coins_earned = 0

