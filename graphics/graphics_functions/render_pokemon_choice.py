import pygame
from graphics import *
from graphics.graphics_attributes import *
from graphics.graphics_classes import Image, Rectangle, Message
from graphics.graphics_classes.Button import choice_pokemon_1_button, choice_pokemon_2_button, choice_pokemon_3_button, back_button, valider_button
import graphics.graphics_functions.render_choose_fight as Render_choose_fight   
from graphics.graphics_functions import draw_text
import game.current_render as Current_render



def state_pokemon_choices():
    render_pokemon_choices()


    if choice_pokemon_1_button.render(screen):
        Current_render.set_state(pokemon_1_action)
    if choice_pokemon_2_button.render(screen):
        Current_render.set_state(pokemon_2_action)
    if choice_pokemon_3_button.render(screen):
        Current_render.set_state(pokemon_3_action)


def render_pokemon_choices():
    bcg_choice = Image('./assets/images/pokemon_choose_nb.png', (0,0))
    bcg_choice.draw_image(screen)

    rectangle = Rectangle.draw_rectangle(Rectangle(330, 20, 370, 160))
    draw_text(screen, text_choix, font_ingame, rectangle, 50, 50, max_lines=5)
    # water, fire, grass = render_pokemon_choices_buttons()
    # return water, fire, grass


# def render_pokemon_choices_buttons():    
#     water = choice_pokemon_1_button.render(screen)
#     fire = choice_pokemon_2_button.render(screen)
#     grass = choice_pokemon_3_button.render(screen)
#     return water, fire, grass


def pokemon_1_action():
    screen.fill('black')
    pokemon_1 = Image('./assets/images/caratoji_nb.png', (0, 0))
    pokemon_1.draw_image(screen)
    rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 600, 160))
    pokemon_presentation = (f"Caratoji est un Pokémon aquatique de type eau et combat.Il combine la résilience et de grosses techniques de combat")
    draw_text(screen, pokemon_presentation, font_little, rectangle, 410, 40, max_lines=5)
    if back_button.render(screen):
        Current_render.set_state(state_pokemon_choices)
    if valider_button.render(screen):
        Current_render.set_state(Render_choose_fight.render_choose_fight)


def pokemon_2_action():
    screen.fill('black')
    pokemon_2 = Image('./assets/images/schroumfameche_nb.png', (0, 0))
    pokemon_2.draw_image(screen)
    rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 600, 160))
    pokemon_presentation = (f"Salasmurf est un mélange de feu et de malice. Elle peut enchanter l'adversaire tout en lançant des flammes redoutables.")
    draw_text(screen, pokemon_presentation, font_little, rectangle, 410, 40, max_lines=5)
    if back_button.render(screen):
        Current_render.set_state(state_pokemon_choices)
    if valider_button.render(screen):
        Current_render.set_state(Render_choose_fight.render_choose_fight)


def pokemon_3_action():
    screen.fill('black')
    pokemon_3 = Image('./assets/images/lufizar_nb.png', (0, 0))
    pokemon_3.draw_image(screen)
    rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 600, 160))
    pokemon_presentation = (f"Lufizar est un Pokémon énergique au cœur de pirate. Il utilise son fruit du démon pour libérer des attaques élastiques.")
    draw_text(screen, pokemon_presentation, font_little, rectangle, 410, 40, max_lines=5)
    if back_button.render(screen):
        Current_render.set_state(state_pokemon_choices)
    if valider_button.render(screen):
        Current_render.set_state(Render_choose_fight.render_choose_fight)
