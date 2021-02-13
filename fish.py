import pygame, sys
from pygame.locals import *
import random, time
#start in the middle of the screen
#jumps up and always is falling down
#tilts up and down
#with going up it goes 45 degrees
#with going down it goes 45 degrees down 
class Player(pygame.spire.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("YellowFish.png")
    self.surf = pygame.Surface((40,40))
    self.rect = self.surf.get_rect(center = (0,640))
  def move(self):
    keyPress = pygame.key.get_pressed()
    if pressed_keys[K_SPACE]:
      self.rect.move_ip(0,5)


