import pygame
from Aliens.Ship.easyenemy_ship import EasyEnemy


class Wave:
    def __init__(self):
        self.wave_number = 1
        self.enemies_to_spawn = self.get_enemies_to_spawn()
        self.enemies_left = self.enemies_to_spawn
        self.alive_enemies = pygame.sprite.Group()
        self.dead_enemies = pygame.sprite.Group()
        self.spawn_time = self.get_spawn_time()      # in seconds
        self.to_spawn_time = 0                       # in seconds

    def new_game(self):
        self.wave_number = 1
        self.enemies_to_spawn = self.get_enemies_to_spawn()
        self.enemies_left = self.enemies_to_spawn
        self.alive_enemies.empty()
        self.dead_enemies.empty()
        self.spawn_time = self.get_spawn_time()
        self.to_spawn_time = 0

    def next_wave(self):
        self.wave_number += 1
        self.enemies_to_spawn = self.get_enemies_to_spawn()
        self.enemies_left = self.enemies_to_spawn
        self.spawn_time = self.get_spawn_time()
        self.to_spawn_time = 0

    def get_enemies_to_spawn(self):
        # WAVE, VALUE: 1, 5 -> 5, 8 -> 10, 13 -> 20, 25 -> 50, 70
        enemies = 0.451636 * self.wave_number ** 1.27209 + 4.53281
        return round(enemies)

    def get_spawn_time(self):
        # WAVE, VALUE: 1, 3 -> 5, 2.8 -> 10, 2.6 -> 20, 2.3 -> 50, 1.6
        spawn_time = 3.28506 - 0.19515 * self.wave_number ** 0.541314
        # avoid values lower than 1.0
        spawn_time = max(1.0, spawn_time)
        return spawn_time

    def update(self):
        self.to_spawn_time -= 0.016
        self.alive_enemies.update()
        self.dead_enemies.update()

        if self.enemies_to_spawn > 0 > self.to_spawn_time:
            self.alive_enemies.add(EasyEnemy(self.wave_number))
            self.enemies_to_spawn -= 1
            self.to_spawn_time = self.spawn_time
        elif self.enemies_to_spawn == 0 and self.enemies_left == 0:
            self.next_wave()

    def get_shots(self, shots):
        for enemy in self.alive_enemies:
            enemy.try_shot(shots)

    def draw(self, screen):
        self.alive_enemies.draw(screen)
        self.dead_enemies.draw(screen)

    def enemy_killed(self, enemy):
        self.to_spawn_time -= self.spawn_time / 2
        self.dead_enemies.add(enemy)
        self.alive_enemies.remove(enemy)
        self.enemies_left -= 1
