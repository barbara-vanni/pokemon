from graphics.graphics_attributes import *
from graphics.graphics_classes.Button_rect import *
from graphics.graphics_classes.Button_image import *
from graphics.graphics_functions.draw_text import *

state = 'pokemon_choices'

def state_pokemon_choices():
    global num_words
    num_words = 1
    water, fire, grass = render_pokemon_choices()
    return water, fire, grass

def render_pokemon_choices():
    bcg_choice = Image('./assets/images/pokemon_choose.png', (0,0))
    bcg_choice.draw_image(screen)

    rectangle = Rectangle.draw_rectangle(Rectangle(330, 20, 370, 160))
    draw_text(screen, text_choix, font_ingame, rectangle, 50, 50, max_lines=5)
    # carapuce = Image('./assets/images/carapuce_2.png', (-30, 250))
    # carapuce.draw_image(screen)
    # salameche = Image('./assets/images/salameche_2.png', (250, 250))
    # salameche.draw_image(screen)
    # carapuce = Image('./assets/images/bulbizarre_2.png', (530, 250))
    # carapuce.draw_image(screen)
    water, fire, grass = render_pokemon_choices_buttons()
    # render_pokemon_choices_buttons_image()
    return water, fire, grass


def render_pokemon_choices_buttons():    
    pokemon_1 = Button_rect(20, 300, 200, 50, 'Type Eau', 'black', 'white')
    pokemon_1.collision(font_long, screen)
    pokemon_2 = Button_rect(300, 300, 200, 50, 'Type Feu', 'black', 'white')
    pokemon_2.collision(font_long, screen)
    pokemon_3 = Button_rect(580, 300, 200, 50, 'Type Plante', 'black', 'white')
    pokemon_3.collision(font_long, screen)
    if pokemon_1.get_clicked():
        pokemon_1_action()
    if pokemon_2.get_clicked():
        pokemon_2_action()
    if pokemon_3.get_clicked():
        pokemon_3_action()
    return pokemon_1, pokemon_2, pokemon_3



def pokemon_1_action():
    screen.fill('black')
    pokemon_1 = Image('./assets/images/caratoji.png', (0, 0))
    pokemon_1.draw_image(screen)

def pokemon_2_action():
    screen.fill('black')
    pokemon_2 = Image('./assets/images/salamoji.png', (0, 0))
    pokemon_2.draw_image(screen)

def pokemon_3_action():
    screen.fill('black')
    pokemon_3 = Image('./assets/images/lufizar.png', (0, 0))
    pokemon_3.draw_image(screen)


    