import pygame 


def texts(score):
  font=pygame.font.Font(None,30)
  scoretext=font.render("Score: "+str(score), 1,(0,0,0))
  screen.blit(scoretext, (0, 0))