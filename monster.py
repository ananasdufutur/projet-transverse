import pygame
import random
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game=game
        self.health=50
        self.max_health=50
        self.attack=5
        self.image=pygame.image.load('assets/sans_v2.jpg')
        self.rect=self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect.x=900
        self.rect.y=300+ random.randint(0,200)
        self.velocity=random.randint(1,5)

    def update_health_bar(self,surface):
        bar_color=(11,210,46)
        back_bar_color=(255,0,0)
        bar_position=[self.rect.x,self.rect.y+50,self.health,4]
        back_bar_position = [self.rect.x, self.rect.y + 50, self.max_health, 4]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface,bar_color,bar_position)


    def move_line(self):

        if self.rect.y<0 :
            self.rect.y=500

        else:
            self.rect.y-=self.velocity

    def damage(self,amount):
        self.health-=amount
        if self.health<=0:
            self.rect.y=900
            self.health=self.max_health
