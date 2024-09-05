import pygame
import math


# pycaster variables
res = 800
border_size = 3
line_width = 3
cnt = 0
map = [
  [1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1],
  [1,0,0,1,0,0,0,1],
  [1,1,0,0,0,0,1,1],
  [1,0,0,0,0,0,0,1],
  [1,1,0,0,0,0,1,1],
  [1,0,0,1,0,0,0,1],
  [1,1,1,1,1,1,1,1],
]
grid_size = int(res/len(map))
radius = (res/grid_size) / 2
print(grid_size)
player_pos = pygame.Vector2(res / 2, res / 2)
# ray settings
theta = math.radians(0) # initial ray
ray_count = 5
assert ray_count % 2 == 1 # ray_count needs to be odd
ray_count += 1 # we will do range 1, ray_count; cannot work with 0
fov = math.radians(30)
look_sens = 2
# pygame setup
pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()
running = True
delta_time = 0

# def draw_slice(i, wall_height, slice_width):
#   for (let j = 0; j < wallHeight; j++):

def draw_grid():
  # draw grid
  for i in range(len(map)):
    for j in range(len(map)):
      if map[i][j] == 1:
        pygame.draw.rect(screen, "red", (i * grid_size, j * grid_size, grid_size - border_size, grid_size - border_size))
      else:
        pygame.draw.rect(screen, "white", (i * grid_size, j * grid_size, grid_size - border_size, grid_size - border_size))
def draw_rays():
    # draw player
  pygame.draw.circle(screen, "green", player_pos, 20)
  # draw rays
  for i in range(1, ray_count):
    if i == math.ceil(ray_count / 2):
      cur_theta = theta
    else:
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
  # poll events
  keys = pygame.key.get_pressed()
  # movement
  if keys[pygame.K_w]:
    player_pos.y -= 300 * delta_time
  if keys[pygame.K_s]:
    player_pos.y += 300 * delta_time
  if keys[pygame.K_a]:
    player_pos.x -= 300 * delta_time
  if keys[pygame.K_d]:
    player_pos.x += 300 * delta_time
  # aim
  if keys[pygame.K_LEFT]:
    theta -= look_sens * delta_time
  if keys[pygame.K_RIGHT]:
    theta += look_sens * delta_time
  # other keys
  if keys[pygame.K_q]:
    running = False


  # clear
  screen.fill("black")


  # draw_grid()
  # draw_rays()
  
  # draw screen



  # swap buffer
  pygame.display.flip()
  delta_time = clock.tick(60) / 1000
pygame.quit()
