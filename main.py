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

def sand_floor():
	screen.blit(ground,(floor_x_pos,900))
	screen.blit(ground,(floor_x_pos + 576,900))

def obstacles():
  obstacles_position = random.choice(obstacles_height)
  seaweed = fish_hook.get_rect(midhook = (700, obstacles_position))
  hook = fish_hook.get_rect(midseaweed = (700,obstacles_position - 300))
  return seaweed, hook

def move_obtacles(obs):
  for ob in obs:
    ob.centerx -= 5
  visible_obstacles = [ob for ob in obs if ob.right > -50]
  return visible_obstacles

def draw_obtacles(obs):
  for ob in obs:
    if ob.bottom >= 1024:
      screen.blit(fish_hook, ob)
    else:
      flip_ob = pygame.transform.flip(fish_hook, False, True)
      screen.blit(flip_ob,ob)

def check_collision(obs):
  global can_score
  for ob in obs:
    if fish_rect.colliderect(ob):
      can_score = True
      return False

    if fish_rect.top <= -100 or fish_rect.bottom >= 900:
      can_score = True
      return False
    
    return True

def rotate_bird(fish):
	new_fish = pygame.transform.rotozoom(fish,-fish_movement * 3,1)
	return new_fish

def fish_animation():
	new_fish = fish_frames[fish_index]
	new_fish_rect = new_fish.get_rect(center = (100,fish_rect.centery))
	return new_fish,new_fish_rect

#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 30
FramePerSec = pygame.time.Clock()
 
#screen
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
#setting up images
background = pygame.image.load("ASSETS/background.png")
background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
ground = pygame.image.load("ASSETS/ground.png")
floor_x_pos = 0
gameOver = pygame.image.load("ASSETS/gameover.png")
mainTitle = pygame.image.load("ASSETS/flippyfish.png")
fish_hook = pygame.image.load("ASSETS/Fish Hook.png")

#Create a white screen 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")

#Getting Obstacles to work
create_hook= pygame.USEREVENT
pygame.time.set_timer(create_hook,1200)
obstacles_height = [400,600,800]

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
    screen.blit(fish_hook, (0,-300))
    screen.blit(ground, (0,500))
    P1.move()
    velocity = 0
    velocity += gravity
    P1.rect.centery += velocity
    pygame.display.update()
    FramePerSec.tick(FPS)



