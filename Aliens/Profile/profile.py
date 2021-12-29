from datetime import timedelta
from Aliens import SETTINGS


class Profile:
    def __init__(self, name="Empty"):
        # profile name
        self.name = name
        # ship
        self.base_speed = round(4 * SETTINGS.SCALE)
        self.base_bullet_speed = round(5 * SETTINGS.SCALE)
        self.base_hit_damage = 5
        self.base_health_capacity = 10
        self.base_lives = 1
        self.base_magazine_size = 3
        self.base_reload_time = 1                       # in seconds
        # upgradable values
        self.drop_rate = 1.0
        self.coin_value = 1
        # earned coins
        self.coins = 0
        # statistics
        self.highest_score = 0
        self.highest_wave = 0
        self.total_enemies_killed = 0
        self.total_time = timedelta(0, 0, 0, 0, 0, 0, 0)
        self.total_coins_earned = 0
