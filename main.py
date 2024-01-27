import pygame
from game import *
from graphics import *


running = True
attack_button = None

while running:
    # universal event handler ( à mettre seulement ici !)
    events = pygame.event.get()
    if pygame.event.Event(pygame.QUIT) in events:
        running = False
    if pygame.mouse.get_pressed()[0] == 1:
        set_mouse_click(True)
    else:
        set_mouse_click(False)

    # get_state (who is a function) returns the function to be executed
    get_state()()

    pygame.display.flip()
    clock.tick(60)
