import pygame, sys
from pygame.locals import *
import random, time
import fish.py

#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 30
FramePerSec = pygame.time.Clock()
 
#Other Variables for use in the program
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 1280
SPEED = 5
SCORE = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
fontSmall = pygame.font.SysFont("Verdana", 20)
background = pygame.image.load("")
ground = pygame.image.load("ground.png")
mainTitle = pygame.image.load("")
background = pygame.image.load("AnimatedStreet.jpg") 
#Create a white screen 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Game")

