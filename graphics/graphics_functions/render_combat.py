from game import *
from event import *
from graphics.graphics_attributes import *
from graphics.graphics_functions import *

def render_combat(pokemon1, pokemon2):
    screen.fill((150,150,150))
    bcg_combat = Image('./assets/images/bcg_combat.png', (0,0))
    bcg_combat.draw_image(screen)

    # Mise en place des informations graphiques pour le pokemon du dresseur 
    pokemon_good = Image('./assets/images/carapuce_2.png', (0, 150))
    pokemon_good.draw_image(screen)
    nom_good = Message(450, 275, 300, 40, f'{pokemon1.get_name()} lvl {pokemon1.get_level()}', 'green', 'black')
    pv_good = Message(450, 325, 300, 40, f'{pokemon1.get_pv()} / {pokemon1.get_pv_max()} pv', 'green', 'black')
    nom_good.message_render(font_ingame, screen)
    pv_good.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white', (450, 375, 300, 20), 0, 15)
    pygame.draw.rect(screen, 'blue', (450, 375, pokemon1.get_pv() * 300 / pokemon1.get_pv_max(), 20), 0, 15)

    # Mise en place des informations graphiques pour le pokemon du vilain
    pokemon_bad = Image('./assets/images/salameche_2.png', (500, 0))
    pokemon_bad.draw_image(screen)
    nom_bad = Message(50, 30, 300, 40, f'{pokemon2.get_name()} lvl {pokemon2.get_level()}', 'green', 'black')
    pv_bad = Message(50, 80, 300, 40, f'{pokemon2.get_pv()} / {pokemon2.get_pv_max()} pv', 'green', 'black')
    nom_bad.message_render(font_ingame, screen)
    pv_bad.message_render(font_ingame, screen)
    pygame.draw.rect(screen, 'white',(50, 130, 300, 20), 0, 15)
    pygame.draw.rect(screen, 'blue', (50, 130, pokemon2.get_pv() * 300 / pokemon2.get_pv_max(), 20), 0, 15)
    print(f"Here get_combat is {get_combat()}\r")
    #Menu de sélection de combat
    if get_combat() == 0:
        pygame.draw.rect(screen, 'white', (10, 410, 780, 180), 0, 15)
        attack_button = Button_rect(20, 430, 350, 40, "A l'attaque !", 'grey', 'black')
        attack_button.collision(font_ingame, screen)
        object_button = Button_rect(430, 430, 350, 40, "Objet", 'grey', 'black')
        object_button.collision(font_ingame, screen)
        flee_button = Button_rect(20, 530, 350, 40, "Fuir", 'grey', 'black')
        flee_button.collision(font_ingame, screen)
        new_pokemon_button = Button_rect(430, 530, 350, 40, "Changer de pokemon", 'grey', 'black')
        new_pokemon_button.collision(font_ingame, screen)
        return attack_button, object_button, flee_button, new_pokemon_button
    
    elif get_combat() == 1:
        rectangle = pygame.draw.rect(screen, 'white', (20, 420, 760, 160), 0, 0)
        if combat_begin.get_attack_chance_ratio() == 0:
            attack_missed = (f"L'attaque de {pokemon1.get_name()} à échoué")
            draw_text(screen, attack_missed, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_attack_chance_ratio() == 1:
            attack_normal = (f"L'attaque de {pokemon1.get_name()} à réussi")
            draw_text(screen, attack_normal, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_attack_chance_ratio() == 2:
            attack_critical = (f"L'attaque de {pokemon1.get_name()} est un coup critique")
            draw_text(screen, attack_critical, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.collision()
        return suite_button
    
    elif get_combat() == 2:
        rectangle = pygame.draw.rect(screen, 'white', (20, 420, 760, 160), 0, 0)
        if combat_begin.get_affinity_values() < 1:
            efficiency_none = (f"{pokemon1.get_name()} lance une attaque. C'est ne pas très efficace.")
            draw_text(screen, efficiency_none, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_affinity_values() == 1:
            efficiency = (f"{pokemon1.get_name()} lance une attaque")
            draw_text(screen, efficiency, font_long, rectangle, 440, 60, max_lines=3)
        elif combat_begin.get_affinity_values() > 1 :
            efficiency_top = (f"{pokemon1.get_name()} lance une attaque, C'est très efficace")
            draw_text(screen, efficiency_top, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.collision()
        return suite_button
    
    elif get_combat() == 3:    
        rectangle = pygame.draw.rect(screen, 'white', (20, 420, 760, 160), 0, 0)
        dead_text = (f"{pokemon2.get_name()} est K.O. {pokemon1.get_name()} à maintenant {pokemon1.get_xp()} / {pokemon1.get_xp_max()} xp")
        draw_text(screen, dead_text, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.collision()
        return suite_button
    
    elif get_combat() == 4:
        print('clic 2')    
        rectangle = pygame.draw.rect(screen, 'white', (20, 420, 760, 160), 0, 0)
        dead_text = (f"{pokemon2.get_name()} est K.O. Félication {pokemon1.get_name()} est passé lvl {pokemon1.get_level()} et son xp est {pokemon1.get_xp()} / {pokemon1.get_xp_max()}")
        draw_text(screen, dead_text, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.collision()
        return suite_button