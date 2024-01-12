from graphics.graphics_attributes import *
from graphics.graphics_classes.Button_rect import *
from graphics.graphics_classes.Button_image import *
from graphics.graphics_functions.draw_text import *
from event.mouse_button_event import *

def render_combat():

    screen.fill((255,255,255))
    bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
    bcg_combat.draw_image(screen)

    # Mise en place des informations graphiques pour le pokemon du dresseur 
    pokemon_good = Image('./assets/images/carapuce_2.png', (0, 150))
    pokemon_good.draw_image(screen)
    border_good = Image('./assets/images/border_message.png', (430, 270))
    border_good.draw_image(screen)
    nom_good = Message(410, 280, 300, 50, 'Carapuce lvl 1', 'white', 'black')
    pv_good = Message(540, 325, 200, 30, '100 / 100 pv', 'white', 'black')
    nom_good.message_render(font_ingame, screen)
    pv_good.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white', (450, 360, 280, 10), 0, 15)
    pygame.draw.rect(screen, 'blue', (450, 360, 280, 10), 0, 15)

    # Mise en place des informations graphiques pour le pokemon du vilain
    pokemon_bad = Image('./assets/images/salameche_2.png', (470, -50))
    pokemon_bad.draw_image(screen)
    border_bad = Image('./assets/images/border_message.png', (20, 20))
    border_bad.draw_image(screen)
    nom_bad = Message(10, 30, 300, 50, 'Salameche lvl 1', 'green', 'black')
    pv_bad = Message(128, 75, 200, 30, '100 / 100 pv', 'green', 'black')
    nom_bad.message_render(font_ingame, screen)
    pv_bad.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white',(40, 110, 280, 10), 0, 15)
    pygame.draw.rect(screen, 'blue', (40, 110, 240, 10), 0, 15)

    #Menu de sélection de combat
    # pygame.draw.rect(screen, 'white', (10, 440, 780, 150), 0, 15)
    border_option_message = Image('./assets/images/border_choice_message.png', (30, 420))
    border_option_message.draw_image(screen)
    attack_button = Button_rect(30, 450, 350, 30, "FIGHT !", 'white', 'black')
    attack_button.collision(font_ingame, screen)
    object_button = Button_rect(410, 450, 350, 30, "OBJECT", 'white', 'black')
    object_button.collision(font_ingame, screen)
    flee_button = Button_rect(30, 510, 350, 30, "RUN", 'white', 'black')
    flee_button.collision(font_ingame, screen)
    new_pokemon_button = Button_rect(410, 510, 350, 30, "CHANGE POKEMON", 'white', 'black')
    new_pokemon_button.collision(font_ingame, screen)

    # rectangle = pygame.draw.rect(screen, 'white', (20, 420, 760, 160), 0, 0)
    # draw_text(screen, text_attaque, font_long, rectangle, 440, 60, max_lines=3)
    # suite_button = Button_image('./assets/images/forward.png', (700, 530))
    # suite_button.draw_image(screen)
    # suite_button.collision()

    return pokemon_good, nom_good, pv_good, pokemon_bad, nom_bad, pv_bad, attack_button, object_button, flee_button, new_pokemon_button