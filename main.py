import pygame
from event import *
from game import *
from game.current_render import *
from graphics import *


running = True
attack_button = None

while running:

    # universal event handler ( à mettre seulement ici !)
    if pygame.event.Event(pygame.QUIT) in pygame.event.get():
        running = False
    # get_state (who is a function) returns the function to be executed
    get_state()()

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


    pygame.display.flip()
