from graphics.graphics_attributes import *
from graphics.graphics_classes.Message import *
from graphics.graphics_classes.Button import *
from graphics.graphics_functions.render_new_game import *
import graphics.graphics_functions.render_combat as render_combat
from graphics.graphics_functions.render_main import *
from game.current_render import *
import game.current_render as Current_render



def render_main_menu():

    titre = Message(100, 50, 600, 120, 'POKEMON', 'white', 'blue')
    titre.message_render(font_title, screen)
    if new_game_button.render(screen):
        Current_render.set_state(render_new_game)
    if continue_button.render(screen):
        Current_render.set_state(render_combat.render_combat_menu)
    if option_button.render(screen):
        Current_render.set_state(render_main_menu)

    # new_game = Button_rect(200, 250, 400, 80, 'New Game', 'white', 'blue')
    # new_game.collision(font_button_menu, screen)
    # continu = Button_rect(200, 350, 400, 80, 'Continue', 'white', 'blue')
    # continu.collision(font_button_menu, screen)
    # option = Button_rect(200, 450, 400, 80, 'Option', 'white', 'blue')
    # option.collision(font_button_menu, screen)

