import pygame

from Aliens.EndlessGameCore.wave import Wave


class Game:
    def __init__(self, ship):
        # store current profile
        self.ship = ship
        # init wave system
        self.wave = Wave()
        # player shots
        self.player_shots = pygame.sprite.Group()
        # hit shots, kept only for animations
        self.hit_shots = pygame.sprite.Group()

    def refactor(self):
        self.ship.refactor()

    def reset(self):
        self.ship.reset()
        self.wave.reset()
        self.player_shots.empty()
        self.hit_shots.empty()

    def update(self):
        self.wave.update()
        self.ship.update()
        self.hit_shots.update()
        self.player_shots.update()
        self.manage_collisions()

    def draw(self, screen):
        self.wave.draw(screen)
        self.ship.draw(screen)
        self.player_shots.draw(screen)
        self.hit_shots.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.player_shots.add(self.ship.shot())
        self.ship.handle_event(event)

    def manage_collisions(self):
        collisions = pygame.sprite.groupcollide(self.player_shots, self.wave.alive_enemies, False, False)
        for shot, enemies in collisions.items():
            enemy = pygame.sprite.spritecollideany(shot, pygame.sprite.Group(enemies), collided=pygame.sprite.collide_mask)
            if enemy:
                if enemy.got_hit(shot.damage):
                    self.wave.enemy_killed(enemy)
                shot.enemy_hit()
                self.hit_shots.add(shot)
                self.player_shots.remove(shot)

