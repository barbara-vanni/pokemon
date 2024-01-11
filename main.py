import pygame
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *
from graphics.graphics_functions.render_new_game import *

continuer = True
while continuer:
    render_new_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip()