from datetime import timedelta
from Aliens.Upgrades.upgrades import *


class Profile:
    def __init__(self):
        # profile name
        self.name = ""
        self.empty_profile = True

        # ---------------- ship upgradables ----------------------
        self.ship_speed = ShipSpeed()
        # health
        self.health_capacity = HealthCapacity()
        self.lives = Lives()

        # weapon
        self.bullets_in_shot = BulletsInShot()
        self.bullet_speed = BulletSpeed()
        self.bullet_damage = BulletDamage()

        # magazine
        self.magazine_size = MagazineSize()
        self.reload_time = ReloadTime()                       # in seconds

        # coins
        self.drop_rate = DropRate()
        self.coin_value = CoinValue()
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
        self.ship_speed = ShipSpeed()
        # health
        self.health_capacity = HealthCapacity()
        self.lives = Lives()

        # weapon
        self.bullets_in_shot = BulletsInShot()
        self.bullet_speed = BulletSpeed()
        self.bullet_damage = BulletDamage()

        # magazine
        self.magazine_size = MagazineSize()
        self.reload_time = ReloadTime()                       # in seconds

        # coins
        self.drop_rate = DropRate()
        self.coin_value = CoinValue()
        # ---------------------------------------------------

        # earned coins
        self.coins = 0
        # statistics
        self.highest_score = 0
        self.highest_wave = 0
        self.total_enemies_killed = 0
        self.total_time = timedelta(0, 0, 0, 0, 0, 0, 0)
        self.total_coins_earned = 0
