#
import pygame, sys
from pygame.locals import *
import random, time
import fish
#import score

def texts(score):
  font = pygame.font.Font("GrinchedRegular.otf", 30)
  scoretext = font.render("Score: "+str(score), 1,(255, 198, 0, 255))
  scoreRect = scoretext.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/8))
  screen.blit(scoretext, scoreRect)

def sand_floor():
	screen.blit(ground,(floor_x_pos,900))
	screen.blit(ground,(floor_x_pos + 576,900))

def obstacles():
  obstaclesHeight = random.randrange(200,500)
  weed = seaweed.get_rect(midtop = (SCREEN_WIDTH, obstaclesHeight))
  hook = fishHook.get_rect(midbottom = (SCREEN_WIDTH,obstaclesHeight - 150))
  return weed, hook

def moveObstacles(obs):
  for ob in obs:
    ob.centerx -= 5
  visible_obstacles = [ob for ob in obs if ob.right > -50]
  return visible_obstacles

def drawObstacles(obs):
  for ob in obs:
    if ob.bottom >= SCREEN_HEIGHT:
      screen.blit(seaweed, ob)
    else:
      screen.blit(fishHook,ob)

def removeObstacles(obs):
  for ob in obs:
    if ob.centerx <= -26:
        hookList.remove(ob)
  return obs

def checkCollision(obs):
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
fishHook = pygame.image.load("ASSETS/Fish Hook.png")
seaweed = pygame.image.load("ASSETS/Seaweed.png")
#Create a white screen 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Game")

#Getting Obstacles to work

hookList = []
SPAWNHOOK = pygame.USEREVENT
pygame.time.set_timer(SPAWNHOOK, 2000)


#creating the fish
P1 = fish.Player()
gravity = 5
velocity = 0
fish_movement = 0
isJumping = False
while True:
  #Cycles through all events occurring  
    for event in pygame.event.get():    
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

        if event.type == SPAWNHOOK:
          hookList.extend(obstacles())
          
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE and  not isJumping:
            isJumping = True
          elif isJumping:
            isJumping = False
        if event.type == pygame.KEYUP:
          isJumping = False

    velocity = P1.jump(isJumping)
    velocity += gravity
    screen.blit(background, (0,0))     
    texts(SCORE)
    screen.blit(P1.image,P1.rect)
    screen.blit(ground, (0,500))
    hookList = moveObstacles(hookList)
    hookList = removeObstacles(hookList)
    drawObstacles(hookList)
    P1.rect.centery += velocity
    pygame.display.update()
    FramePerSec.tick(FPS)
