
# from game import *
from event import *
from graphics.graphics_attributes import *
from graphics.graphics_functions import draw_text
from game.games_classes.Combat import *
from graphics.graphics_classes import *
from game.games_attributes import *
# # from game.current_render import *
# import game.current_render as Current_render


def render_combat_menu():
    combat = combat_begin
    pokemon1 = combat.get_pokemon1()
    pokemon2 = combat.get_pokemon2()

    screen.fill((255,255,255))
    bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
    bcg_combat.draw_image(screen)
    render_combat_pokemon()

    render_message_fight = choice_fight()

    if render_message_fight == "attack":
        render_message_fight = attack_button_event()
    elif render_message_fight == "object":
        pass
    elif render_message_fight == "flee":
        pass
    elif render_message_fight == "change_pokemon":
        pass



def render_combat_pokemon():
    
    # Mise en place des informations graphiques pour le pokemon du dresseur 
    pokemon_good = Image('./assets/images/carapuce_2.png', (0, 130))
    pokemon_good.draw_image(screen)
    border_good = Image('./assets/images/border_message.png', (430, 270))
    border_good.draw_image(screen)
    nom_good = Message(410, 280, 300, 50, f'{pokemon1.get_name()} lvl {pokemon1.get_level()}', 'white', 'black')
    pv_good = Message(540, 325, 200, 30, f'{pokemon1.get_pv()} / {pokemon1.get_pv_max()} pv', 'white', 'black')
    nom_good.message_render(font_ingame, screen)
    pv_good.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white', (450, 360, 280, 10), 0, 15)
    pygame.draw.rect(screen, 'blue', (450, 360, pokemon1.get_pv() * 280 / pokemon1.get_pv_max(), 10), 0, 15)

    # Mise en place des informations graphiques pour le pokemon du vilain
    pokemon_bad = Image('./assets/images/salameche_2.png', (440, -60))
    pokemon_bad.draw_image(screen)
    border_bad = Image('./assets/images/border_message.png', (20, 20))
    border_bad.draw_image(screen)
    nom_bad = Message(10, 30, 300, 50, f'{pokemon2.get_name()} lvl {pokemon2.get_level()}', 'green', 'black')
    pv_bad = Message(128, 75, 200, 30, f'{pokemon2.get_pv()} / {pokemon2.get_pv_max()} pv', 'green', 'black')
    nom_bad.message_render(font_ingame, screen)
    pv_bad.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white',(40, 110, 280, 10), 0, 15)
    pygame.draw.rect(screen, 'blue', (40, 110, pokemon2.get_pv() * 280 / pokemon2.get_pv_max(), 10), 0, 15)

def attack_button_event():
    rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
    border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
    border_option_message.draw_image(screen)
    draw_text(screen, combat_begin.get_render_message(), font_long, rectangle, 440, 60, max_lines=3)
    # draw_text(screen, "salut ça va, ça marche", font_long, rectangle, 440, 60, max_lines=3)
    suite_button = Button_image('./assets/images/forward.png', (700, 530))
    suite_button.draw_image(screen)
    suite_button.collision()

#Menu de sélection de combat
def choice_fight():
    border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
    border_option_message.draw_image(screen)
    attack_button.render(screen)
    object_button.render(screen)
    flee_button.render(screen)
    change_poke_button.render(screen)
    combat_begin.first_hit()
    combat_begin.attack_chance()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if attack_button.render(screen):
                return "attack"
            elif object_button.render(screen):
                return "object"
            elif flee_button.render(screen):
                return "flee"
            elif change_poke_button.render(screen):
                return "change_pokemon"
    
    return None






