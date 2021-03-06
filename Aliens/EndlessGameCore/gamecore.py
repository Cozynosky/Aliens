import pygame

from datetime import datetime
from Aliens.EndlessGameCore.wave import Wave
from Aliens.EndlessGameCore.coin import Coin
from Aliens.Ship.ship import ShipState
from Aliens.Ship.player_ship import PlayerShip
from Aliens.EndlessGameCore.game_ui import GameUI
from Aliens.EndlessGameCore.enums import GameState, UIState
from Aliens.EndlessGameCore.nextwave_scene import NextWaveScene
from Aliens.OnlineScores.onlinescores import update_highscores, get_smallest_value
from Aliens import SOUNDS


class Game:
    def __init__(self, scene):
        self.state = GameState.STARTING
        self.start_time = datetime.now()
        self.end_time = self.start_time
        self.scene = scene
        self.ship = PlayerShip(scene.app)
        self.score = 0
        self.total_killed = 0
        self.coins_earned = 0
        self.wave = Wave(self)
        self.player_shots = pygame.sprite.Group()
        self.enemies_shots = pygame.sprite.Group()
        self.hit_shots = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.game_ui = GameUI(self)
        self.paused = False
        self.nextwave_scene = NextWaveScene()
        self.smallest_online_highscore = get_smallest_value()

    def refactor(self):
        self.game_ui.refactor()
        self.ship.refactor()
        self.wave.refactor()
        self.nextwave_scene.refactor()
        for coin in self.coins:
            coin.refactor()
        for shot in self.player_shots:
            shot.refactor()
        for shot in self.enemies_shots:
            shot.refactor()
        for shot in self.hit_shots:
            shot.refactor()

    def new_game(self):
        pygame.mouse.set_visible(False)
        self.game_ui.reset()
        self.scene.app.background.animate_background = True
        self.start_time = datetime.now()
        self.end_time = self.start_time
        self.state = GameState.STARTING
        self.score = 0
        self.coins_earned = 0
        self.total_killed = 0
        self.ship.new_game()
        self.wave.new_game(self.scene.app.current_profile.starting_wave.get_value())
        self.player_shots.empty()
        self.enemies_shots.empty()
        self.hit_shots.empty()
        self.coins.empty()
        self.paused = False

    def update(self):
        if not self.paused:
            if self.state == GameState.STARTING:
                self.ship.update()
                self.game_ui.update()
                if self.ship.state == ShipState.ALIVE and self.game_ui.state == UIState.SHOWED:
                    self.state = GameState.GAME_ON
            elif self.state == GameState.GAME_ON:
                if self.ship.state == ShipState.ALIVE or self.ship.state == ShipState.RESPAWNING:
                    self.coins.update()
                    self.wave.update()
                    self.wave.get_shots(self.enemies_shots)
                    self.ship.update()
                    self.hit_shots.update()
                    self.player_shots.update()
                    self.enemies_shots.update()
                    # game ui update
                    self.game_ui.update()
                    # collisions
                    self.bullets_with_enemies_collisions()
                    self.bullets_with_player_collisions()
                    self.player_with_enemy_collisions()
                    self.player_with_coin_collision()
                    if self.bottom_hud_collision():
                        self.game_ui.hide_bottom_hud()
                    if self.top_hud_collision():
                        self.game_ui.hide_top_hud()

                elif self.ship.state == ShipState.DEAD:
                    self.ship.update()
                    self.wave.dead_enemies.update()
                    self.game_ui.update()

                if self.ship.state == ShipState.OUTOFLIVES:
                    pygame.mouse.set_visible(True)
                    self.state = GameState.GAME_OVER
                    self.scene.game_over_scene.update()
                    SOUNDS.game_over.play()

            elif self.state == GameState.NEXT_WAVE:
                self.nextwave_scene.update()
                if self.nextwave_scene.is_ready:
                    self.scene.app.background.animate_background = True
                    self.nextwave_scene.reset()
                    self.wave.next_wave()
                    self.state = GameState.GAME_ON

            elif self.state == GameState.GAME_OFF:
                if self.score > self.smallest_online_highscore:
                    update_highscores(self.score, self.scene.app.current_profile.name)
                    self.smallest_online_highscore = get_smallest_value()
                self.end_time = datetime.now()
                self.save_progress()
                self.scene.app.current_scene = self.scene.app.game_scenes["GameMenuScene"]
                pygame.mouse.set_visible(True)
                self.scene.app.background.animate_background = True

    def draw(self, screen):
        self.coins.draw(screen)
        self.wave.draw(screen)
        self.ship.draw(screen)
        self.player_shots.draw(screen)
        self.enemies_shots.draw(screen)
        self.hit_shots.draw(screen)

        if self.state != GameState.GAME_OVER:
            self.game_ui.draw(screen)

        if self.state == GameState.NEXT_WAVE:
            self.nextwave_scene.render(screen)

    def save_progress(self):
        self.scene.app.current_profile.coins += self.coins_earned
        self.scene.app.current_profile.total_enemies_killed += self.total_killed
        self.scene.app.current_profile.total_coins_earned += self.coins_earned
        self.scene.app.current_profile.total_time += self.end_time - self.start_time

        if self.score > self.scene.app.current_profile.highest_score:
            self.scene.app.current_profile.highest_score = self.score

        if self.wave.wave_number > self.scene.app.current_profile.highest_wave:
            self.scene.app.current_profile.highest_wave = self.wave.wave_number

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and self.state != GameState.GAME_OVER:
                pygame.mouse.set_visible(not pygame.mouse.get_visible())
                self.paused = not self.paused
                if self.state != GameState.NEXT_WAVE:
                    self.scene.app.background.animate_background = not self.scene.app.background.animate_background
                
        if self.state == GameState.GAME_ON:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shots = self.ship.shot()
                    if shots:
                        for shot in shots:
                            self.player_shots.add(shot)
            self.ship.handle_event(event)

    def bullets_with_enemies_collisions(self):
        collisions = pygame.sprite.groupcollide(self.player_shots, self.wave.alive_enemies, False, False)
        for shot, enemies in collisions.items():
            enemy = pygame.sprite.spritecollideany(shot, pygame.sprite.Group(enemies), collided=pygame.sprite.collide_mask)
            if enemy and enemy.state == ShipState.ALIVE:
                if enemy.take_damage(shot.hit_damage):
                    self.wave.enemy_killed(enemy)
                    self.score += int(enemy.health_capacity)
                    Coin.drop_coin(self.scene.app.current_profile.drop_rate.get_value(), self.coins, enemy.rect.x, enemy.rect.y)
                    self.total_killed += 1
                shot.ship_hit()
                self.hit_shots.add(shot)
                self.player_shots.remove(shot)

    def bullets_with_player_collisions(self):
        if self.ship.state == ShipState.ALIVE:
            collisions = pygame.sprite.spritecollide(self.ship, self.enemies_shots, False)
            for shot in collisions:
                if self.ship.state == ShipState.ALIVE:
                    mask_collision = pygame.sprite.collide_mask(self.ship, shot)
                    if mask_collision:
                        if self.ship.take_damage(shot.hit_damage):
                            self.scene.app.background.animate_background = False
                        shot.ship_hit()
                        self.hit_shots.add(shot)
                        self.enemies_shots.remove(shot)

    def player_with_enemy_collisions(self):
        if self.ship.state == ShipState.ALIVE:
            collisions = pygame.sprite.spritecollide(self.ship, self.wave.alive_enemies, False)
            for enemy in collisions:
                mask_collision = pygame.sprite.collide_mask(self.ship, enemy)
                if mask_collision:
                    if self.ship.take_damage(self.ship.health_capacity):
                        self.scene.app.background.animate_background = False
                    if enemy.take_damage(self.ship.health_capacity):
                        self.wave.enemy_killed(enemy)
                        self.score += int(enemy.health_capacity)
                        Coin.drop_coin(self.scene.app.current_profile.drop_rate.get_value(), self.coins, enemy.rect.x, enemy.rect.y)
                        self.total_killed += 1

    def player_with_coin_collision(self):
        if self.ship.state == ShipState.ALIVE:
            collisions = pygame.sprite.spritecollide(self.ship, self.coins, False)
            for coin in collisions:
                mask_collision = pygame.sprite.collide_mask(self.ship, coin)
                if mask_collision:
                    SOUNDS.collect_coin.play()
                    self.coins_earned += self.scene.app.current_profile.coin_value.get_value()
                    coin.kill()

    def bottom_hud_collision(self):
        if self.game_ui.bottom_hud_bg_rect.colliderect(self.ship.rect):
            offset = (self.ship.rect.x - self.game_ui.bottom_hud_bg_rect.x, self.ship.rect.y - self.game_ui.bottom_hud_bg_rect.y)
            if self.game_ui.bottom_hud_bg_mask.overlap(self.ship.mask, offset):
                return True

        for shot in self.player_shots:
            if self.game_ui.bottom_hud_bg_rect.colliderect(shot.rect):
                offset = (shot.rect.x - self.game_ui.bottom_hud_bg_rect.x, shot.rect.y - self.game_ui.bottom_hud_bg_rect.y)
                if self.game_ui.bottom_hud_bg_mask.overlap(shot.mask, offset):
                    return True

        for shot in self.enemies_shots:
            if self.game_ui.bottom_hud_bg_rect.colliderect(shot.rect):
                offset = (shot.rect.x - self.game_ui.bottom_hud_bg_rect.x, shot.rect.y - self.game_ui.bottom_hud_bg_rect.y)
                if self.game_ui.bottom_hud_bg_mask.overlap(shot.mask, offset):
                    return True

        for coin in self.coins:
            if self.game_ui.bottom_hud_bg_rect.colliderect(coin.rect):
                offset = (coin.rect.x - self.game_ui.bottom_hud_bg_rect.x, coin.rect.y - self.game_ui.bottom_hud_bg_rect.y)
                if self.game_ui.bottom_hud_bg_mask.overlap(coin.mask, offset):
                    return True

        for enemy in self.wave.alive_enemies:
            if self.game_ui.bottom_hud_bg_rect.colliderect(enemy.rect):
                offset = (enemy.rect.x - self.game_ui.bottom_hud_bg_rect.x, enemy.rect.y - self.game_ui.bottom_hud_bg_rect.y)
                if self.game_ui.bottom_hud_bg_mask.overlap(enemy.mask, offset):
                    return True

        for enemy in self.wave.dead_enemies:
            if self.game_ui.bottom_hud_bg_rect.colliderect(enemy.rect):
                offset = (enemy.rect.x - self.game_ui.bottom_hud_bg_rect.x, enemy.rect.y - self.game_ui.bottom_hud_bg_rect.y)
                if self.game_ui.bottom_hud_bg_mask.overlap(enemy.mask, offset):
                    return True

        return False

    def top_hud_collision(self):
        if self.game_ui.top_hud_bg_rect.colliderect(self.ship.rect):
            offset = (self.ship.rect.x - self.game_ui.top_hud_bg_rect.x, self.ship.rect.y - self.game_ui.top_hud_bg_rect.y)
            if self.game_ui.top_hud_bg_mask.overlap(self.ship.mask, offset):
                return True

        for shot in self.player_shots:
            if self.game_ui.top_hud_bg_rect.colliderect(shot.rect):
                offset = (shot.rect.x - self.game_ui.top_hud_bg_rect.x, shot.rect.y - self.game_ui.top_hud_bg_rect.y)
                if self.game_ui.top_hud_bg_mask.overlap(shot.mask, offset):
                    return True

        for shot in self.enemies_shots:
            if self.game_ui.top_hud_bg_rect.colliderect(shot.rect):
                offset = (shot.rect.x - self.game_ui.top_hud_bg_rect.x, shot.rect.y - self.game_ui.top_hud_bg_rect.y)
                if self.game_ui.top_hud_bg_mask.overlap(shot.mask, offset):
                    return True

        for coin in self.coins:
            if self.game_ui.top_hud_bg_rect.colliderect(coin.rect):
                offset = (coin.rect.x - self.game_ui.top_hud_bg_rect.x, coin.rect.y - self.game_ui.top_hud_bg_rect.y)
                if self.game_ui.top_hud_bg_mask.overlap(coin.mask, offset):
                    return True
        for enemy in self.wave.alive_enemies:
            if self.game_ui.top_hud_bg_rect.colliderect(enemy.rect):
                offset = (enemy.rect.x - self.game_ui.top_hud_bg_rect.x, enemy.rect.y - self.game_ui.top_hud_bg_rect.y)
                if self.game_ui.top_hud_bg_mask.overlap(enemy.mask, offset):
                    return True

        for enemy in self.wave.dead_enemies:
            if self.game_ui.top_hud_bg_rect.colliderect(enemy.rect):
                offset = (enemy.rect.x - self.game_ui.top_hud_bg_rect.x, enemy.rect.y - self.game_ui.top_hud_bg_rect.y)
                if self.game_ui.top_hud_bg_mask.overlap(enemy.mask, offset):
                    return True

        return False

