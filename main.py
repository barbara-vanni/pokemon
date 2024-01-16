import pygame
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *
from graphics.graphics_functions.render_new_game import *
from graphics.graphics_functions.render_pokemon_choice import *
from event.quit import *
from event.mouse_button_event import *
# from game.render_states import *

continuer = True


while continuer:
    # new_game, continu, option = render_main()
    pokemon_good, nom_good, pv_good, pokemon_bad, nom_bad, pv_bad, attack_button, object_button, flee_button, new_pokemon_button = render_combat()
    for event in pygame.event.get():
        continuer = quit_event(event, continuer)
        # mouse_button_event(event, new_game, font_ingame, screen)
    pygame.display.flip()
