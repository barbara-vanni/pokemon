import pygame
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *

continuer = True
while continuer:
    render_combat()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip()