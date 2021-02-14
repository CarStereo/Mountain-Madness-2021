#
import pygame, sys, os
from pygame.locals import *
import random, time
import fish
#import score

def menus(score, state):
  font = pygame.font.Font("ASSETS/GrinchedRegular.otf", 30)
  if state == 'main game':
    scoreText = font.render("Score: "+str(score), 1,(255, 198, 0, 255))
    scoreRect = scoreText.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/8))
    screen.blit(scoreText, scoreRect)

  elif state == 'game over':
    scoreSurface = font.render("Score: "+str(score) ,1,(255, 198, 0, 255))
    scoreRect = scoreSurface.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/8))
    screen.blit(scoreSurface,scoreRect)
    gameOverRect = gameOver.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(gameOver, gameOverRect) 
    highScoreSurf = font.render("High Score: "+str(HIGHSCORE),1,(255, 198, 0, 255))
    highScoreRect = highScoreSurf.get_rect(center = (SCREEN_WIDTH/2,SCREEN_WIDTH/3))
    screen.blit(highScoreSurf,highScoreRect)
  else:
    return

  

def scoreUpdate(obs):
  #obs is an array of the obstacles
  #add points if an obstacle makes it past the fishes postion
  for ob in obs:
    if ob.centerx < SCREEN_WIDTH / 4 and ob.centerx > (SCREEN_WIDTH /4) - 10:
      return 5
  return 0

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
  global death
  for ob in obs:
    if P1.rect.colliderect(ob):
      #print("you die")
      death = True
      return False

    if P1.rect.top <= 0 or P1.rect.bottom >= 600:
      #print("out of bounds")
      death = True
      return False
    
  return True

def updateHighScore(hs,s):
  file = open("scores.txt", "w")
  if(hs < s):
    file.truncate()
    file.write(str(hs))
    file.close()
    return hs
  else:
    filesize = os.path.getsize("scores.txt")
    if filesize == 0:
      file.truncate()
      file.write(str(s))
      file.close()
      return s
    else:
      oldHs = file.read()
      return oldHs


#do not know if we are going to implement
def rotate_bird(fish):
	P1 = pygame.transform.rotozoom(fish,-fish_movement * 3,1)
	return P1

def fish_animation():
	P1 = fish_frames[fish_index]
	new_P1.rect = P1.get_rect(center = (100,P1.rect.centery))
	return P1,new_P1.rect

#Initializing 
pygame.init()
gameState = str('start menu')
isAlive = True
#Setting up FPS 
FPS = 30
FramePerSec = pygame.time.Clock()
 
#screen
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
SPEED = 5
#setting up images
background = pygame.image.load("ASSETS/background.png")
background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))
startMenu = pygame.image.load("ASSETS/menu.png")
startMenu = pygame.transform.scale(startMenu,(SCREEN_WIDTH,SCREEN_HEIGHT))
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

#score tracking
SCORE = 0
HIGHSCORE = 0

sMenu = True

def startUp(inMenu):
  while inMenu:
    #start menu
    for event in pygame.event.get():    
      if event.type == QUIT:
        pygame.quit()
        sys.exit()    
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          inMenu = False
    
    screen.blit(background, (0,0)) 
    screen.blit(ground, (0,525))
    screen.blit(startMenu, (0,0)) 
    pygame.display.update()
    FramePerSec.tick(FPS)
  
startUp(sMenu)

while True:
  #Cycles through all events occurring  
    for event in pygame.event.get():    
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

        if event.type == SPAWNHOOK:
          hookList.extend(obstacles())       

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE and not isJumping:
            gameState = 'main game'
            isJumping = True
            
          elif isJumping:
            isJumping = False
        if event.type == pygame.KEYUP:
          isJumping = False
    
    screen.blit(background, (0,0)) 
    screen.blit(ground, (0,525))
    
    if isAlive: 
      velocity = P1.jump(isJumping)
      velocity += gravity
      screen.blit(P1.image,P1.rect)
      P1.rect.centery += velocity 

      hookList = moveObstacles(hookList)
      hookList = removeObstacles(hookList)
      drawObstacles(hookList)
      isAlive = checkCollision(hookList) 
      newScore = scoreUpdate(hookList)
      SCORE += newScore
      
      menus(SCORE,gameState)

    else:
      #bird died
      gameState = 'game over'
      HIGHSCORE = updateHighScore(HIGHSCORE,SCORE)
      menus(SCORE, gameState)

  
    pygame.display.update()
    FramePerSec.tick(FPS)