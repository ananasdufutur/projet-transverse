import pygame.sprite
import pygame
from player import Player
from monster import  Monster
from pygame.locals import K_RETURN, K_SPACE, KEYDOWN, KEYUP, QUIT, RESIZABLE
import time
class Game:

    def __init__(self):
        self.is_playing=False
        self.all_players =pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed={}
        self.all_monster= pygame.sprite.Group()
        self.score=0
    def start(self):
        self.is_playing=True
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()
    def game_over(self):
        self.all_monster=pygame.sprite.Group()
        self.player.health=self.player.max_health
        self.score=0
    def update(self,fenetre,a,continuer):



        background = pygame.image.load('assets/1200px-SSBU-Pokémon_Stadium_2.webp')
        fenetre.blit(background, (0, 0))
        a += 1
        fenetre.blit(background, (0, 0))

        fenetre.blit(self.player.image, self.player.rect)

        font = pygame.font.SysFont("monospace", 50)
        score_text = font.render(f"Score : {self.score}", 1, (255, 0, 0))
        fenetre.blit(score_text, (50, 50))

        for projectile in self.player.all_projectiles:
            projectile.move(self.player)
            # print(projectile.rect.x,projectile.rect.y)
            # print(game.player.alpha)
        for monster in self.all_monster:
            if a % 2 == 0:
                monster.move_line()
            monster.update_health_bar(fenetre)

        self.player.all_projectiles.draw(fenetre)

        self.all_monster.draw(fenetre)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 900:
            self.player.move_right()
            # fenetre.blit(background, (0, 0))
            # game.player.all_projectiles.draw(fenetre)
            # game.all_monster.draw(fenetre)
            # monster.update_health_bar(fenetre)
            # for monster in game.all_monster:
            # monster.update_health_bar(fenetre)
            # fenetre.blit(game.player.image, game.player.rect)


        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:

            # fenetre.blit(background, (0, 0))
            # game.player.all_projectiles.draw(fenetre)
            # game.all_monster.draw(fenetre)
            # monster.update_health_bar(fenetre)
            # for monster in game.all_monster:
            # monster.update_health_bar(fenetre)
            # fenetre.blit(game.player.image, game.player.rect)
            self.player.move_left()

        elif self.pressed.get(pygame.K_UP):
            self.player.up()
        elif self.pressed.get(pygame.K_DOWN):
            self.player.down()
        #elif self.pressed.get(pygame.K_SPACE):
            #self.player.launch_projectile()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

                if event.key == pygame.K_SPACE:
                    self.player.launch_projectile()
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

            elif event.type == QUIT:
                 continuer = 0
        return continuer
        #time.sleep(0.01)


    def spawn_monster(self):
        monster=Monster(self  )
        self.all_monster.add(monster)

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)
