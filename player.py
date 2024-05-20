import pygame
from projectile import Projectile
class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health=100
        self.max_health=100
        self.attack=10
        self.velocity=3
        self.image=pygame.image.load('assets/tank.png')
        self.image = pygame.transform.scale(self.image, (200, 100))
        self.rect = self.image.get_rect()
        self.rect.x=100
        self.rect.y=400
        self.all_projectiles = pygame.sprite.Group()
        self.alpha=45
    def damage(self,amount):
        if self.health-amount>amount:
            self.health -=amount
        else:
            self.game.game_over()
    def up(self):
        self.alpha+=0.01
        if self.alpha>90:
            self.alpha=90
    def down(self):
        self.alpha-=0.01
        if self.alpha<0:
            self.alpha=0


    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
