#
import pygame, sys
from pygame.locals import *
import random, time
import fish
#import score

def texts(score):
  font=pygame.font.Font(None,30)
  scoretext=font.render("Score: "+str(score), 1,(0,0,0))
  screen.blit(scoretext, (0, 0))

#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 30
FramePerSec = pygame.time.Clock()
 
#screen
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
 
#setting up images
background = pygame.image.load("ASSETS/background.png")
background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
ground = pygame.image.load("ASSETS/ground.png")
gameOver = pygame.image.load("ASSETS/gameover.png")
mainTitle = pygame.image.load("ASSETS/flippyfish.png")

#Create a white screen 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Game")

#creating the fish
P1 = fish.Player()
gravity = 5
velocity = 0
while True:
  #Cycles through all events occurring  
    for event in pygame.event.get():    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    screen.blit(background, (0,0))     
    texts(SCORE)
    screen.blit(P1.image,P1.rect)
    P1.move()
    velocity = 0
    velocity += gravity
    P1.rect.centery += velocity
    pygame.display.update()
    FramePerSec.tick(FPS)

