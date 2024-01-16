import pygame
from graphics import *
from game import *

turn_number = 0

def suite_button_event(event, suite_button):
    global turn_number
    if event.type == pygame.MOUSEBUTTONDOWN:
        if get_combat() == 1:
            if suite_button.get_clicked():
                if combat_begin.get_attack_chance_ratio() == 0:
                    if combat_begin.get_pokemon1() == combat_begin.get_pokemon_player():
                        combat_begin.end_attack()
                        set_combat(1)
                        suite_button.collision()
                    else:
                        combat_begin.end_attack()
                        set_combat(0)
                        suite_button.collision()
                else:
                    set_combat(2)
                    combat_begin.attack_chance()
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
                        suite_button.collision()
                    else:
                        set_combat(3)
                        suite_button.collision()
                else:
                    if turn_number == 1:
                        combat_begin.end_attack()
                        set_combat(0)
                        turn_number = 0
                    else:
                        turn_number += 1
                        combat_begin.end_attack()
                        set_combat(1)
                        suite_button.collision()

        suite_button.get_clicked()
        if get_combat() == 3 or get_combat() == 4:
            if suite_button.get_clicked() == True:
                pokemon1.set_pv(pokemon1.get_pv_max())
                pokemon2.set_pv(pokemon2.get_pv_max())
                set_combat(0)
