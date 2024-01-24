import pygame
from game import *
from graphics import *

running = True
attack_button = None

while running:

    # universal event handler ( à mettre seulement ici !)
    if pygame.event.Event(pygame.QUIT) in pygame.event.get():
        running = False

    # get_state (who is a function) returns the function to be executed
    get_state()()

# continuer = True
# attack_button = None

# while continuer:
#     render_combat_pokemon()
#     if get_menu() == 0:
#         new_game, continu, option = render_main()
#     elif get_menu() == 1:
#         if get_combat() == 0:
#             attack_button, object_button, flee_button, new_pokemon_button = render_combat(get_pokemon1(), get_pokemon2())
#         elif get_combat() == 1 or get_combat() == 2 or get_combat() == 3 or get_combat() == 4:
#             suite_button = render_combat(get_pokemon1(), get_pokemon2())

#     for event in pygame.event.get():
#         continuer = quit_event(event, continuer)
#         mouse_button_event(event, new_game)
#         if get_menu() == 1:
#             if get_combat() == 0:
#                 attack_button_event(event, attack_button)
#             elif get_combat() == 1 or get_combat() == 2 or get_combat() == 3 or get_combat() == 4:
#                 suite_button_event(event, suite_button)


    pygame.display.flip()
