import pygame
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *
from graphics.graphics_functions.render_new_game import *
from graphics.graphics_functions.render_pokemon_choice import *
from game.games_attributes import *
from game.games_classes.Combat import *
from event.quit import *
from event.mouse_button_event import *
from event.attack_button_event import *
from event.suite_button_event import *

continuer = True
attack_button = None

while continuer:
    if get_menu() == 0:
        new_game, continu, option = render_main()
    elif get_menu() == 1:
        if get_combat() == 0:
            attack_button, object_button, flee_button, new_pokemon_button = render_combat(pokemon1, pokemon2)
        elif get_combat() == 1 or get_combat() == 2 or get_combat() == 3:
            suite_button = render_combat(pokemon1, pokemon2)

    for event in pygame.event.get():
        continuer = quit_event(event, continuer)
        mouse_button_event(event, new_game)
        if get_menu() == 1:
            if get_combat() == 0:
                attack_button_event(event, attack_button)
            elif get_combat() == 1 or get_combat() == 2 or get_combat() == 3:
                suite_button_event(event, suite_button)
                combat_begin.fight()
    pygame.display.flip()
