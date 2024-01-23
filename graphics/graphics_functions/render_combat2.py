from game import *
from event import *

from graphics.graphics_attributes import *
from graphics.graphics_functions import draw_text
from graphics.graphics_classes.Button import suite_button, attack_button, object_button, flee_button, change_poke_button



continuer = True
attack_button = None


state_fight = 0

def render_combat_pokemon():
    
    # Mise en place des informations graphiques pour le pokemon du dresseur 
    pokemon_good = Image(get_pokemon1().get_image_front(), (0, 130))
    pokemon_good.scale_image((300, 300))
    pokemon_good.draw_image(screen)
    border_good = Image('./assets/images/border_message.png', (430, 270))
    border_good.draw_image(screen)
    nom_good = Message(410, 280, 300, 50, f'{get_pokemon1().get_name()} lvl {get_pokemon1().get_level()}', 'white', 'black')
    pv_good = Message(540, 325, 200, 30, f'{get_pokemon1().get_pv()} / {get_pokemon1().get_pv_max()} pv', 'white', 'black')
    nom_good.message_render(font_ingame, screen)
    pv_good.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white', (450, 360, 280, 10), 0, 15)
    pygame.draw.rect(screen, 'blue', (450, 360, get_pokemon1().get_pv() * 280 / get_pokemon1().get_pv_max(), 10), 0, 15)

    # Mise en place des informations graphiques pour le pokemon du vilain
    pokemon_bad = Image(get_pokemon2().get_image_front(), (440, 0))
    pokemon_bad.scale_image((300, 300))
    pokemon_bad.draw_image(screen)
    border_bad = Image('./assets/images/border_message.png', (20, 20))
    border_bad.draw_image(screen)
    nom_bad = Message(10, 30, 300, 50, f'{get_pokemon2().get_name()} lvl {get_pokemon2().get_level()}', 'green', 'black')
    pv_bad = Message(128, 75, 200, 30, f'{get_pokemon2().get_pv()} / {get_pokemon2().get_pv_max()} pv', 'green', 'black')
    nom_bad.message_render(font_ingame, screen)
    pv_bad.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white',(40, 110, 280, 10), 0, 15)
    pygame.draw.rect(screen, 'blue', (40, 110, get_pokemon2().get_pv() * 280 / get_pokemon2().get_pv_max(), 10), 0, 15)
    # print(get_pokemon2().get_name(), end='\r')

    #Menu de sélection de combat
    if get_combat() == 0:
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        attack_button = Button_rect(30, 450, 350, 30, "FIGHT !", 'white', 'black')
        attack_button.collision(font_ingame, screen)
        object_button = Button_rect(410, 450, 350, 30, "OBJECT", 'white', 'black')
        object_button.collision(font_ingame, screen)
        flee_button = Button_rect(30, 510, 350, 30, "RUN", 'white', 'black')
        flee_button.collision(font_ingame, screen)
        new_pokemon_button = Button_rect(410, 510, 350, 30, "CHANGE POKEMON", 'white', 'black')
        new_pokemon_button.collision(font_ingame, screen)
        return attack_button, object_button, flee_button, new_pokemon_button
    
    elif get_combat() == 1:
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if combat_begin.get_attack_chance_ratio() == 0:
            attack_missed = (f"L'attaque de {combat_begin.get_pokemon1().get_name()} à échoué")
            draw_text(screen, attack_missed, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_attack_chance_ratio() == 1:
            attack_normal = (f"L'attaque de {combat_begin.get_pokemon1().get_name()} à réussi")
            draw_text(screen, attack_normal, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_attack_chance_ratio() == 2:
            attack_critical = (f"L'attaque de {combat_begin.get_pokemon1().get_name()} est un coup critique")
            draw_text(screen, attack_critical, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.render(screen)
        return suite_button
    
    elif get_combat() == 2:
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if combat_begin.get_affinity_values() < 1:
            efficiency_none = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque. C'est ne pas très efficace.")
            draw_text(screen, efficiency_none, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_affinity_values() == 1:
            efficiency = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque")
            draw_text(screen, efficiency, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_affinity_values() > 1 :
            efficiency_top = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque, C'est très efficace")
            draw_text(screen, efficiency_top, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.render(screen)
        return suite_button
    
    elif get_combat() == 3:    
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{pokemon2.get_name()} est K.O. {pokemon1.get_name()} à maintenant {pokemon1.get_xp()} / {pokemon1.get_xp_max()} xp")
        draw_text(screen, dead_text, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.render(screen)
        return suite_button
    
    elif get_combat() == 4:   
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{pokemon2.get_name()} est K.O. Félication {pokemon1.get_name()} est passé lvl {pokemon1.get_level()} et son xp est {pokemon1.get_xp()} / {pokemon1.get_xp_max()}")
        draw_text(screen, dead_text, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.render(screen)
        return suite_button

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

message_box = choice_fight

turn_number = 0

def suite_button_event(event):
    global turn_number
    if event.type == pygame.MOUSEBUTTONDOWN:
        if suite_button is not None and suite_button.check_clicked():
            if get_combat()== 0:
                set_combat(1)
                combat_begin.first_hit()
                combat_begin.attack_chance()
        if get_combat() == 1:
            if suite_button.check_clicked():
                if combat_begin.get_attack_chance_ratio() == 0:
                    if combat_begin.get_pokemon1() == combat_begin.get_pokemon_player():
                        combat_begin.end_attack()
                        set_combat(1)
                        suite_button.render(screen)
                    else:
                        combat_begin.end_attack()
                        set_combat(0)
                        suite_button.render(screen)
                else:
                    set_combat(2)
                    combat_begin.attack_chance()
                    combat_begin.attack()
                    suite_button.render(screen)

        suite_button.check_clicked()
        if get_combat() == 2:
            if suite_button.check_clicked() == True:
                mort = combat_begin.end_game()
                if mort == True:
                    level_up = combat_begin.gain_xp()
                    if level_up == True:
                        pokedex.change_statistics(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_xp(), combat_begin.get_pokemon1().get_xp_max(), trainer.get_name_trainer())
                        pokedex.change_stat_pv(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_pv(), trainer.get_name_trainer())
                        set_combat(4)
                        suite_button.render(screen)
                    else:
                        pokedex.change_stat_pv(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_pv(), trainer.get_name_trainer())
                        pokedex.change_stat_xp(combat_begin.get_pokemon1().get_name(), trainer.get_name_trainer())
                        set_combat(3)
                        suite_button.render(screen)
                else:
                    if turn_number == 1:
                        combat_begin.end_attack()
                        set_combat(0)
                        turn_number = 0
                    else:
                        turn_number += 1
                        combat_begin.end_attack()
                        set_combat(1)
                        suite_button.render(screen)

        suite_button.check_clicked()
        if get_combat() == 3 or get_combat() == 4:
            if suite_button.check_clicked() == True:
                # old_pv = combat_begin.get_pokemon1().get_pv()
                set_pokemon1(pokedex.choose_specific_pokemon("Mewtwo"))
                # combat_begin.get_pokemon1().set_pv(old_pv)
                set_pokemon2(pokedex.choose_random_pokemon())
                set_combat(0)
  
def attack_button_event(event, button_object):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_object is not None and button_object.check_clicked():
            if get_combat()== 0:
                set_combat(1)
                combat_begin.first_hit()
                combat_begin.attack_chance()

def mouse_button_event(event, button_object):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_object.render(screen) == True:
            set_menu(1)

def quit_event(event, continuer):
    if event.type == pygame.QUIT:
        return False
    return continuer


def render_combat():
    global message_box, continuer, attack_button, object_button, flee_button, change_poke_button, combat_begin
    screen.fill((255,255,255))
    bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
    bcg_combat.draw_image(screen)
    set_combat(0)
    render_combat_pokemon()
    # choice_fight()

    if get_menu() == 1:
        if get_combat() == 0:
            attack_button = render_combat(get_pokemon1(), get_pokemon2())
        elif get_combat() == 1 or get_combat() == 2 or get_combat() == 3 or get_combat() == 4:
            suite_button = render_combat(get_pokemon1(), get_pokemon2())

    for event in pygame.event.get():
        # continuer = quit_event(event, continuer)
        # mouse_button_event(event, continuer)
        if get_menu() == 1:
            if get_combat() == 0:
                attack_button_event(event, attack_button)
            elif get_combat() == 1 or get_combat() == 2 or get_combat() == 3 or get_combat() == 4:
                suite_button_event(event, suite_button)


    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if attack_button.render(screen):
    #         #     message_box = attack_button_event
    #         # if suite_button.render(screen):
    #             message_box = render_combat_pokemon
    #         if object_button.render(screen):
    #             pass
    #         if flee_button.render(screen):
    #             pass
    #         if change_poke_button.render(screen):
    #             pass
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #     message_box()
        pygame.display.flip()

