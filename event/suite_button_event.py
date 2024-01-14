import pygame
from graphics.graphics_attributes import *

def suite_button_event(event, suite_button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if get_combat() == 1 or get_combat() == 2:
            if suite_button.get_clicked() == True:
                set_combat(3)
        elif get_combat() == 3:
            if suite_button.get_clicked() == True:
                set_combat(0)