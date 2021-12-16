import pygame
from Aliens.Enemies.easyenemy import EasyEnemy


class Wave:
    def __init__(self):
        self.wave_number = 1
        self.number_to_kill = 5
        self.number_of_spawned = 0
        self.alive_enemies = pygame.sprite.Group()
        self.dead_enemies = pygame.sprite.Group()
        self.spawn_time = 3                           # in seconds
        self.to_spawn_time = 3                        # in seconds

    def reset(self):
        self.wave_number = 1
        self.number_to_kill = 5
        self.number_of_spawned = 0
        self.alive_enemies.empty()
        self.dead_enemies.empty()
        self.spawn_time = 3
        self.to_spawn_time = 3

    def update(self):
        if self.number_of_spawned < self.number_to_kill and self.spawn_time <= self.to_spawn_time:
            self.alive_enemies.add(EasyEnemy(self.wave_number))
            self.to_spawn_time = 0
            self.number_of_spawned += 1

        self.to_spawn_time += 0.016
        self.alive_enemies.update()
        self.dead_enemies.update()

    def draw(self, screen):
        self.alive_enemies.draw(screen)
        self.dead_enemies.draw(screen)

    def enemy_killed(self, enemy):
        self.to_spawn_time += self.spawn_time / 2
        self.dead_enemies.add(enemy)
        self.alive_enemies.remove(enemy)
