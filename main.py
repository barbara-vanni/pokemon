import pygame
from event import *
from game import *
from graphics import *
from game.current_render import *


running = True

running = True
while running:

    # universal event handler ( à mettre seulement ici !)
    if pygame.event.Event(pygame.QUIT) in pygame.event.get():
        running = False

    # get_state (who is a function) returns the function to be executed
    get_state()()

    pygame.display.flip()
