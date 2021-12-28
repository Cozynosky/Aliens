import pygame

from Aliens.EndlessGameCore.wave import Wave
from Aliens.EndlessGameCore.coin import Coin
from Aliens.Ship.ship import ShipState
from Aliens.EndlessGameCore.game_ui import GameUI
from enum import Enum


class GameState(Enum):
    STARTING = 0
    GAME_ON = 1
    NEXT_WAVE = 2
    GAMEOVER = 3


class Game:
    def __init__(self, profile, scene):
        self.state = GameState.GAME_ON
        self.profile = profile
        self.scene = scene
        self.ship = profile.ship
        self.score = 0
        self.coins_earned = 0
        self.wave = Wave()
        self.player_shots = pygame.sprite.Group()
        self.enemies_shots = pygame.sprite.Group()
        self.hit_shots = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.game_ui = GameUI(self)
        self.paused = False

    def refactor(self):
        self.game_ui.refactor()
        self.ship.refactor()

    def new_game(self):
        self.state = GameState.GAME_ON
        self.score = 0
        self.coins_earned = 0
        self.ship.new_game()
        self.wave.new_game()
        self.player_shots.empty()
        self.enemies_shots.empty()
        self.hit_shots.empty()
        self.coins.empty()
        self.paused = False

    def update(self):
        if self.state == GameState.GAME_ON:
            if self.ship.state == ShipState.ALIVE:
                self.scene.app.background.update()
                self.coins.update()
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
                self.player_with_coin_collision()
                # game ui update
                self.game_ui.update()
            elif self.ship.state == ShipState.DEAD:
                self.ship.update()
                self.wave.dead_enemies.update()
                self.game_ui.update()
            elif self.ship.state == ShipState.OUTOFLIVES:
                self.state = GameState.GAMEOVER

    def draw(self, screen):
        self.coins.draw(screen)
        self.wave.draw(screen)
        self.ship.draw(screen)
        self.player_shots.draw(screen)
        self.enemies_shots.draw(screen)
        self.hit_shots.draw(screen)
        self.game_ui.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.paused = not self.paused
        if self.state == GameState.GAME_ON:
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
                    Coin.drop_coin(self.profile.drop_rate, self.coins, enemy.rect.x, enemy.rect.y)
                shot.ship_hit()
                self.hit_shots.add(shot)
                self.player_shots.remove(shot)

    def bullets_with_player_collisions(self):
        if self.ship.state == ShipState.ALIVE:
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
                    if enemy.take_damage(self.ship.health_capacity):
                        self.wave.enemy_killed(enemy)
                        self.score += int(enemy.health_capacity)
                        Coin.drop_coin(self.profile.drop_rate, self.coins, enemy.rect.x, enemy.rect.y)

    def player_with_coin_collision(self):
        if self.ship.state == ShipState.ALIVE:
            collisions = pygame.sprite.spritecollide(self.ship, self.coins, False)
            for coin in collisions:
                mask_collision = pygame.sprite.collide_mask(self.ship, coin)
                if mask_collision:
                    self.coins_earned += self.profile.coin_value
                    coin.kill()
