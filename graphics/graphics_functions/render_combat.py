# from game import *
# from event import *
# from graphics.graphics_attributes import *
# from graphics.graphics_functions import *

# def render_combat(pokemon1, pokemon2):
#     screen.fill((255,255,255))
#     bcg_combat = Image('./assets/images/battlegrass.png', (0,0))
#     bcg_combat.draw_image(screen)

#     # Mise en place des informations graphiques pour le pokemon du dresseur 
#     pokemon_good = Image('./assets/images/carapuce_2.png', (0, 130))
#     pokemon_good.draw_image(screen)
#     border_good = Image('./assets/images/border_message.png', (430, 270))
#     border_good.draw_image(screen)
#     nom_good = Message(410, 280, 300, 50, f'{pokemon1.get_name()} lvl {pokemon1.get_level()}', 'white', 'black')
#     pv_good = Message(540, 325, 200, 30, f'{pokemon1.get_pv()} / {pokemon1.get_pv_max()} pv', 'white', 'black')
#     nom_good.message_render(font_ingame, screen)
#     pv_good.message_render(font_ingame, screen)
#     pygame.draw.rect(screen, 'white', (450, 360, 280, 10), 0, 15)
#     pygame.draw.rect(screen, 'blue', (450, 360, pokemon1.get_pv() * 280 / pokemon1.get_pv_max(), 10), 0, 15)

#     # Mise en place des informations graphiques pour le pokemon du vilain
#     pokemon_bad = Image('./assets/images/salameche_2.png', (440, -60))
#     pokemon_bad.draw_image(screen)
#     border_bad = Image('./assets/images/border_message.png', (20, 20))
#     border_bad.draw_image(screen)
#     nom_bad = Message(10, 30, 300, 50, f'{pokemon2.get_name()} lvl {pokemon2.get_level()}', 'green', 'black')
#     pv_bad = Message(128, 75, 200, 30, f'{pokemon2.get_pv()} / {pokemon2.get_pv_max()} pv', 'green', 'black')
#     nom_bad.message_render(font_ingame, screen)
#     pv_bad.message_render(font_ingame, screen)
#     pygame.draw.rect(screen, 'white',(40, 110, 280, 10), 0, 15)
#     pygame.draw.rect(screen, 'blue', (40, 110, pokemon2.get_pv() * 280 / pokemon2.get_pv_max(), 10), 0, 15)

#     #Menu de sélection de combat
#     if get_combat() == 0:
#         border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
#         border_option_message.draw_image(screen)
#         attack_button = Button_rect(30, 450, 350, 30, "FIGHT !", 'white', 'black')
#         attack_button.collision(font_ingame, screen)
#         object_button = Button_rect(410, 450, 350, 30, "OBJECT", 'white', 'black')
#         object_button.collision(font_ingame, screen)
#         flee_button = Button_rect(30, 510, 350, 30, "RUN", 'white', 'black')
#         flee_button.collision(font_ingame, screen)
#         new_pokemon_button = Button_rect(410, 510, 350, 30, "CHANGE POKEMON", 'white', 'black')
#         new_pokemon_button.collision(font_ingame, screen)
#         return attack_button, object_button, flee_button, new_pokemon_button
    
#     elif get_combat() == 1:
#         rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
#         border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
#         border_option_message.draw_image(screen)
#         draw_text(screen, combat_begin.get_render_message(), font_long, rectangle, 440, 60, max_lines=3)
#         suite_button = Button_image('./assets/images/forward.png', (700, 530))
#         suite_button.draw_image(screen)
#         suite_button.collision()
#         return suite_button

from game import *
from event import *
from graphics.graphics_attributes import *
from graphics.graphics_functions import *

def render_combat(pokemon1, pokemon2):
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
        suite_button.collision()
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
        suite_button.collision()
        return suite_button
    
    elif get_combat() == 3:    
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{pokemon2.get_name()} est K.O. {pokemon1.get_name()} à maintenant {pokemon1.get_xp()} / {pokemon1.get_xp_max()} xp")
        draw_text(screen, dead_text, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.collision()
        return suite_button
    
    elif get_combat() == 4:   
        rectangle = Rectangle.draw_rectangle(Rectangle(20, 420, 760, 160))
        border_option_message = Image('./assets/images/border_choice_message.png', (30, 410))
        border_option_message.draw_image(screen)
        dead_text = (f"{pokemon2.get_name()} est K.O. Félication {pokemon1.get_name()} est passé lvl {pokemon1.get_level()} et son xp est {pokemon1.get_xp()} / {pokemon1.get_xp_max()}")
        draw_text(screen, dead_text, font_long, rectangle, 440, 60, max_lines=3)
        suite_button = Button_image('./assets/images/forward.png', (700, 530))
        suite_button.draw_image(screen)
        suite_button.collision()
        return suite_button