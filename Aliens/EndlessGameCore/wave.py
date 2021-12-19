import pygame
from Aliens.Ship.easyenemy_ship import EasyEnemy


class Wave:
    def __init__(self):
        self.wave_number = 1
        self.enemies_to_spawn = 5
        self.alive_enemies = pygame.sprite.Group()
        self.dead_enemies = pygame.sprite.Group()
        self.spawn_time = 3                           # in seconds
        self.to_spawn_time = 1                       # in seconds

    def reset(self):
        self.wave_number = 1
        self.enemies_to_spawn = 5
        self.alive_enemies.empty()
        self.dead_enemies.empty()
        self.spawn_time = 3
        self.to_spawn_time = 1

    def update(self):
        self.to_spawn_time -= 0.016
        self.alive_enemies.update()
        self.dead_enemies.update()

        if self.enemies_to_spawn > 0 > self.to_spawn_time:
            self.alive_enemies.add(EasyEnemy(self.wave_number))
            self.enemies_to_spawn -= 1
            self.to_spawn_time = self.spawn_time
        else:
            pass

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
