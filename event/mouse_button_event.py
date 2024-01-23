import pygame
from graphics import *

def mouse_button_event(event, button_object):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_object.render(screen) == True:
            set_menu(1)