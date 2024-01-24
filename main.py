import pygame
from game import *
from graphics import *

continuer = True
attack_button = None

# while running:

    # universal event handler ( à mettre seulement ici !)
    # if pygame.event.Event(pygame.QUIT) in pygame.event.get():
    #     running = False

    # get_state (who is a function) returns the function to be executed
    # get_state()()
    # event handler
    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         # if input_rect.collidepoint(event.pos):
    #         #     active = True
    #         # else:
    #             active = False
    #     if event.type == pygame.KEYDOWN:
    #         if active:
    #             if event.key == pygame.K_BACKSPACE:
    #                 # get text input from 0 to -1 i.e. end.
    #                 user_text = user_text[:-1]
    #             # elif event.key == pygame.K_RETURN:
    #                 # Save the entered name to the JSON file when Enter key is pressed
    #                 # save_data(user_text, 0)  
    #             else:
    #                 user_text += event.unicode
    #                 if event.key == pygame.K_SPACE:
    #                     game_paused = True
    #     if event.type == pygame.QUIT:
    #         running = False

continuer = True
attack_button = None

while continuer:
    render_combat_pokemon()
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
