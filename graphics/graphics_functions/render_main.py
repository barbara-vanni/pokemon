from graphics.graphics_attributes import *
from graphics.graphics_classes.Message import *
from graphics.graphics_classes.Button import *
from graphics.graphics_functions.render_new_game import *
import graphics.graphics_functions.render_combat as render_combat
from graphics.graphics_functions.render_main import *
# from graphics.graphics_functions.render_pokedex_menu import render_pokedex_menu
import graphics.graphics_functions.render_pokedex_menu as render_pokedex
from game.current_render import *
import game.current_render as Current_render
from game.games_attributes import *
from graphics.graphics_functions.render_choose_fight import *



def render_main_menu():

    titre = Message(100, 50, 600, 120, 'POKEMON', 'white', 'blue')
    titre.message_render(font_title, screen)
    if new_game_button.render(screen):
        Current_render.set_state(render_new_game)

    if continue_button.render(screen):
        Current_render.set_state(render_combat.render_combat_pokemon)  

    if option_button.render(screen):
        Current_render.set_state(render_choose_fight)