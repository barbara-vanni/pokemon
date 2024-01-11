from graphics.graphics_attributes import *
# from graphics.graphics_classes.Image import *
from graphics.graphics_classes.Button_rect import *
from graphics.graphics_classes.Button_image import *

def render_combat():
    screen.fill((150,150,150))
    bcg_combat = Image('./assets/images/bcg_combat.png', (0,0))
    bcg_combat.draw_image(screen)

    # Mise en place des informations graphiques pour le pokemon du dresseur 
    pokemon_good = Image('./assets/images/carapuce.png', (0, 150))
    pokemon_good.draw_image(screen)
    nom_good = Message(450, 275, 300, 40, 'carapuce lvl 1', 'green', 'black')
    pv_good = Message(450, 325, 300, 40, '100 / 100 pv', 'green', 'black')
    nom_good.message_render(font_ingame, screen)
    pv_good.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white', (450, 375, 300, 20), 0, 15)
    pygame.draw.rect(screen, 'blue', (450, 375, 300, 20), 0, 15)

    # Mise en place des informations graphiques pour le pokemon du vilain
    pokemon_bad = Image('./assets/images/salameche.png', (500, 0))
    pokemon_bad.draw_image(screen)
    nom_bad = Message(50, 30, 300, 40, 'salameche lvl 1', 'green', 'black')
    pv_bad = Message(50, 80, 300, 40, '100 / 100 pv', 'green', 'black')
    nom_bad.message_render(font_ingame, screen)
    pv_bad.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white',(50, 130, 300, 20), 0, 15)
    pygame.draw.rect(screen, 'blue', (50, 130, 300, 20), 0, 15)

    #Menu de sélection de combat
    pygame.draw.rect(screen, 'white', (10, 410, 780, 180), 0, 15)
    attack_button = Button_rect(20, 430, 350, 40, "A l'attaque !", 'grey', 'black')
    attack_button.collision(font_ingame, screen)
    object_button = Button_rect(430, 430, 350, 40, "Objet", 'grey', 'black')
    object_button.collision(font_ingame, screen)
    flee_button = Button_rect(20, 530, 350, 40, "Fuir", 'grey', 'black')
    flee_button.collision(font_ingame, screen)
    new_pokemon_button = Button_rect(430, 530, 350, 40, "Changer de pokemon", 'grey', 'black')
    new_pokemon_button.collision(font_ingame, screen)

    attack_message_1 = Message(20, 420, 760, 60, "Le pokémone (nom de pokemon) lance l'attaque",'grey', 'black')
    attack_message_2 = Message(20, 480, 760, 60, "(nom de l'attaque)",'grey', 'black')
    attack_message_3 = Message(20, 540, 760, 40, "C'est (efficacité) efficace",'grey', 'black')
    attack_message_1.message_render(font_ingame, screen)
    attack_message_2.message_render(font_ingame, screen)
    attack_message_3.message_render(font_ingame, screen)
    suite_button = Button_image('./assets/images/forward.png', (700, 530))
    suite_button.draw_image(screen)