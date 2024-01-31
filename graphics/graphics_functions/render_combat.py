from game import *
from graphics.graphics_attributes import *
from graphics.graphics_functions import draw_text, render_choose_fight
from graphics.graphics_classes import *
from game.games_attributes import *
from game.games_classes.Combat import Combat
import game.current_render as Current_render

turn_number = 0
catch_chance = 0

def render_combat_pokemon():
    global turn_number

    # suite_button.clicked = False
    screen.fill((255,255,255))
    bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
    bcg_combat.draw_image(screen)

    # Mise en place des informations graphiques pour le pokemon du dresseur
    # Combat.combat_begin.set_pokemon1(get_pokemon1())
    pokemon_good = Image(f'assets/images/pokemon_back/{(get_pokemon1().get_name()).lower()}.png', (70, 250))
    pokemon_good.scale_image((200, 200))
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
    pokedex2.change_statut(get_pokemon2().get_name(), trainer.get_name_trainer())

    #Menu de sélection de combat
    if get_combat() == 0:
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if attack_button.render(screen):
            set_combat(1)
            Combat.combat_begin.first_hit()
            Combat.combat_begin.attack_chance()
        elif flee_button.render(screen):
            Current_render.set_state(render_choose_fight.render_choose_fight)
            Combat.combat_begin.set_pokemon2(pokedex2.choose_random_pokemon())
            set_pokemon2(Combat.combat_begin.get_pokemon2())
        elif change_poke_button.render(screen):
            set_combat(7)
        elif object_button.render(screen):
            set_combat(8)
    
    elif get_combat() == 1:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if Combat.combat_begin.get_attack_chance_ratio() == 0:
            attack_missed = (f"L'attaque de {Combat.combat_begin.get_pokemon1().get_name()} à échoué")
            draw_text(screen, attack_missed, font_ingame, rectangle, 460, 60, max_lines=3)
        elif Combat.combat_begin.get_attack_chance_ratio() == 1:
            attack_normal = (f"L'attaque de {Combat.combat_begin.get_pokemon1().get_name()} à réussi")
            draw_text(screen, attack_normal, font_ingame, rectangle, 460, 60, max_lines=3)
        elif Combat.combat_begin.get_attack_chance_ratio() == 2:
            attack_critical = (f"L'attaque de {Combat.combat_begin.get_pokemon1().get_name()} est un coup critique")
            draw_text(screen, attack_critical, font_ingame, rectangle, 460, 60, max_lines=3)
        if suite_button.render(screen):
            if Combat.combat_begin.get_attack_chance_ratio() == 0:
                if turn_number == 1:
                    Combat.combat_begin.end_attack()
                    # Combat.combat_begin.set_pokemon1(get_pokemon1())
                    # Combat.combat_begin.set_pokemon2(get_pokemon2())
                    set_combat(0)
                    turn_number = 0
                else:
                    turn_number += 1
                    Combat.combat_begin.attack_chance()
                    Combat.combat_begin.end_attack()
            else:
                set_combat(2)
                Combat.combat_begin.attack()
    
    elif get_combat() == 2:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if Combat.combat_begin.get_affinity_values() < 1:
            efficiency_none = (f"{Combat.combat_begin.get_pokemon1().get_name()} lance une attaque. Ce n'est pas très efficace.")
            draw_text(screen, efficiency_none, font_ingame, rectangle, 460, 60, max_lines=3)
        elif Combat.combat_begin.get_affinity_values() == 1:
            efficiency = (f"{Combat.combat_begin.get_pokemon1().get_name()} lance une attaque. C'est moyennement efficace")
            draw_text(screen, efficiency, font_ingame, rectangle, 460, 60, max_lines=3)
        elif Combat.combat_begin.get_affinity_values() > 1 :
            efficiency_top = (f"{Combat.combat_begin.get_pokemon1().get_name()} lance une attaque. C'est très efficace")
            draw_text(screen, efficiency_top, font_ingame, rectangle, 460, 60, max_lines=3)

        if suite_button.render(screen):
            if Combat.combat_begin.end_game() == True:
                print(Combat.combat_begin.get_pokemon2().get_name(), Combat.combat_begin.get_pokemon_player())
                if Combat.combat_begin.gain_xp() == True:
                    pokedex2.change_statistics(Combat.combat_begin.get_pokemon1().get_name(), Combat.combat_begin.get_pokemon1().get_xp(), trainer.get_name_trainer())
                    pokedex2.change_stat_pv(Combat.combat_begin.get_pokemon1().get_name(), Combat.combat_begin.get_pokemon1().get_pv(), trainer.get_name_trainer())
                    evolution = pokedex2.evolution(Combat.combat_begin.get_pokemon1(), trainer.get_name_trainer())
                    if evolution:
                        Combat.combat_begin.set_pokemon1(pokedex2.choose_specific_pokemon(Combat.combat_begin.get_pokemon1().get_evolution_name()))
                        set_pokemon1(Combat.combat_begin.get_pokemon1())
                        set_combat(6)
                    else:
                        set_combat(4)
                else:
                    if Combat.combat_begin.get_pokemon2().get_name() == Combat.combat_begin.get_pokemon_player():
                        get_pokemon1().set_pv(get_pokemon1().get_pv_max())
                        set_pokemon2(pokedex2.choose_random_pokemon())
                        Combat.combat_begin.set_pokemon2(get_pokemon2())
                        Current_render.set_state(render_choose_fight.render_choose_fight)
                    else:
                        pokedex2.change_stat_pv(Combat.combat_begin.get_pokemon1().get_name(), Combat.combat_begin.get_pokemon1().get_pv(), trainer.get_name_trainer())
                        pokedex2.change_stat_xp(Combat.combat_begin.get_pokemon1().get_name(), trainer.get_name_trainer())
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
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{get_pokemon2().get_name()} est K.O. {get_pokemon1().get_name()} à maintenant {get_pokemon1().get_xp()} / {get_pokemon1().get_xp_max()} xp")
        draw_text(screen, dead_text, font_ingame, rectangle, 460, 60, max_lines=3)
        if suite_button.render(screen):  
            if get_state_combat() == 1:
                get_pokemon1().set_pv(get_pokemon1().get_pv_max())
                Current_render.set_state(render_choose_fight.render_choose_fight)
            else:
                set_pokemon1(pokedex2.choose_specific_pokemon(get_pokemon1().get_name()))
                set_pokemon2(pokedex2.choose_random_pokemon())
                scale = pokedex2.get_level_scale(get_pokemon1())
                get_pokemon2().set_level(random.randint(get_pokemon1().get_level() - scale, get_pokemon1().get_level() + scale))
                pokedex2.stats_level_scale(get_pokemon2())
                pokedex2.change_statut(get_pokemon2().get_name(), trainer.get_name_trainer())
                Combat.combat_begin.set_pokemon1(get_pokemon1())
                Combat.combat_begin.set_pokemon2(get_pokemon2())
                set_combat(0)
    
    elif get_combat() == 4:   
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{Combat.combat_begin.get_pokemon2().get_name()} est K.O. Félication {Combat.combat_begin.get_pokemon1().get_name()} est passé lvl {Combat.combat_begin.get_pokemon1().get_level()} et son xp est {Combat.combat_begin.get_pokemon1().get_xp()} / {Combat.combat_begin.get_pokemon1().get_xp_max()}")
        draw_text(screen, dead_text, font_ingame, rectangle, 460, 60, max_lines=3)
        if suite_button.render(screen):  
            if get_state_combat() == 1:
                get_pokemon1().set_pv(get_pokemon1().get_pv_max())
                Current_render.set_state(render_choose_fight.render_choose_fight)
            else:
                set_pokemon1(pokedex2.choose_specific_pokemon(get_pokemon1().get_name()))
                set_pokemon2(pokedex2.choose_random_pokemon())
                scale = pokedex2.get_level_scale(get_pokemon1())
                get_pokemon2().set_level(random.randint(get_pokemon1().get_level() - scale, get_pokemon1().get_level() + scale))
                pokedex2.stats_level_scale(get_pokemon2())
                pokedex2.change_statut(get_pokemon2().get_name(), trainer.get_name_trainer())
                Combat.combat_begin.set_pokemon1(get_pokemon1())
                Combat.combat_begin.set_pokemon2(get_pokemon2())
                set_combat(0)
    
    elif get_combat() == 6:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"Votre {Combat.combat_begin.get_pokemon_player()} vient d'évoluer en {Combat.combat_begin.get_pokemon1().get_name()}")
        draw_text(screen, dead_text, font_ingame, rectangle, 460, 60, max_lines=3)
        if suite_button.render(screen):
            set_pokemon1(pokedex2.choose_specific_pokemon(get_pokemon1().get_name()))
            set_pokemon2(pokedex2.choose_random_pokemon())
            scale = pokedex2.get_level_scale(get_pokemon1())
            get_pokemon2().set_level(random.randint(get_pokemon1().get_level() - scale, get_pokemon1().get_level() + scale))
            pokedex2.stats_level_scale(get_pokemon2())
            pokedex2.change_statut(get_pokemon2().get_name(), trainer.get_name_trainer())
            Combat.combat_begin.set_pokemon1(get_pokemon1())
            Combat.combat_begin.set_pokemon2(get_pokemon2())
            set_combat(0)
    
    elif get_combat() == 7:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        for index, pokemon in enumerate(trainer.get_pokemon_list()):
            if index <= 2:
                pokemon_button = Button(100 + 200 * index, 470, pokemon.get_name(), font_ingame, 0, 'black', 'black')
                if pokemon_button.render(screen):
                    Combat.combat_begin.set_pokemon1(pokedex2.choose_specific_pokemon(pokemon.get_name()))
                    set_pokemon1(Combat.combat_begin.get_pokemon1())
                    if turn_number == 0:
                        turn_number += 1
                        set_combat(1)
                        Combat.combat_begin.attack_chance()
                    else:
                        set_combat(0)
                        turn_number = 0
                    set_combat(0)
                elif suite_button.render(screen):
                    set_combat(0)
                
            elif index >= 3 and index <= 5:
                pokemon_button = Button(100 + 200 * (index - 3), 520, pokemon.get_name(), font_ingame, 0, 'black', 'black')
                if pokemon_button.render(screen):
                    Combat.combat_begin.set_pokemon1(pokedex2.choose_specific_pokemon(pokemon.get_name()))
                    set_pokemon1(Combat.combat_begin.get_pokemon1())
                    if turn_number == 0:
                        turn_number += 1
                        set_combat(1)
                        Combat.combat_begin.attack_chance()
                    else:
                        set_combat(0)
                        turn_number = 0
                    set_combat(0)
                elif suite_button.render(screen):
                    set_combat(0)

    elif get_combat() == 8:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if button_potion.render(screen):
            pv_earned = Message(100, 380, 550, 160, f"You earned 20 pv", 'white', 'black')	
            pv_earned.message_render(font_ingame, screen)
            if turn_number == 0:
                pygame.display.update()
                pygame.time.delay(1000)
                turn_number += 1
                Combat.combat_begin.attack_chance()
                set_combat(1)
            else:
                pygame.display.update()
                pygame.time.delay(1000)
                set_combat(0)
                turn_number = 0
            trainer.potion(Combat.combat_begin.get_pokemon1())
        elif button_pokeball.render(screen):
            set_combat(9)
    
    elif get_combat() == 9:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        catch_chance_ratio = trainer.pokeball()
        if catch_chance_ratio == 1:
            pokemon_catched = Message(100, 380, 550, 160, f"You caught {get_pokemon2().get_name()}", 'white', 'black')
            pokemon_catched.message_render(font_ingame, screen)
            pygame.display.update()
            pygame.time.delay(1000)
            Combat.combat_begin.set_pokemon2(pokedex2.choose_random_pokemon())
            set_pokemon2(Combat.combat_begin.get_pokemon2())
            set_combat(0)
        elif catch_chance_ratio == 0:
            pokemon_no_catched = Message(100, 380, 550, 160, f"You didn't catch {get_pokemon2().get_name()}", 'white', 'black')
            pokemon_no_catched.message_render(font_ingame, screen)
            pygame.display.update()
            pygame.time.delay(1000)
            if turn_number == 0:
                turn_number += 1
                set_combat(1)
                Combat.combat_begin.attack_chance()
            else:
                set_combat(0)
                turn_number = 0





    elif get_combat() == 8:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        if button_potion.render(screen):
            pv_earned = Message(100, 380, 550, 160, f"You earned 20 pv", 'white', 'black')	
            pv_earned.message_render(font_ingame, screen)
            if turn_number == 0:
                pygame.display.update()
                pygame.time.delay(1000)
                turn_number += 1
                Combat.combat_begin.attack_chance()
                set_combat(1)
            else:
                pygame.display.update()
                pygame.time.delay(1000)
                set_combat(0)
                turn_number = 0
            trainer.potion(Combat.combat_begin.get_pokemon1())
        elif button_pokeball.render(screen):
            set_combat(9)
    
    elif get_combat() == 9:
        rectangle = Rectangle.draw_rectangle(Rectangle(100, 380, 550, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        catch_chance_ratio = trainer.pokeball()
        if catch_chance_ratio == 1:
            pokemon_catched = Message(100, 380, 550, 160, f"You caught {get_pokemon2().get_name()}", 'white', 'black')
            pokemon_catched.message_render(font_ingame, screen)
            pygame.display.update()
            pygame.time.delay(1000)
            Combat.combat_begin.set_pokemon2(pokedex.choose_random_pokemon())
            set_pokemon2(Combat.combat_begin.get_pokemon2())
            set_combat(0)
        elif catch_chance_ratio == 0:
            pokemon_no_catched = Message(100, 380, 550, 160, f"You didn't catch {get_pokemon2().get_name()}", 'white', 'black')
            pokemon_no_catched.message_render(font_ingame, screen)
            pygame.display.update()
            pygame.time.delay(1000)
            if turn_number == 0:
                turn_number += 1
                set_combat(1)
                Combat.combat_begin.attack_chance()
            else:
                set_combat(0)
                turn_number = 0







