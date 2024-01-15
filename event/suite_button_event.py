import pygame
from graphics import *
from game import *

# def suite_button_event(event, suite_button):
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         suite_button.collision
#         if get_combat() == 1 or get_combat() == 2:
#             if suite_button.get_clicked() == True:
#                 combat_begin.set_states(1)
#                 set_combat(3)
#         elif get_combat() == 3 and combat_begin.get_states() == 1:
#             if suite_button.get_clicked() == True:
#                 combat_begin.set_states(2)
#         elif get_combat() == 3 and combat_begin.get_states() == 2:
#             if suite_button.get_clicked() == True:
#                 combat_begin.set_states(1)
#                 set_combat(2)

def suite_button_event(event, suite_button):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if get_combat() == 1:
            if suite_button.get_clicked():
                if combat_begin.get_attack_chance_ratio() == 0:
                    combat_begin.end_attack()
                set_combat(2)
                combat_begin.attack()
                suite_button.collision()

        suite_button.get_clicked()
        if get_combat() == 2:
            if suite_button.get_clicked() == True:
                mort = combat_begin.end_game()
                if mort == True:
                    level_up = combat_begin.gain_xp()
                    if level_up == True:
                        set_combat(4)
                    else:
                        set_combat(3)