from game import *
from event import *
from graphics.graphics_attributes import *
from graphics.graphics_functions import *
from game.games_attributes import *

turn_number = 0

def render_combat_pokemon():
    global turn_number
    screen.fill((255,255,255))
    bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
    bcg_combat.draw_image(screen)
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

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if attack_button is not None and attack_button.get_clicked():
                    if get_combat()== 0:
                        set_combat(1)
                        combat_begin.first_hit()
                        combat_begin.attack_chance()

    
    elif get_combat() == 1:
        rectangle = Rectangle.draw_rectangle(Rectangle(30, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if combat_begin.get_attack_chance_ratio() == 0:
            attack_missed = (f"L'attaque de {combat_begin.get_pokemon1().get_name()} à échoué")
            draw_text(screen, attack_missed, font_ingame, rectangle, 490, 60, max_lines=3)
        elif combat_begin.get_attack_chance_ratio() == 1:
            attack_normal = (f"L'attaque de {combat_begin.get_pokemon1().get_name()} à réussi")
            draw_text(screen, attack_normal, font_ingame, rectangle, 490, 60, max_lines=3)
        elif combat_begin.get_attack_chance_ratio() == 2:
            attack_critical = (f"L'attaque de {combat_begin.get_pokemon1().get_name()} est \n un coup critique")
            draw_text(screen, attack_critical, font_ingame, rectangle, 490, 60, max_lines=3)
        image = pygame.image.load('./assets/images/forward.png')
        suite_button = Button_image(680, 485, image, 1) 
        suite_button.draw(screen)
    
    elif get_combat() == 2:
        rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if combat_begin.get_affinity_values() < 1:
            efficiency_none = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque.\n\n   C'est ne pas très efficace.")
            draw_text(screen, efficiency_none, font_ingame, rectangle, 490, 60, max_lines=3)
        elif combat_begin.get_affinity_values() == 1:
            efficiency = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque")
            draw_text(screen, efficiency, font_ingame, rectangle, 490, 60, max_lines=3)
        elif combat_begin.get_affinity_values() > 1 :
            efficiency_top = (f"{combat_begin.get_pokemon1().get_name()} lance une attaque. \n\n   C'est très efficace")
            draw_text(screen, efficiency_top, font_ingame, rectangle, 490, 60, max_lines=3)
        image = pygame.image.load('./assets/images/forward.png')
        suite_button = Button_image(680, 485, image, 1)
        suite_button.draw(screen)
    
    elif get_combat() == 3:    
        rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{pokemon2.get_name()} est K.O. {pokemon1.get_name()} à maintenant {pokemon1.get_xp()} / {pokemon1.get_xp_max()} xp")
        draw_text(screen, dead_text, font_ingame, rectangle, 490, 60, max_lines=3)
        image = pygame.image.load('./assets/images/forward.png')
        suite_button = Button_image(680, 485, image, 1)
        suite_button.draw(screen)
    
    elif get_combat() == 4:   
        rectangle = Rectangle.draw_rectangle(Rectangle(30, 430, 740, 140))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{pokemon2.get_name()} est K.O. Félication {pokemon1.get_name()} est passé lvl {pokemon1.get_level()} et son xp est {pokemon1.get_xp()} / {pokemon1.get_xp_max()}")
        draw_text(screen, dead_text, font_ingame, rectangle, 490, 60, max_lines=3)
        image = pygame.image.load('./assets/images/forward.png')
        suite_button = Button_image(680, 485, image, 1)
        suite_button.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if get_combat() == 1:
                if suite_button.draw(screen):
                    if combat_begin.get_attack_chance_ratio() == 0:
                        if combat_begin.get_pokemon1() == combat_begin.get_pokemon_player():
                            combat_begin.end_attack()
                            set_combat(1)
                        else:
                            combat_begin.end_attack()
                            set_combat(0)
                    else:
                        set_combat(2)
                        combat_begin.attack_chance()
                        combat_begin.attack()

            if get_combat() == 2:
                if suite_button.draw(screen) == True:
                    mort = combat_begin.end_game()
                    if mort == True:
                        level_up = combat_begin.gain_xp()
                        if level_up == True:
                            pokedex.change_statistics(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_xp(), combat_begin.get_pokemon1().get_xp_max())
                            pokedex.change_stat_pv(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_pv())
                            set_combat(4)
                        else:
                            pokedex.change_stat_pv(combat_begin.get_pokemon1().get_name(), combat_begin.get_pokemon1().get_pv())
                            pokedex.change_stat_xp(combat_begin.get_pokemon1().get_name())
                            set_combat(3)
                    else:
                        if turn_number == 1:
                            combat_begin.end_attack()
                            set_combat(0)
                            turn_number = 0
                        else:
                            turn_number += 1
                            combat_begin.end_attack()
                            set_combat(1)

            if get_combat() == 3 or get_combat() == 4:
                if suite_button.draw(screen) == True:
                    # old_pv = combat_begin.get_pokemon1().get_pv()
                    set_pokemon1(pokedex.choose_specific_pokemon("Mewtwo"))
                    # combat_begin.get_pokemon1().set_pv(old_pv)
                    set_pokemon2(pokedex.choose_random_pokemon())
                    set_combat(0)