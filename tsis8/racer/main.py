import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
clock = pygame.time.Clock()
 

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0

#Setting up fonts(text)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("images/Street.png")
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")
#setting up background music
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.play(-1)



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin_image = pygame.image.load("images/Coin.png")
        coin_image = pygame.transform.scale(coin_image,(40,40))
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
    def rem(self):
        self.rect.top = 0
        self.rect.center = (random.randint(30, 370), 0)
    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
class Enemy(pygame.sprite.Sprite): #враг
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
  
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
   
 
#setting up sprites         
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating sprites groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == INC_SPEED:
            SPEED += 2
            
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("score:" + str(SCORE), True, BLACK)
    coin_scores = font_small.render( "cash:"+ str(COIN_SCORE) + "$", True,BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coin_scores, (250, 10))
    
    #Moves and Re-draws all Sprites
    for game_object in all_sprites:
        DISPLAYSURF.blit(game_object.image, game_object.rect)
        game_object.move()
        
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("sounds/crash.wav").play()
        time.sleep(0.5)
        
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        DISPLAYSURF.blit(scores,(100, 320))
        DISPLAYSURF.blit(coin_scores, (100, 350))
        
        pygame.display.update()
        for game_object in all_sprites:
            game_object.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            if coin == C1:
                COIN_SCORE += 5
                C1.rem()
                 
    pygame.display.update()
    clock.tick(FPS)