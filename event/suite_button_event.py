import pygame
from graphics.graphics_attributes import *
from game.games_attributes import *

def suite_button_event(event, suite_button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        suite_button.collision
        if get_combat() == 1 or get_combat() == 2:
            if suite_button.get_clicked() == True:
                combat_begin.set_states(1)
                set_combat(3)
        elif get_combat() == 3 and combat_begin.get_states() == 1:
            if suite_button.get_clicked() == True:
                combat_begin.set_states(2)
        elif get_combat() == 3 and combat_begin.get_states() == 2:
            if suite_button.get_clicked() == True:
                combat_begin.set_states(1)
                set_combat(2)