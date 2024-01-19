
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
#Menu de sélection de combat
def choice_fight():
    border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
    border_option_message.draw_image(screen)
    attack_button.render(screen)
    object_button.render(screen)
    flee_button.render(screen)
    change_poke_button.render(screen)

def suite_button_event():
    global combat_begin
    rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
    valider_button.render(screen)
    suite_button_event_2()
    text = combat_begin.get_render_message()
    draw_text(screen, text, font_long, rectangle, 490, 60, max_lines=3)

count_combat = 0
   
def suite_button_event_2():
    global count_combat, combat_begin, pokemon1, pokemon2
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if count_combat() == 1:
                combat_begin.first_hit()
                if valider_button.render(screen):
                    if combat_begin.get_attack_chance_ratio() == 0:
                        if combat_begin.get_pokemon1() == combat_begin.get_pokemon_player():
                            
                            combat_begin.end_attack()
                            count_combat = 1
                            valider_button.render(screen)

                        else:
                            combat_begin.end_attack()
                            count_combat = 0
                            valider_button.render(screen)

                    else:
                        count_combat = 2
                        combat_begin.attack_chance()
                        combat_begin.attack()
                        valider_button.render(screen)

            valider_button.render(screen)
            if count_combat() == 2:
                if valider_button.active == True:
                    print('hihi')
                    mort = combat_begin.end_game()
                    if mort == True:
                        level_up = combat_begin.gain_xp()
                        if level_up == True:
                            count_combat = 4
                            valider_button.render(screen)

                        else:
                            count_combat = 3 
                            valider_button.render(screen)

                    else:
                        if combat_begin.get_pokemon1() != combat_begin.get_pokemon_player():
                            combat_begin.end_attack()
                            count_combat= 0
                        else:
                            combat_begin.end_attack()
                            count_combat = 1
                            valider_button.render(screen)


            valider_button.render(screen)
            if count_combat == 3 or count_combat == 4:
                if valider_button.active == True:
                    print('hihihi')
                    pokemon1.set_pv(pokemon1.get_pv_max())
                    pokemon2.set_pv(pokemon2.get_pv_max())
                    count_combat = 0


message_box = choice_fight
# button_suite_press_count = 0
# state_fight = 0