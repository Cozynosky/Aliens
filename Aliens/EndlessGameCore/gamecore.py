import pygame

from Aliens.EndlessGameCore.wave import Wave
from Aliens.Ship.ship import ShipState
from Aliens.EndlessGameCore.game_ui import GameUI
from enum import Enum


class GameState(Enum):
    STARTING = 0

    NEXT_WAVE = 2
    GAMEOVER = 3


class Game:
    def __init__(self, ship):
        self.ship = ship
        self.score = 0

        self.wave = Wave()
        self.player_shots = pygame.sprite.Group()
        self.enemies_shots = pygame.sprite.Group()
        self.hit_shots = pygame.sprite.Group()
        self.game_ui = GameUI(self)

    def refactor(self):
        self.game_ui.refactor()
        self.ship.refactor()

    def reset(self):
        self.score = 0
        self.ship.reset()
        self.wave.reset()
        self.player_shots.empty()
        self.enemies_shots.empty()
        self.hit_shots.empty()

    def update(self):
        self.wave.update()
        self.wave.get_shots(self.enemies_shots)
        self.ship.update()
        self.hit_shots.update()
        self.player_shots.update()
        self.enemies_shots.update()
        # collisions
        self.bullets_with_enemies_collisions()
        self.bullets_with_player_collisions()
        self.player_with_enemy_collisions()
        # game ui update
        self.game_ui.update()

    def draw(self, screen):
        self.wave.draw(screen)
        self.ship.draw(screen)
        self.player_shots.draw(screen)
        self.enemies_shots.draw(screen)
        self.hit_shots.draw(screen)
        self.game_ui.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot = self.ship.shot()
                if shot:
                    self.player_shots.add(shot)
        self.ship.handle_event(event)

    def bullets_with_enemies_collisions(self):
        collisions = pygame.sprite.groupcollide(self.player_shots, self.wave.alive_enemies, False, False)
        for shot, enemies in collisions.items():
            enemy = pygame.sprite.spritecollideany(shot, pygame.sprite.Group(enemies), collided=pygame.sprite.collide_mask)
            if enemy:
                if enemy.take_damage(shot.hit_damage):
                    self.wave.enemy_killed(enemy)
                    self.score += int(enemy.health_capacity)
                shot.ship_hit()
                self.hit_shots.add(shot)
                self.player_shots.remove(shot)

    def bullets_with_player_collisions(self):
        collisions = pygame.sprite.spritecollide(self.ship, self.enemies_shots, False)
        for shot in collisions:
            mask_collision = pygame.sprite.collide_mask(self.ship, shot)
            if mask_collision:
                if self.ship.take_damage(shot.hit_damage):
                    # player is dead
                    pass
                shot.ship_hit()
                self.hit_shots.add(shot)
                self.enemies_shots.remove(shot)

    def player_with_enemy_collisions(self):
        if self.ship.state == ShipState.ALIVE:
            collisions = pygame.sprite.spritecollide(self.ship, self.wave.alive_enemies, False)
            for enemy in collisions:
                mask_collision = pygame.sprite.collide_mask(self.ship, enemy)
                if mask_collision:
                    self.ship.take_damage(self.ship.health_capacity)
                    enemy.take_damage(enemy.health_capacity)
                    self.wave.enemy_killed(enemy)