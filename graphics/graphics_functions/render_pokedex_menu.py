import pygame
from game import *
from graphics.graphics_classes.Button import *
from graphics import *
from graphics.graphics_attributes import *

selected_pokemon_type = ""
selected_pokemon_name = ""

def render_pokedex_menu():
    screen.fill((255, 255, 255))
    bcg_pokedex = Image('./assets/images/pokedex_pokemon_groupe.png', (0,0))
    bcg_pokedex.draw_image(screen)
    global selected_pokemon_type, selected_pokemon_name
    if get_pokedex_render() == 0:
        titre = Message(200, 30, 400, 10, 'POKEDEX', 'black', 'white')
        titre.message_render(font_button_menu, screen)

        buttons = []
        for i in range(4):
            x = 285 + 130 * i

            for j in range(4):
                y = 85 + 110 * j
                index = i * 4 + j + 1
                image_path = f'./assets/images/type/badges_{str(index)}.jpg'
                image = pygame.image.load(image_path)
                message_type = Message(x, y + 80, 75, 15, pokemon_types[index - 1], 'black', 'black')
                message_type.message_render(font_ingame, screen)
                button_types = Button_image(x, y, image, 1)
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

        matching_pokemon = pokedex.get_pokemon_by_type(selected_pokemon_type)

        for i, pokemon in enumerate(matching_pokemon):
            if len(matching_pokemon) == 1:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_button_menu, screen)
                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (100, 0))
                    image.scale_image((600,600))
                    image.draw_image(screen)
                else:
                    message_type = Message(400, 500, 75, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_input, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(100, 0, image, 10)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

            elif len(matching_pokemon) <= 2:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_button_menu, screen)
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
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_button_menu, screen)
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
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_button_menu, screen)
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
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_button_menu, screen)
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
                titre = Message(200, 20, 200, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_button_menu, screen)
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
                titre = Message(200, 10, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title_in, screen)
                x = 50 + 160 * (i % 5)
                y = 80 + 80 * (i // 5)
                # image = f'./assets/images/pokemon_front/{pokemon.get_name()}.png' if pokemon.get_statut() == 1 else f'./assets/images/shadow/{pokemon.get_name()}.png'
                if pokemon.get_statut() == 0:
                    image = Image(f'./assets/images/shadow/{pokemon.get_name()}.png', (x, y))
                    image.draw_image(screen)
                else:
                    message_type = Message(x + 25, y + 60, 20, 15, pokemon.get_name(), 'black', 'black')
                    message_type.message_render(font_little, screen)
                    image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                    image = pygame.image.load(image_path)
                    button_types = Button_image(x, y, image, 1)
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)

        return_(screen)
        
    
    if get_pokedex_render() == 2:
        screen.fill((255, 220, 250))

        matching_pokemon_name = pokedex.get_pokemon_by_name(selected_pokemon_name)

        for index, pokemon in enumerate(matching_pokemon_name):
            titre = Message(200, 20, 400, 100, selected_pokemon_name, 'black', 'red')
            titre.message_render(font_input, screen)
            selected_pokemon_image = Image(f'./assets/images/pokemon_front/{selected_pokemon_name}.png', (0, 200))
            selected_pokemon_image.scale_image_bis(5, 5)
            selected_pokemon_image.draw_image(screen)
            level_message = Message(400, 200, 300, 40, f'Level = {str(pokemon.get_level())}', 'black', 'red')
            level_message.message_render(font_long, screen)
            attack_message = Message(400, 250, 300, 40, f'Attack = {str(pokemon.get_power_attack())}', 'black', 'red')
            attack_message.message_render(font_long, screen)
            defense_message = Message(400, 300, 300, 40, f'Defense = {str(pokemon.get_defense())}', 'black', 'red')
            defense_message.message_render(font_long, screen)
            speed_message = Message(400, 350, 300, 40, f'Speed = {str(pokemon.get_speed())}', 'black', 'red')
            speed_message.message_render(font_long, screen)
            life_point_message = Message(400, 400, 300, 40, f'Life point = {str(pokemon.get_pv())} / {str(pokemon.get_pv_max())}', 'black', 'red')
            life_point_message.message_render(font_long, screen)
            xp_point_message = Message(400, 450, 300, 40, f'Experience = {str(pokemon.get_xp())} / {str(pokemon.get_xp_max())}', 'black', 'red')
            xp_point_message.message_render(font_long, screen)
            if pokemon.get_in_stockage() == 1:
                in_stockage_message = Message(400, 450, 300, 40, f'{pokemon.get_name()} vous accompagne!')
                in_stockage_message.message_render(font_long, screen)
            else:
                add_to_stockage_button = Button_rect(400, 500, 300, 80, 'Ajouter au stockage', 'black', 'red')
                add_to_stockage_button.collision(font_long, screen)
        return_(screen)

def return_(screen):
    if back_button.render(screen):
        if get_pokedex_render() == 1:
            set_pokedex_render(0) 
        elif get_pokedex_render() == 2:
            set_pokedex_render(1)


