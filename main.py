import pygame
from graphics.graphics_functions.render_main import *

continuer = True
while continuer:
    render_main()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False