from graphics.graphics_attributes import *
from graphics.graphics_classes.Message import *
from graphics.graphics_classes.Button import *
from graphics.graphics_functions.render_new_game import *
import graphics.graphics_functions.render_combat as render_combat
from graphics.graphics_functions.render_main import *
import graphics.graphics_functions.render_pokedex_menu as render_pokedex
from game.current_render import *
import game.current_render as Current_render
from game.games_attributes import *
import graphics.graphics_functions.render_choose_fight as Render_choose_fight



def render_main_menu():
    bcg_main_menu = Image('./assets/images/main_menu.png', (0, 0))
    bcg_main_menu.draw_image(screen)
    titre = Message(99, 53, 600, 120, 'POKEMON', 'white', 'red')
    titre.message_render(font_title, screen)
    titre = Message(104, 54, 600, 120, 'POKEMON', 'white', 'orange')
    titre.message_render(font_title, screen)
    titre = Message(106, 56, 600, 120, 'POKEMON', 'white', 'orange')
    titre.message_render(font_title, screen)
    if new_game_button.render(screen):
        pokedex.cleanup_trainer_file()
        Current_render.set_state(render_new_game)

    if continue_button.render(screen):
        if pokedex.choose_trainer_file() == None:
            message = Message(250, 450, 300, 100, 'No save file', 'white', 'black')
            message.message_render(font_button_menu, screen)
            pygame.display.update()
            pygame.time.delay(1000)
        else:
            selected_trainer_file = pokedex2.choose_trainer_file()
            trainer.set_name_trainer(selected_trainer_file)
            pokemon = pokedex2.choose_your_pokemon(trainer.get_name_trainer())
            trainer.set_actif_pokemon(pokemon)
            set_pokemon1(trainer.get_actif_pokemon())
            trainer.add_pokemon(get_pokemon1())
            pokedex2.change_pokemon_trainer(trainer.get_name_trainer(), get_pokemon1())
            Current_render.set_state(Render_choose_fight.render_choose_fight)
            pokedex2.load_from_json(trainer.get_name_trainer())

