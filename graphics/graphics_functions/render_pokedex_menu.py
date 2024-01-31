import pygame
from game import *
from game.games_classes.Pokemon import *
from graphics.graphics_classes.Button import *
from graphics import *
from graphics.graphics_attributes import *
import game.current_render as Current_render
import graphics.graphics_functions.render_choose_fight as Render_choose_fight



selected_pokemon_type = ""
selected_pokemon_name = ""

def render_pokedex_menu():
    screen.fill((255, 255, 255))
    bcg_pokedex = Image('./assets/images/pokedex_pokemon_groupe.png', (0,0))
    bcg_pokedex.draw_image(screen)
    global selected_pokemon_type, selected_pokemon_name
    if get_pokedex_render() == 0:
        titre = Message(200, 30, 400, 10, 'POKEDEX', 'black', 'white')
        titre.message_render(font_button_menu_in, screen)

        buttons = []
        for i in range(4):
            x = 285 + 130 * i

            for j in range(4):
                y = 85 + 110 * j
                index = i * 4 + j + 1
                image_path = f'./assets/images/type/{str(index)}_gem.png'
                image = pygame.image.load(image_path)
                message_type = Message(x + 10, y + 85, 75, 15, pokemon_types[index - 1], 'black', 'black')
                message_type.message_render(font_ingame, screen)
                button_types = Button_image(x, y, image, 3)
                buttons.append(button_types.draw(screen))

        try:
            index = buttons.index(True)
        except:
            index = -1
        if index != -1:
            selected_pokemon_type = pokemon_types[index]
            set_pokedex_render(1)
        return_(screen)

    if get_pokedex_render() == 1:
        screen.fill((255, 255, 255))
        bcg_pokedex = Image('./assets/images/pokedex_pokemon_groupe.png', (0,0))
        bcg_pokedex.draw_image(screen)

        matching_pokemon = pokedex2.get_pokemon_by_type(selected_pokemon_type, trainer.get_name_trainer())

        for i, pokemon in enumerate(matching_pokemon):
            if len(matching_pokemon) == 1:
                titre = Message(350, 30, 40, 10, selected_pokemon_type, 'black', 'white')
                titre.message_render(font_button_menu_in, screen)
                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (100, 0))
                    image.scale_image((600,600))
                    image.draw_image(screen)
                elif pokemon.get_statut() == 1:
                    message_type = Message(400, 500, 75, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_input, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(100, 0, image, 10)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

            elif len(matching_pokemon) <= 2:
                titre = Message(350, 30, 40, 10, selected_pokemon_type, 'black', 'white')
                titre.message_render(font_button_menu_in, screen)
                x = 125 + 300 * (i % 2)
                y = 200 + 200 * (i // 2)
                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (x, y))
                    image.scale_image((170,170))
                    image.draw_image(screen)
                else:
                    message_type = Message(x + 110, y + 300, 75, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_ingame, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(x, y, image, 4)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

            elif len(matching_pokemon) <= 4:
                titre = Message(350, 30, 40, 10, selected_pokemon_type, 'black', 'white')
                titre.message_render(font_button_menu_in, screen)
                x = 150 + 300 * (i % 2)
                y = 120 + 220 * (i // 2)

                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (x, y))
                    image.scale_image((170,170))
                    image.draw_image(screen)
                else:
                    message_type = Message(x + 95, y + 170, 10, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_ingame, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(x, y, image, 3)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

            elif len(matching_pokemon) <= 8:
                titre = Message(350, 30, 40, 10, selected_pokemon_type, 'black', 'white')
                titre.message_render(font_button_menu_in, screen)
                x = 20 + 200 * (i % 4)
                y = 100 + 220 * (i // 4)

                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (x, y))
                    image.scale_image((150,150))
                    image.draw_image(screen)
                else:
                    message_type = Message(x + 60, y + 190, 75, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_ingame, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(x, y, image, 3)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

            elif len(matching_pokemon) <= 12:
                titre = Message(350, 30, 40, 10, selected_pokemon_type, 'black', 'white')
                titre.message_render(font_button_menu_in, screen)
                x = 30 + 200 * (i % 4)
                y = 120 + 150 * (i // 4)

                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (x, y))
                    image.scale_image((100,100))
                    image.draw_image(screen)
                else:
                    message_type = Message(x + 40, y + 130, 75, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_ingame, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(x, y, image, 2)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

            elif len(matching_pokemon) <= 16:
                titre = Message(350, 30, 40, 10, selected_pokemon_type, 'black', 'white')
                titre.message_render(font_button_menu_in, screen)
                x = 40 + 200 * (i % 4)
                y = 100 + 120 * (i // 4)

                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (x, y))
                    image.scale_image((100,100))
                    image.draw_image(screen)
                else:
                    message_type = Message(x + 35, y + 100, 30, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_ingame, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(x, y, image, 1.5)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

            else:
                titre = Message(350, 30, 40, 10, selected_pokemon_type, 'black', 'white')
                titre.message_render(font_title_in, screen)
                x = 50 + 90 * (i % 8)
                y = 80 + 60 * (i // 8)
                # image = f'./assets/images/pokemon_front/{pokemon.get_name()}.png' if pokemon.get_statut() == 1 else f'./assets/images/shadow/{pokemon.get_name()}.png'
                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (x, y))
                    image.draw_image(screen)
                else:
                    message_type = Message(x + 25, y + 40, 20, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_tiny, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(x, y, image, 1)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

        return_(screen)
        
    
    if get_pokedex_render() == 2:
        screen.fill((255, 220, 250))
        bcg_pokedex = Image('./assets/images/pokedex_pokemon_solo.png', (0,0))
        bcg_pokedex.draw_image(screen)

        matching_pokemon_name = pokedex2.get_pokemon_by_name(selected_pokemon_name, trainer.get_name_trainer())

        for index, pokemon in enumerate(matching_pokemon_name):
            titre = Message(350, 30, 40, 10, selected_pokemon_name, 'black', 'white')
            titre.message_render(font_input, screen)
            selected_pokemon_image = Image(f'./assets/images/pokemon_front/{selected_pokemon_name}.png', (0, 200))
            selected_pokemon_image.scale_image_bis(5, 5)
            selected_pokemon_image.draw_image(screen)
            level_message = Message(400, 150, 300, 40, f'Level = {str(pokemon.get_level())}', 'black', 'black')
            level_message.message_render(font_ingame, screen)
            attack_message = Message(400, 200, 300, 40, f'Attack = {str(pokemon.get_power_attack())}', 'black', 'black')
            attack_message.message_render(font_ingame, screen)
            defense_message = Message(400, 250, 300, 40, f'Defense = {str(pokemon.get_defense())}', 'black', 'black')
            defense_message.message_render(font_ingame, screen)
            speed_message = Message(400, 300, 300, 40, f'Speed = {str(pokemon.get_speed())}', 'black', 'black')
            speed_message.message_render(font_ingame, screen)
            life_point_message = Message(400, 350, 300, 40, f'Life point = {str(pokemon.get_pv())} / {str(pokemon.get_pv_max())}', 'black', 'black')
            life_point_message.message_render(font_ingame, screen)
            xp_point_message = Message(400, 400, 300, 40, f'Experience = {str(pokemon.get_xp())} / {str(pokemon.get_xp_max())}', 'black', 'black')
            xp_point_message.message_render(font_ingame, screen)
            add_pokemon_list()    
        return_(screen)

    if get_pokedex_render() == 3:
        render_list_pokemon()
        return_(screen)


def add_pokemon_list():
    global selected_pokemon_type, selected_pokemon_name
    pokemon = pokedex2.get_pokemon_by_name(selected_pokemon_name, trainer.get_name_trainer())[0]

    if pokemon.get_in_stockage() == 1:
        if button_remove_pokemon.render(screen):
            set_pokedex_render(3)
            trainer.remove_pokemon(pokemon)
            pokemon.set_in_stockage(0)
            Current_render.set_state(render_list_pokemon)
    elif pokemon.get_in_stockage() == 0:
        if button_add_pokemon.render(screen):
            if len(trainer.get_pokemon_list()) >= 6:
                full = Message(350, 480, 300, 40, f'Inventory full, please remove pokemon', 'black', 'white')
                full.message_render(font_ingame, screen)
                pygame.display.update()
                pygame.time.delay(1000)
                Current_render.set_state(render_list_pokemon)
            else:
                trainer.add_pokemon(pokemon)
                pokedex.change_pokemon_trainer(trainer.get_name_trainer(), pokemon)
                set_pokedex_render(3)
                pokemon.set_in_stockage(1)
                Current_render.set_state(render_list_pokemon)

def render_list_pokemon():
    bcg_pokedex_list = Image('./assets/images/pokedex_pokemon_choix.png', (0, 0))
    bcg_pokedex_list.draw_image(screen)
    for index, pokemon in enumerate(trainer.get_pokemon_list()):
        if index <= 2:
            image = Image(f'./assets/images/pokemon_front/{pokemon.get_name()}.png', (25 + 270 * index, 110))
            image.scale_image((200, 200))
            image.draw_image(screen)
        elif index >=3 and index <= 5:
            image = Image(f'./assets/images/pokemon_front/{pokemon.get_name()}.png', (25 + 270 * (index - 3), 320))
            image.scale_image((200, 200))
            image.draw_image(screen)
    
    if back_button.render(screen):
        set_pokedex_render(0)
        Current_render.set_state(render_pokedex_menu)



def return_(screen):
    if back_button.render(screen):
        if get_pokedex_render() == 0:
            Current_render.set_state(Render_choose_fight.render_choose_fight)
        elif get_pokedex_render() == 1:
            set_pokedex_render(0) 
        elif get_pokedex_render() == 2:
            set_pokedex_render(1)
        elif get_pokedex_render() == 3:
            set_pokedex_render(2)


