import pygame
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *
from graphics.graphics_functions.render_new_game import *
from graphics.graphics_functions.render_pokemon_choice import *
from Event import *

continuer = True
while continuer:
    render_pokemon_choices()
    event = Event()
    event_boucle_result = event.event_boucle()
    continuer = event.quit_event(continuer, event_boucle_result)
    pygame.display.flip()
