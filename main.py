#
import pygame, sys, os
from pygame.locals import *
import random, time
import fish
#import score

def menus(score, highscore, state):
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

  

def scoreUpdate(obs, s):
  #obs is an array of the obstacles
  #add points if an obstacle makes it past the fishes postion
  
  for ob in obs:
    if ob.centerx < SCREEN_WIDTH / 4 and ob.centerx > (SCREEN_WIDTH /4) - 10:
      fishString = fishColours.pop(0)
      #change the fish
      P1.image = pygame.image.load(fishString)
      P1.image = pygame.transform.scale2x(P1.image)
      P1.surf = pygame.Surface((40,40))
      fishColours.append(fishString)
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
    if ob.centerx <= -26 or not isAlive:
        hookList.remove(ob)
  return obs

def checkCollision(obs):
  global death
  for ob in obs:
    if P1.rect.colliderect(ob):
      hitSound.play()
      #print("you die")
      death = True
      return False

    if P1.rect.top <= 0 or P1.rect.bottom >= 600:
      hitSound.play()
      #print("out of bounds")
      death = True
      return False
    
  return True

def updateHighScore(hs,s):
  #create a new file if there isnt one
  #if the hgih score is less than the new score
  #   overwrite what is on the file as the new high score
  #   return the new hs
  #else check if the file is empty
  #if it is then write a new hs and return s
  #else, return the old hs from the file
  file = open("scores.txt", "w")
  if(hs < s):
    file.truncate()
    file.write(str(hs))
    file.close()
    return s
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
def paused(pause):
  font = pygame.font.Font("ASSETS/GrinchedRegular.otf", 30)
  textSurf = font.render("Paused", 1,(255, 198, 0, 255))
  textRect = textSurf.get_rect(center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)))
  screen.blit(textSurf, textRect)


  while pause:
      for event in pygame.event.get():

          if event.type == pygame.QUIT:
              pygame.quit()
              quit()
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not isJumping:
              pause = False
        #gameDisplay.fill(white)
      pygame.display.update()

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
fishColours = ["ASSETS/YellowFish.png", "ASSETS/OrangeFish.png", "ASSETS/GreenFish.png", "ASSETS/FullGreenFish.png", "ASSETS/PurpleFish.png", "ASSETS/BlueFish.png"]

def checkColour(s):
  return
    
#score tracking
SCORE = 0
HIGHSCORE = 0

sMenu = True

swimSound = pygame.mixer.Sound('sfx/sfx_swim.wav')
hitSound = pygame.mixer.Sound('sfx/sfx_hit.wav')

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
          if isAlive:
            hookList.extend(obstacles())       

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE and not isJumping:
            swimSound.play()
            gameState = 'main game'
            isJumping = True
          elif isJumping:
            isJumping = False
        if event.type == pygame.KEYUP:
          isJumping = False

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_p:
            pause = True
            paused(pause)
          if event.key == pygame.K_ESCAPE and not isAlive:
            gameState = 'main game'
            isAlive = True
            P1 = fish.Player()
            SCORE = 0
            for hook in hookList:
              hookList.remove(hook)
    
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
      newScore = scoreUpdate(hookList,SCORE)
      SCORE += newScore
      menus(SCORE,HIGHSCORE,gameState)
      checkColour(SCORE)

    else:
      #bird died
      gameState = 'game over'
      HIGHSCORE = updateHighScore(HIGHSCORE,SCORE)
      if(HIGHSCORE < SCORE):
        HIGHSCORE = SCORE
      menus(SCORE,HIGHSCORE, gameState)
          
  
    pygame.display.update()
    FramePerSec.tick(FPS)