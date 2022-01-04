from datetime import timedelta


class Profile:
    def __init__(self):
        # profile name
        self.name = ""
        self.empty_profile = True

        # ---------------- ship upgradables ----------------------
        self.ship_speed_level = 1
        # weapon
        self.shots_in_shot_level = 1
        self.bullet_speed_level = 1
        self.bullet_damage_level = 1
        # health
        self.health_capacity_level = 1
        self.lives_level = 1
        # magazine
        self.magazine_size_level = 1
        self.reload_time_level = 1                       # in seconds
        # coins
        self.drop_rate_level = 0.3
        self.coin_value_level = 1
        # ---------------------------------------------------

        # earned coins
        self.coins = 0
        # statistics
        self.highest_score = 0
        self.highest_wave = 0
        self.total_enemies_killed = 0
        self.total_time = timedelta(0, 0, 0, 0, 0, 0, 0)
        self.total_coins_earned = 0

    def reset_profile(self):
        # profile name
        self.name = ""
        self.empty_profile = True

        # ---------------- ship upgradables ----------------------
        self.ship_speed_level = 1
        # weapon
        self.shots_in_shot_level = 1
        self.bullet_speed_level = 1
        self.bullet_damage_level = 1
        # health
        self.health_capacity_level = 1
        self.lives_level = 1
        # magazine
        self.magazine_size_level = 1
        self.reload_time_level = 1                       # in seconds
        # coins
        self.drop_rate_level = 0.3
        self.coin_value_level = 1
        # ---------------------------------------------------

        # earned coins
        self.coins = 0
        # statistics
        self.highest_score = 0
        self.highest_wave = 0
        self.total_enemies_killed = 0
        self.total_time = timedelta(0, 0, 0, 0, 0, 0, 0)
        self.total_coins_earned = 0
