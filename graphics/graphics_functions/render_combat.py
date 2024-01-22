
# from game import *
from event import *
from graphics.graphics_attributes import *
from graphics.graphics_functions import draw_text
from game.games_classes.Combat import *
# import game.games_classes.Combat as Combat
from graphics.graphics_classes import *
from game.games_attributes import combat_begin, pokemon1, pokemon2
# # from game.current_render import *
# import game.current_render as Current_render
import time



def render_combat_menu():
    global message_box, button_suite_press_count, state_fight
    combat = combat_begin
    pokemon1 = combat.get_pokemon1()
    pokemon2 = combat.get_pokemon2()

    screen.fill((255,255,255))
    bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
    bcg_combat.draw_image(screen)
    set_combat(0)
    render_combat_pokemon()
    choice_fight()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if attack_button.render(screen):
                message_box = attack_button_event
            if suite_button.render(screen):
                message_box = suite_button_event
            if valider_button.render(screen):
                state_fight += 1
            if object_button.render(screen):
                pass
            if flee_button.render(screen):
                pass
            if change_poke_button.render(screen):
                pass
        if event.type == pygame.QUIT:
            pygame.quit()
    message_box()
    pygame.display.flip()

#Menu de sélection de combat
def choice_fight():
    border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
    border_option_message.draw_image(screen)
    attack_button.render(screen)
    object_button.render(screen)
    flee_button.render(screen)
    change_poke_button.render(screen)

message_box = choice_fight
state_fight = 0

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
    global num_words, combat_begin
    attack_button.active = False
    object_button.active = False
    flee_button.active = False
    change_poke_button.active = False
    suite_button.render(screen)
    message = Message(30, 430, 740, 140, 'You choose to fight', 'white', 'black')
    message.message_render(font_ingame, screen)

# render pour l'affinité de l'attaque entre les pokemons et la chance de réussite de l'attaque   
def render_next_step_1():      
    rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
    valider_button.render(screen)
    if combat_begin.get_attack_chance_ratio() == 0:
        message = f"L'attaque de {combat_begin.get_pokemon1().get_name()} \n\n à échoué"
    elif combat_begin.get_attack_chance_ratio() == 1:
        message = f"L'attaque de {combat_begin.get_pokemon1().get_name()} \n\n à réussi"
    elif combat_begin.get_attack_chance_ratio() == 2:
        message = f"L'attaque de {combat_begin.get_pokemon1().get_name()} \n\n est un coup critique" 
    draw_text(screen, message, font_ingame, rectangle, 490, 60, max_lines=3)

def render_attack_missed():
    rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
    valider_button.render(screen)
    message = f"C'est au tour de {combat_begin.get_pokemon2().get_name()} \n\n"
    draw_text(screen, message, font_ingame, rectangle, 490, 60, max_lines=3)

# render pour l'efficacité de l'attaque et perte des pv 
def render_next_step_2():
    rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
    valider_button.render(screen)
    if combat_begin.get_affinity_values() < 1:
        efficiency = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque.\n\n C'est ne pas très efficace.")
    elif combat_begin.get_affinity_values() == 1:
        efficiency = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque")
    elif combat_begin.get_affinity_values() > 1 :
        efficiency = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque. \n\n C'est très efficace")
    draw_text(screen, efficiency, font_ingame, rectangle, 490, 60, max_lines=3)

# render pour la mort du pokemon première partie
def render_next_step_3():
    rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
    valider_button.render(screen)
    dead_text = (f"{pokemon2.get_name()} est K.O. {pokemon1.get_name()} à maintenant {pokemon1.get_xp()} / {pokemon1.get_xp_max()} xp")
    draw_text(screen, dead_text, font_long, rectangle, 490, 60, max_lines=3)

# render pour la mort du pokemon deuxième partie
def render_next_step_4():
    rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
    valider_button.render(screen)
    dead_text = (f"{pokemon2.get_name()} est K.O. Félication {pokemon1.get_name()} est passé lvl {pokemon1.get_level()} et son xp est {pokemon1.get_xp()} / {pokemon1.get_xp_max()}")
    draw_text(screen, dead_text, font_long, rectangle, 490, 60, max_lines=3)

def next_step_1():
    global state_fight
    combat_begin.first_hit()
    combat_begin.attack_chance()
    if combat_begin.get_attack_chance_ratio() == 0:
        combat_begin.end_attack()
        return 2
    else:
        return 1

def next_step_2():
    global state_fight
    if combat_begin.get_attack_chance_ratio() == 1 or combat_begin.get_attack_chance_ratio() == 2:
        combat_begin.affinity()
    return 3

def next_step_3():
    global state_fight
    if combat_begin.get_attack_chance_ratio() == 1 or combat_begin.get_attack_chance_ratio() == 2:
        combat_begin.attack()
    return 4

def next_step_4():
    global state_fight
    if combat_begin.get_attack_chance_ratio() == 1 or combat_begin.get_attack_chance_ratio() == 2:
        combat_begin.end_attack()
    return 0

def next_step_5():
    global state_fight
    if combat_begin.end_game() == True:
        return 5
    else:
        return 0

def handle_logic():
    global state_fight
    if state_fight == 0:
        pass
    elif state_fight == 1:
        state_fight = next_step_1()
    elif state_fight == 2:
        state_fight = next_step_1()
    elif state_fight == 3:
        state_fight = next_step_2()
    elif state_fight == 4:
        state_fight = next_step_3()
    elif state_fight == 5:
        state_fight = next_step_4()
    else:
        raise Exception(f"Unknown state {state_fight}")
    return state_fight

def handle_render():
    if state_fight == 0:
        attack_button_event()
    elif state_fight == 1:
        render_next_step_1()
    elif state_fight == 2:
        render_attack_missed()
    elif state_fight == 3:
        render_next_step_2()
    elif state_fight == 4:
        render_next_step_3()
    elif state_fight == 5:
        render_next_step_4()
    else:
        raise Exception(f"Unknown state {state_fight}")
    return state_fight

def suite_button_event():
    global state_fight
    print("Entering suite_button_event")
    for i in range(5):
        handle_logic()
        handle_render()
    if valider_button.render(screen):
        state_fight += 1
    print("Exiting suite_button_event")


