import pygame, sys, random 

def sand_floor():
  screen.blit(floor_surface,(floor_x_pos, 900))
  screen.blit(floor_surface_pos + 576, 900))

def obstacles():
  obstacles_position = random.choice(pipe_height)
  seaweed = ob_surface.get_rect(midhook = 700, obstacles_position)
  hook = ob_surface.get rect(midseaweed = (700,obstacles_position- 300))
return seaweed, hook

def move_obtacles(obs):
  for ob in obs:
    ob.centerx -= 5
  visible_obstacles = [ob for ob in obs if ob.right > -50]
  return visible_obstacles

def draw_obtacles(obs):
  for ob in obs:
    if ob.bottom >= 1024:
      screen.blit(ob_surface, ob)
    else:
      flip_ob = pygame.transform.flip(ob_surface, False, True)
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