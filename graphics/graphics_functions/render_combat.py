from game import *
from graphics.graphics_attributes import *
from graphics.graphics_functions import draw_text, render_choose_fight
from graphics.graphics_classes import *
from game.games_attributes import *
from game.games_classes.Combat import Combat
import game.current_render as Current_render

turn_number = 0


def render_combat_pokemon():
    global turn_number

    # suite_button.clicked = False
    screen.fill((255,255,255))
    bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
    bcg_combat.draw_image(screen)

    # for pokeball_number in range(1, 6):
    #     if get_state_combat() == pokeball_number:
    #         pokeball = Image(f'./assets/images/pokeball{pokeball_number}.png', (pokeball_number * 60, 0))
    #     pokeball.draw_image(screen)

    pokeball = None  # Initialisez la variable en dehors de la boucle

    for pokeball_number in range(1, 6):
        if get_state_combat() == pokeball_number:
            pokeball = Image(f'./assets/images/pokeball{pokeball_number}.png', (pokeball_number * 60, 0))

    if pokeball is not None:
        pokeball.draw_image(screen)

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


    #Menu de sélection de combat
    if get_combat() == 0:
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        # attack_button.draw(screen)
        object_button = Button_rect(410, 450, 350, 30, "OBJECT", 'white', 'black')
        object_button.collision(font_ingame, screen)
        flee_button = Button_rect(30, 510, 350, 30, "RUN", 'white', 'black')
        flee_button.collision(font_ingame, screen)
        new_pokemon_button = Button_rect(410, 510, 350, 30, "CHANGE POKEMON", 'white', 'black')
        new_pokemon_button.collision(font_ingame, screen)
        if attack_button.render(screen):
            set_combat(1)
            Combat.combat_begin.first_hit()
            Combat.combat_begin.attack_chance()
    
    elif get_combat() == 1:
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if Combat.combat_begin.get_attack_chance_ratio() == 0:
            attack_missed = (f"L'attaque de {Combat.combat_begin.get_pokemon1().get_name()} à échoué")
            draw_text(screen, attack_missed, font_ingame, rectangle, 490, 60, max_lines=3)
        elif Combat.combat_begin.get_attack_chance_ratio() == 1:
            attack_normal = (f"L'attaque de {Combat.combat_begin.get_pokemon1().get_name()} à réussi")
            draw_text(screen, attack_normal, font_ingame, rectangle, 490, 60, max_lines=3)
        elif Combat.combat_begin.get_attack_chance_ratio() == 2:
            attack_critical = (f"L'attaque de {Combat.combat_begin.get_pokemon1().get_name()} est un coup critique")
            draw_text(screen, attack_critical, font_ingame, rectangle, 490, 60, max_lines=3)
        if suite_button.render(screen):
            print("coucou")
            if Combat.combat_begin.get_attack_chance_ratio() == 0:
                if turn_number == 1:
                    Combat.combat_begin.end_attack()
                    set_combat(0)
                    turn_number = 0
                else:
                    turn_number += 1
                    Combat.combat_begin.attack_chance()
                    Combat.combat_begin.end_attack()
                    # set_combat(1)
            else:
                set_combat(2)
                # Combat.combat_begin.attack_chance()
                Combat.combat_begin.attack()
    
    elif get_combat() == 2:
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if Combat.combat_begin.get_affinity_values() < 1:
            efficiency_none = (f"{Combat.combat_begin.get_pokemon1().get_name()} lance une attaque. C'est ne pas très efficace.")
            draw_text(screen, efficiency_none, font_ingame, rectangle, 490, 60, max_lines=3)
        elif Combat.combat_begin.get_affinity_values() == 1:
            efficiency = (f"{Combat.combat_begin.get_pokemon1().get_name()} lance une attaque")
            draw_text(screen, efficiency, font_ingame, rectangle, 490, 60, max_lines=3)
        elif Combat.combat_begin.get_affinity_values() > 1 :
            efficiency_top = (f"{Combat.combat_begin.get_pokemon1().get_name()} lance une attaque, C'est très efficace")
            draw_text(screen, efficiency_top, font_ingame, rectangle, 490, 60, max_lines=3)

        if suite_button.render(screen):
            print("coucou2")
            if Combat.combat_begin.end_game() == True:
                if Combat.combat_begin.gain_xp() == True:
                    pokedex.change_statistics(Combat.combat_begin.get_pokemon1().get_name(), Combat.combat_begin.get_pokemon1().get_xp(), Combat.combat_begin.get_pokemon1().get_xp_max(), 'save')
                    pokedex.change_stat_pv(Combat.combat_begin.get_pokemon1().get_name(), Combat.combat_begin.get_pokemon1().get_pv(), 'save')
                    set_combat(4)
                else:
                    pokedex.change_stat_pv(Combat.combat_begin.get_pokemon1().get_name(), Combat.combat_begin.get_pokemon1().get_pv(), 'save')
                    pokedex.change_stat_xp(Combat.combat_begin.get_pokemon1().get_name(), 'save')
                    set_combat(3)
            else:
                if turn_number == 1:
                    Combat.combat_begin.end_attack()
                    set_combat(0)
                    turn_number = 0
                else:
                    turn_number += 1
                    Combat.combat_begin.end_attack()
                    set_combat(1)
    
    elif get_combat() == 3:    
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{get_pokemon2().get_name()} est K.O. {get_pokemon1().get_name()} à maintenant {pokemon1.get_xp()} / {pokemon1.get_xp_max()} xp")
        draw_text(screen, dead_text, font_ingame, rectangle, 490, 60, max_lines=3)
        if suite_button.render(screen):  
            if get_state_combat() == 1:
                Current_render.set_state(render_choose_fight.render_choose_fight)
            else:
                set_pokemon1(pokedex.choose_specific_pokemon("Mewtwo"))
                set_pokemon2(pokedex.choose_random_pokemon())
                Combat.combat_begin.set_pokemon2(get_pokemon2())
                set_combat(0)

    
    elif get_combat() == 4:   
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{get_pokemon2().get_name()} est K.O. Félication {get_pokemon1().get_name()} est passé lvl {pokemon1.get_level()} et son xp est {pokemon1.get_xp()} / {pokemon1.get_xp_max()}")
        draw_text(screen, dead_text, font_ingame, rectangle, 490, 60, max_lines=3)
        if suite_button.render(screen):  
            if get_state_combat() == 1:
                Current_render.set_state(render_choose_fight.render_choose_fight)
            else:
                set_pokemon1(pokedex.choose_specific_pokemon("Mewtwo"))
                set_pokemon2(pokedex.choose_random_pokemon())
                Combat.combat_begin.set_pokemon2(get_pokemon2())
                set_combat(0)

    
    

    
