import states
from graphics.graphics_functions.render_main import *
from graphics.graphics_functions.render_combat import *
from graphics.graphics_functions.render_new_game import *
from graphics.graphics_functions.render_pokemon_choice import *

def render():
    menu = get_menu()
    match menu:
        case states.MENU:
            new_game, continu, option = render_main()
        case states.NORMAL:
            pokemon_good, nom_good, pv_good, pokemon_bad, nom_bad, pv_bad, attack_button, object_button, flee_button, new_pokemon_button = render_combat()
        
    pygame.display.flip()

# menu_state = "main_menu"
# running = True

# def render_menu():
#     global menu_state, state, running
#     if intro_menu == True :
#         # if we are in the intro page render the intro image
#         screen.blit(intro_menu_img, (0,0))
#     if continu_button.draw(screen):
#         state = "game_menu"
#     if new_game_button.draw(screen):
#         state = "new_game_menu"
#     if option_button.draw(screen):
#         state = "option_menu"
#     if quit_button.draw(screen):
#         running = False
#     return render_menu

# state = render_menu 


# base de la fonction pour l'etat du jeu quand le bouton continuer est cliqué
# def game_menu():
#     global state
# return game_menu