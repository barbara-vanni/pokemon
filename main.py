import pygame
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *
from graphics.graphics_functions.render_new_game import *
from graphics.graphics_functions.render_pokemon_choice import *
from event.quit import *
from event.mouse_button_event import *
from event.attack_button_event import *

continuer = True

while continuer:
    menu = get_menu()
    combat = get_combat()
    if menu == 0:
        new_game, continu, option = render_main()
    elif menu == 1:
        if combat == 0:
            attack_button, object_button, flee_button, new_pokemon_button = render_combat()
        elif combat == 1:
            render_combat()

    for event in pygame.event.get():
        continuer = quit_event(event, continuer)
        mouse_button_event(event, new_game)
        if menu == 1:
            attack_button_event(event, attack_button)
    pygame.display.flip()
