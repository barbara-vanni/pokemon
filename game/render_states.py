import states
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *
from graphics.graphics_functions.render_new_game import *
from graphics.graphics_functions.render_pokemon_choice import *

def render(menu):
    match menu:
        case states.MENU:
            new_game, continu, option = render_main()
        case states.NORMAL:
            pokemon_good, nom_good, pv_good, pokemon_bad, nom_bad, pv_bad, attack_button, object_button, flee_button, new_pokemon_button = render_combat()
        
    Py.display.flip()