from graphics.graphics_attributes import *
from graphics.graphics_classes import *

def render_main():
    if get_menu() == 0:
        titre = Message(100, 50, 600, 120, 'POKEMON', 'white', 'blue')
        titre.message_render(font_title, screen)
        new_game = Button_rect(200, 250, 400, 80, 'New Game', 'white', 'blue')
        new_game.collision(font_button_menu, screen)
        continu = Button_rect(200, 350, 400, 80, 'Continue', 'white', 'blue')
        continu.collision(font_button_menu, screen)
        option = Button_rect(200, 450, 400, 80, 'Option', 'white', 'blue')
        option.collision(font_button_menu, screen)
    
        return new_game, continu, option
    return None, None, None