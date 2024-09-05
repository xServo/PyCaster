import pygame
import math


# pycaster variables
res = 1000
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
# pygame setup
pygame.init()
screen = pygame.display.set_mode((res, res))
clock = pygame.time.Clock()
running = True
delta_time = 0




# main loop
while running:
  # poll for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # poll events
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player_pos.y -= 300 * delta_time
  if keys[pygame.K_s]:
    player_pos.y += 300 * delta_time
  if keys[pygame.K_a]:
    player_pos.x -= 300 * delta_time
  if keys[pygame.K_d]:
    player_pos.x += 300 * delta_time
  if keys[pygame.K_q]:
    running = False

  # clear
  screen.fill("black")


  # draw grid
  for i in range(len(map)):
    for j in range(len(map)):
      if map[i][j] == 1:
        pygame.draw.rect(screen, "red", (i * grid_size, j * grid_size, grid_size - border_size, grid_size - border_size))
      else:
        pygame.draw.rect(screen, "white", (i * grid_size, j * grid_size, grid_size - border_size, grid_size - border_size))

  # draw player
  pygame.draw.circle(screen, "green", player_pos, 20)
  # draw line
  # end_pos_x = (math.floor(player_pos.x / grid_size)) + 1
  # end_pos_y = (math.floor(player_pos.y / grid_size)) + 1

  cnt += 1
  theta = math.radians(30)
  # rotation formula
  end_pos_x = ((player_pos.x / grid_size) * math.cos(theta)) - ((player_pos.y / grid_size) * math.sin(theta))
  end_pos_y = ((player_pos.x / grid_size) * math.sin(theta)) + ((player_pos.y / grid_size) * math.cos(theta))


  # end_pos = pygame.Vector2(end_pos_x * grid_size + grid_size / 2,end_pos_y * grid_size + grid_size / 2)
  end_pos = pygame.Vector2(end_pos_x * grid_size,end_pos_y * grid_size)
  pygame.draw.line(screen, "blue", player_pos, end_pos, line_width)

  print("end x: ", end_pos_x)
  print("end y: ", end_pos_y)
  print("player x: ", player_pos.x / grid_size)
  print("player y: ", player_pos.y / grid_size)
  # minimalistic-crossplatform clear
  print("\n\n\n\n\n\n\n\n\n\n\n")

  # swap buffer
  pygame.display.flip()
  delta_time = clock.tick(60) / 1000
pygame.quit()
