import pygame
from graphics import *
from graphics.graphics_attributes import *
from game.current_render import *
import game.current_render as Current_render
from graphics.graphics_functions import draw_text

state = 'pokemon_choices'

def state_pokemon_choices():
    global num_words
    num_words = 1
    water, fire, grass = render_pokemon_choices()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if choice_pokemon_1_button.render(screen):
                Current_render.set_state(pokemon_1_action)
            if choice_pokemon_2_button.render(screen):
                Current_render.set_state(pokemon_2_action)
            if choice_pokemon_3_button.render(screen):
                Current_render.set_state(pokemon_3_action)
                

    return water, fire, grass

def render_pokemon_choices():
    bcg_choice = Image('./assets/images/pokemon_choose.png', (0,0))
    bcg_choice.draw_image(screen)

    rectangle = Rectangle.draw_rectangle(Rectangle(330, 20, 370, 160))
    draw_text(screen, text_choix, font_ingame, rectangle, 50, 50, max_lines=5)
    water, fire, grass = render_pokemon_choices_buttons()


    return water, fire, grass


def render_pokemon_choices_buttons():    
    water = choice_pokemon_1_button.render(screen)
    fire = choice_pokemon_2_button.render(screen)
    grass = choice_pokemon_3_button.render(screen)
    return water, fire, grass



def pokemon_1_action():
    screen.fill('black')
    pokemon_1 = Image('./assets/images/caratoji.png', (0, 0))
    pokemon_1.draw_image(screen)
    if back_button.render(screen):
        Current_render.set_state(state_pokemon_choices)

def pokemon_2_action():
    screen.fill('black')
    pokemon_2 = Image('./assets/images/schroumameche.png', (0, 0))
    pokemon_2.draw_image(screen)
    if back_button.render(screen):
        Current_render.set_state(state_pokemon_choices)

def pokemon_3_action():
    screen.fill('black')
    pokemon_3 = Image('./assets/images/lufizar.png', (0, 0))
    pokemon_3.draw_image(screen)
    if back_button.render(screen):
        Current_render.set_state(state_pokemon_choices)