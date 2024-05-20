import pygame
import math
class Projectile(pygame.sprite.Sprite):
    
    def __init__(self,player):
        super().__init__()
        self.velocity = 100
        self.image = pygame.image.load('assets/M107_M795_M483A1.png')
        self.rect = self.image.get_rect()
        self.image =pygame.transform.scale(self.image,(40,20))
        self.rect.x = player.rect.x+100
        self.rect.y = player.rect.y+50
        self.temps=0
        self.Y0=player.rect.y +50
        self.y_x=player.rect.y
        self.x_t=player.rect.x+100
        self.X0=player.rect.x+100
        self.player=player
        self.aplha_0=player.alpha
    def remove_s(self):
        self.player.all_projectiles.remove(self)
    def move(self,player):
        self.x_t=self.velocity*math.cos(self.aplha_0)*self.temps
        self.y_x =(-1/2)*9.8*(self.temps**2)+(self.velocity*math.sin(self.aplha_0)*self.temps)+0
        self.rect.x= self.x_t+self.X0
        self.rect.y= -self.y_x+self.Y0
        self.temps+= 0.1

        if self.rect.x>1000:
            self.remove_s()
        elif self.rect.x<0:
            self.remove_s()
        elif self.rect.y>600:
            self.remove_s()
        for monster in self.player.game.check_collision(self,self.player.game.all_monster):
            self.remove_s()
            monster.damage(self.player.attack)
