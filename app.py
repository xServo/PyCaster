import pygame
import math
import time


# pycaster variables
res = 800
near_plane = 40
far_plane = 600
view_distance = far_plane - near_plane
border_size = 3
line_width = 3
cnt = 0
is_map = True
map = [
  [1,1,1,1,1,1,1,1],
  [1,0,0,0,1,1,1,1],
  [1,0,0,0,0,0,0,1],
  [1,1,0,0,0,0,1,1],
  [1,0,0,0,0,0,0,1],
  [1,1,0,0,0,0,1,1],
  [1,0,0,1,0,1,1,1],
  [1,1,1,1,1,1,1,1],
]
grid_size = int(res/len(map))
radius = (res/grid_size) / 2
print(grid_size)
player_pos = pygame.Vector2(res / 2, res / 2)
# ray settings
theta = math.radians(0) # initial ray
ray_count = 20
assert ray_count % 2 == 0 # ray_count needs to be even
ray_count += 1 # we will do range 1, ray_count; cannot work with 0
fov = math.radians(30)
look_sens = 2
# graphics settings
wall_res = 20
assert wall_res % 2 == 0 # wall_res needs to be even
# pygame setup
pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()
running = True
delta_time = 0
column_size = res / ray_count

def is_in_bounds(new_x, new_y, grid_size):
  grid_x = int(new_x / grid_size)
  grid_y = int(new_y / grid_size)

  # Check if the new position is within map bounds
  if grid_x < 0 or grid_x >= len(map[0]) or grid_y < 0 or grid_y >= len(map):
    return False

  return map[grid_y][grid_x] == 0


def draw_grid():
  for i in range(len(map)):
    for j in range(len(map)):
      if map[i][j] == 1:
        pygame.draw.rect(screen, "red", (j * grid_size, i * grid_size, grid_size - border_size, grid_size - border_size))
      else:
        pygame.draw.rect(screen, "white", (j * grid_size, i * grid_size, grid_size - border_size, grid_size - border_size))

def draw_wall(column, size):
  size += wall_res / 2 # accounts for tile missing on bottom and top of screen
  column += 1 # deals with zero index multiplication problem
  # pygame.draw.rect(screen, "red", (column * column_size, //// size / wall_res, column_size, res - 2*(size / wall_res))) # needs work TODO TODO TODO
  y_offset = (wall_res-size)*(res/wall_res)
  pygame.draw.rect(screen, "red", (column * column_size, y_offset, column_size+1, res - y_offset*2)) # needs work TODO TODO TODO

def draw_rays():
    # draw player
  pygame.draw.circle(screen, "green", player_pos, 20)
  # draw rays
  for i in range(1, ray_count):
    # if i == math.ceil(ray_count / 2):
    #   cur_theta = theta
    # else:
    cur_theta = theta + ((fov / ray_count) * i)

    end_pos_x = player_pos.x / grid_size
    end_pos_y = player_pos.y / grid_size
    dx = math.cos(cur_theta)
    dy = math.sin(cur_theta)
    # increment until a wall is hit
    incr = 0
    while (map[math.floor(end_pos_y)][math.floor(end_pos_x)] == 0):
      end_pos_x += dx * 0.05
      end_pos_y += dy * 0.05
      incr += 1
      if incr > 300:
        break  
      # distance = Math.sqrt((x - this.player.x) ** 2 + (y - this.player.y) ** 2);
      # wall_height = 300 / distance;
    end_pos = pygame.Vector2(end_pos_x * grid_size,end_pos_y * grid_size)
    pygame.draw.line(screen, "blue", player_pos, end_pos, line_width)

    # debug
    # print("end x: ", end_pos_x)
    # print("end y: ", end_pos_y)
    # print("player x: ", player_pos.x / grid_size)
    # print("player y: ", player_pos.y / grid_size)
    # # minimalistic-crossplatform clear
    # print("\n\n\n\n\n\n\n\n\n\n\n")



# main loop
while running:
  # poll for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN: 
      # toggle map
      if event.key == pygame.K_r:
        if is_map:
          is_map = False
        else:
          is_map = True
  # poll events
  keys = pygame.key.get_pressed()
  # movement
  if keys[pygame.K_w]:
    new_x = player_pos.x + math.cos(theta) * 300 * delta_time
    new_y = player_pos.y + math.sin(theta) * 300 * delta_time

    if is_in_bounds(new_x, new_y, grid_size):
        player_pos.x = new_x
        player_pos.y = new_y

  if keys[pygame.K_s]:
    new_x = player_pos.x - math.cos(theta) * 300 * delta_time
    new_y = player_pos.y - math.sin(theta) * 300 * delta_time

    if is_in_bounds(new_x, new_y, grid_size):
        player_pos.x = new_x
        player_pos.y = new_y

  if keys[pygame.K_a]:
    new_x = player_pos.x + math.sin(theta) * 300 * delta_time
    new_y = player_pos.y - math.cos(theta) * 300 * delta_time

    if is_in_bounds(new_x, new_y, grid_size):
        player_pos.x = new_x
        player_pos.y = new_y

  if keys[pygame.K_d]:
    new_x = player_pos.x - math.sin(theta) * 300 * delta_time
    new_y = player_pos.y + math.cos(theta) * 300 * delta_time

    if is_in_bounds(new_x, new_y, grid_size):
        player_pos.x = new_x
        player_pos.y = new_y

  # aim
  if keys[pygame.K_LEFT]:
    theta -= look_sens * delta_time
  if keys[pygame.K_RIGHT]:
    theta += look_sens * delta_time
  # quit game
  if keys[pygame.K_q]:
    running = False

  # clear
  screen.fill("black")

  if is_map:
    draw_grid()
    draw_rays()
  else:
    pygame.draw.rect(screen, "grey", (0, res/2, res, res))
    for i in range(1, ray_count):
      cur_theta = theta + ((fov / ray_count) * i)

      end_pos_x = player_pos.x / grid_size
      end_pos_y = player_pos.y / grid_size
      dx = math.cos(cur_theta)
      dy = math.sin(cur_theta)
      # increment until a wall is hit
      incr = 0
      while (map[math.floor(end_pos_y)][math.floor(end_pos_x)] == 0):
        end_pos_x += dx * 0.05
        end_pos_y += dy * 0.05
        incr += 1
        if incr > 300:
          draw_wall(i, 0)
          break  
      end_pos_x *= grid_size
      end_pos_y *= grid_size
      distance = math.sqrt((player_pos.x - end_pos_x) ** 2 + (player_pos.y - end_pos_y) ** 2)

      if distance != 0:
        inverted_distance = 1 / distance
      else:
        inverted_distance = 5000

      draw_wall(i - 1, inverted_distance*wall_res*50)
  



  # swap buffer
  pygame.display.flip()
  delta_time = clock.tick(60) / 1000
pygame.quit()
