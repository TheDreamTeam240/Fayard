import pygame
from pytmx.util_pygame import load_pygame
from pathlib import Path
import pyscroll

pygame.init()
pygame.display.set_caption("Faillearr_simulator")
screen = pygame.display.set_mode((1920, 1080))

tmx_data = load_pygame("faille_arr_sim_map.tmx")
map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

bool_window = True

while bool_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            bool_window = False

    group.draw(screen)

    pygame.display.flip()

pygame.quit()
