import pygame

from Aliens.EndlessGameCore.wave import Wave


class Game:
    def __init__(self, ship):
        # store current profile
        self.ship = ship
        # init wave system
        self.wave = Wave()

    def refactor(self):
        self.ship.refactor()

    def reset(self):
        self.ship.reset()
        self.wave.reset()

    def update(self):
        self.wave.update()
        self.ship.update()
        self.manage_collisions()

    def draw(self, screen):
        self.wave.draw(screen)
        self.ship.draw(screen)

    def handle_event(self, event):
        self.ship.handle_event(event)

    def manage_collisions(self):
        collisions = pygame.sprite.groupcollide(self.ship.shots, self.wave.enemies_in_wave, False, False)
        for shot, enemies in collisions.items():
            enemy = pygame.sprite.spritecollideany(shot, pygame.sprite.Group(enemies), collided=pygame.sprite.collide_mask)
            if enemy:
                # enemy.kill()
                shot.enemy_hit()

