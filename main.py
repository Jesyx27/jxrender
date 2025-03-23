import sys
import pygame
import math
from rotation import Rotation
from position import Position
from scene import Scene
from object import Object
from camera import Camera
from mesh.vertex import Vertex
from mesh.mesh import Mesh
from mesh.face import Face
from mesh.edge import Edge

pygame.init()
 
fps = 30
fpsClock = pygame.time.Clock()
 
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))

# Rotation: x=roll, y=pitch, z=yaw

vertices_cube = {
  "far_rgt_top": Vertex(Position(1, 1, 2), "local"),
  "far_lft_top": Vertex(Position(1, -1, 2), "local"),
  "cls_rgt_top": Vertex(Position(-1, 1, 2), "local"),
  "cls_lft_top": Vertex(Position(-1, -1, 2), "local"),
  "far_rgt_bot": Vertex(Position(2, 2, -1), "local"),
  "far_lft_bot": Vertex(Position(2, -2, -1), "local"),
  "cls_rgt_bot": Vertex(Position(-2, 2, -1), "local"),
  "cls_lft_bot": Vertex(Position(-2, -2, -1), "local"),
}

verteces_pyramid = {
  "top": Vertex(Position(0, 0, -5), "local"),
  "far_rgt": Vertex(Position(1, 1, -2), "local"),
  "far_lft": Vertex(Position(1, -1, -2), "local"),
  "cls_rgt": Vertex(Position(-1, 1, -2), "local"),
  "cls_lft": Vertex(Position(-1, -1, -2), "local"),
}


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

ORIG_ROTATION = Rotation(math.pi/2, 0, 0)
ORIG_POSITION = Position(0, -10, 0)

cube_mesh = Mesh(faces=[
  Face([vertices_cube["far_rgt_top"], vertices_cube["far_lft_top"], vertices_cube["cls_lft_top"], vertices_cube["cls_rgt_top"]], RED),
  Face([vertices_cube["far_rgt_bot"], vertices_cube["far_lft_bot"], vertices_cube["cls_lft_bot"], vertices_cube["cls_rgt_bot"]], GREEN),
  Face([vertices_cube["far_rgt_top"], vertices_cube["far_rgt_bot"], vertices_cube["cls_rgt_bot"], vertices_cube["cls_rgt_top"]], BLUE),
  Face([vertices_cube["far_lft_top"], vertices_cube["far_lft_bot"], vertices_cube["cls_lft_bot"], vertices_cube["cls_lft_top"]], MAGENTA),
  Face([vertices_cube["far_rgt_top"], vertices_cube["far_lft_top"], vertices_cube["far_lft_bot"], vertices_cube["far_rgt_bot"]], YELLOW),
  Face([vertices_cube["cls_rgt_top"], vertices_cube["cls_lft_top"], vertices_cube["cls_lft_bot"], vertices_cube["cls_rgt_bot"]], AQUA),
])
pyramid_mesh = Mesh(faces=[
    Face([verteces_pyramid["top"], verteces_pyramid["far_rgt"], verteces_pyramid["far_lft"]], RED),
    Face([verteces_pyramid["top"], verteces_pyramid["far_rgt"], verteces_pyramid["cls_rgt"]], GREEN),
    Face([verteces_pyramid["top"], verteces_pyramid["cls_rgt"], verteces_pyramid["cls_lft"]], BLUE),
    Face([verteces_pyramid["top"], verteces_pyramid["cls_lft"], verteces_pyramid["far_lft"]], MAGENTA),
    Face([verteces_pyramid["far_rgt"], verteces_pyramid["far_lft"], verteces_pyramid["cls_lft"], verteces_pyramid["cls_rgt"]], YELLOW)
])

cube = Object("cube", [0, 0, 0], Rotation(0, 0, 0), cube_mesh)
pyramid = Object("pyramid", [0, 0, 0], Rotation(0, 0, 0), pyramid_mesh)
floor = Object("floor", [0, 0, 0], Rotation(0, 0, 0), Mesh(faces=[Face([Vertex(Position(1, 1, -1)), Vertex(Position(1, -1, -1)), Vertex(Position(-1, -1, -1)), Vertex(Position(-1, 1, -1))], WHITE)]))
camera = Camera(ORIG_POSITION, rotation=ORIG_ROTATION, fov=90)

font = pygame.font.Font(None, 36)
scene = Scene("main", [cube, pyramid, floor], camera=camera, sheet=screen)

# Game loop.
while True:
  screen.fill((0, 0, 0))
  scene.render()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  dx, dy = pygame.mouse.get_rel()
  camera.rotation.rotate([0, dx/100, 0])

  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_w]:
    camera.walk("forward")
  if pressed[pygame.K_s]:
    camera.walk("backward")
  if pressed[pygame.K_a]:
    camera.walk("left")
  if pressed[pygame.K_d]:
    camera.walk("right")
  if pressed[pygame.K_SPACE]:
    print('Space!')
    camera.rotation = ORIG_ROTATION
    camera.position = ORIG_POSITION

  camera.rotation.rotate([
    (pressed[pygame.K_x] / 10) * (-1 if pressed[pygame.K_LSHIFT] else 1),
    (pressed[pygame.K_y] / 10) * (-1 if pressed[pygame.K_LSHIFT] else 1),
    (pressed[pygame.K_z] / 10) * (-1 if pressed[pygame.K_LSHIFT] else 1)
  ])

  rot_text = font.render("{:.1f}, {:.1f}, {:.1f}".format(camera.rotation.x, camera.rotation.y, camera.rotation.z), False, (255, 255, 255))
  pos_text = font.render("{:.1f}, {:.1f}, {:.1f}".format(camera.position.x, camera.position.y, camera.position.z), False, (255, 255, 255))
  [screen.blit(text, (5, 5+30*i)) for i, text in enumerate([rot_text, pos_text])]

  # Update.
  
  # Draw.
  
  pygame.display.flip()
  fpsClock.tick(fps)