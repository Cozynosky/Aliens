import pygame
from Aliens.Enemies.easyenemy import EasyEnemy


class Wave:
    def __init__(self):
        self.wave_number = 1
        self.number_to_kill = 8
        self.number_of_spawned = 0
        self.enemies_in_wave = pygame.sprite.Group()
        self.spawn_time = 5                           # in seconds
        self.to_spawn_time = 5                        # in seconds

    def reset(self):
        self.wave_number = 1
        self.number_to_kill = 20
        self.number_of_spawned = 0
        self.enemies_in_wave.empty()
        self.spawn_time = 5
        self.to_spawn_time = 5

    def update(self):
        if self.number_of_spawned < self.number_to_kill and self.spawn_time <= self.to_spawn_time:
            self.enemies_in_wave.add(EasyEnemy(self.wave_number))
            self.to_spawn_time = 0
            self.number_of_spawned += 1
        self.to_spawn_time += 0.016
        self.enemies_in_wave.update()

    def draw(self, screen):
        self.enemies_in_wave.draw(screen)
