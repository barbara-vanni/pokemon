import pygame
from graphics.graphics_attributes import *
from graphics.graphics_classes.Button_rect import *
from graphics.graphics_classes.Button_image import *
from graphics.graphics_functions.draw_text import *

def render_new_game():
    bcg_new_game = Image('./assets/images/professor_chen_classico.png', (0,0))
    bcg_new_game.draw_image(screen)
    # avatar = Image('./assets/images/sacha.png', (275, 50))
    # avatar.draw_image(screen)

    enter_name = Message(300, 100, 600, 60, 'Who are you ?', 'white', 'white')
    enter_name.message_render(font_long, screen)
    input_button = Button_rect(100, 450, 600, 60, '', 'white', 'blue')
    input_button.collision(font_long, screen)


    valider_button = Button_image('./assets/images/forward.png', (650, 455))
    valider_button.draw_image(screen)
    valider_button.collision()