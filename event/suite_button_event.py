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
                        pokedex.change_statistics(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_xp(), combat_begin.get_pokemon1().get_xp_max())
                        pokedex.change_stat_pv(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_pv())
                        set_combat(4)
                        suite_button.collision()
                    else:
                        pokedex.change_stat_pv(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_pv())
                        pokedex.change_stat_xp(combat_begin.get_pokemon1().get_name())
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
                # old_pv = combat_begin.get_pokemon1().get_pv()
                set_pokemon1(pokedex.choose_specific_pokemon("Mewtwo"))
                # combat_begin.get_pokemon1().set_pv(old_pv)
                set_pokemon2(pokedex.choose_random_pokemon())
                set_combat(0)
  
