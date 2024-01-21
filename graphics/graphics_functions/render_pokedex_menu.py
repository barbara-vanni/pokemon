import pygame
from game import *
from graphics import *
from graphics.graphics_attributes import *

selected_pokemon_type = ""
selected_pokemon_name = ""

def render_pokedex_menu():
    global selected_pokemon_type, selected_pokemon_name
    if get_pokedex_render() == 0:
        titre = Message(200, 20, 400, 100, 'Pokedex', 'black', 'red')
        titre.message_render(font_title, screen)

        for i in range(4):
            x = 75 + 200 * i

            for j in range(4):
                y = 150 + 110 * j
                index = j * 4 + i + 1
                image_path = f'./assets/images/type/badges_{str(index)}.jpg'
                image = pygame.image.load(image_path)
                message_type = Message(x, y + 80, 75, 15, pokemon_types[index - 1], 'black', 'white')
                message_type.message_render(font_ingame, screen)
                button_types = Button_image(x, y, image, 1)
                button_types.draw(screen)

                for event in pygame.event.get():
                    # if event.type == pygame.QUIT:
                    #     continuer = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button_types.draw(screen):
                            selected_pokemon_type = pokemon_types[index - 1]
                            set_pokedex_render(1)
        return_button = Button_rect(80, 530, 150, 60, 'Retour', 'black', 'red')
        return_button.collision(font_button_menu, screen)

    if get_pokedex_render() == 1:
        screen.fill((0, 0, 0))

        matching_pokemon = pokedex.get_pokemon_by_type(selected_pokemon_type)

        for i, pokemon in enumerate(matching_pokemon):
            if len(matching_pokemon) == 1:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title, screen)
                message_type = Message(400, 500, 75, 15, pokemon.get_name(), 'black', 'white')
                message_type.message_render(font_title, screen)
                image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                image = pygame.image.load(image_path)
                button_types = Button_image(100, 0, image, 10)
                button_types.draw(screen)

            elif len(matching_pokemon) <= 2:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title, screen)
                x = 50 + 400 * (i % 2)
                y = 150 + 200 * (i // 2)
                message_type = Message(x + 120, y + 350, 75, 15, pokemon.get_name(), 'black', 'white')
                message_type.message_render(font_title_in_page, screen)
                image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                image = pygame.image.load(image_path)
                button_types = Button_image(x, y, image, 5)
                button_types.draw(screen)

            elif len(matching_pokemon) <= 4:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title, screen)
                x = 150 + 300 * (i % 2)
                y = 120 + 220 * (i // 2)
                message_type = Message(x + 60, y + 200, 75, 15, pokemon.get_name(), 'black', 'white')
                message_type.message_render(font_title_in_page, screen)
                image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                image = pygame.image.load(image_path)
                button_types = Button_image(x, y, image, 3)
                button_types.draw(screen)

            elif len(matching_pokemon) <= 8:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title, screen)
                x = 20 + 200 * (i % 4)
                y = 100 + 220 * (i // 4)
                message_type = Message(x + 60, y + 200, 75, 15, pokemon.get_name(), 'black', 'white')
                message_type.message_render(font_title_in, screen)
                image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                image = pygame.image.load(image_path)
                button_types = Button_image(x, y, image, 3)
                button_types.draw(screen)

            elif len(matching_pokemon) <= 12:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title, screen)
                x = 30 + 200 * (i % 4)
                y = 120 + 150 * (i // 4)
                message_type = Message(x + 40, y + 130, 75, 15, pokemon.get_name(), 'black', 'white')
                message_type.message_render(font_title_in, screen)
                image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                image = pygame.image.load(image_path)
                button_types = Button_image(x, y, image, 2)
                button_types.draw(screen)

            elif len(matching_pokemon) <= 16:
                titre = Message(200, 20, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title, screen)
                x = 40 + 200 * (i % 4)
                y = 100 + 120 * (i // 4)
                message_type = Message(x + 10, y + 100, 75, 15, pokemon.get_name(), 'black', 'white')
                message_type.message_render(font_title_in, screen)
                image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                image = pygame.image.load(image_path)
                button_types = Button_image(x, y, image, 1.5)
                button_types.draw(screen)

            else:
                titre = Message(200, 10, 400, 100, selected_pokemon_type, 'black', 'red')
                titre.message_render(font_title_in, screen)
                x = 50 + 160 * (i % 5)
                y = 80 + 80 * (i // 5)
                message_type = Message(x, y + 70, 75, 15, pokemon.get_name(), 'black', 'white')
                message_type.message_render(font_title_water, screen)
                image_path = f'./assets/images/pokemon_front/{pokemon.get_name()}.png'
                image = pygame.image.load(image_path)
                button_types = Button_image(x, y, image, 1)
                button_types.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_types.draw(screen):
                        selected_pokemon_name = pokemon.get_name()
                        set_pokedex_render(2)
                        
        return_button = Button_rect(80, 530, 150, 60, 'Retour', 'black', 'red')
        return_button.collision(font_button_menu, screen)
    
    if get_pokedex_render() == 2:
        screen.fill((0, 0, 0))

        matching_pokemon_name = pokedex.get_pokemon_by_name(selected_pokemon_name)

        for index, pokemon in enumerate(matching_pokemon_name):
            titre = Message(200, 20, 400, 100, selected_pokemon_name, 'black', 'red')
            titre.message_render(font_title, screen)
            selected_pokemon_image = Image(f'./assets/images/pokemon_front/{selected_pokemon_name}.png', (0, 200))
            selected_pokemon_image.scale_image_bis(5, 5)
            selected_pokemon_image.draw_image(screen)
            level_message = Message(400, 150, 300, 40, f'Level = {str(pokemon.get_level())}', 'black', 'red')
            level_message.message_render(font_long, screen)
            attack_message = Message(400, 200, 300, 40, f'Attack = {str(pokemon.get_power_attack())}', 'black', 'red')
            attack_message.message_render(font_long, screen)
            defense_message = Message(400, 250, 300, 40, f'Defense = {str(pokemon.get_defense())}', 'black', 'red')
            defense_message.message_render(font_long, screen)
            speed_message = Message(400, 300, 300, 40, f'Speed = {str(pokemon.get_speed())}', 'black', 'red')
            speed_message.message_render(font_long, screen)
            life_point_message = Message(400, 350, 300, 40, f'Life point = {str(pokemon.get_pv())} / {str(pokemon.get_pv_max())}', 'black', 'red')
            life_point_message.message_render(font_long, screen)
            xp_point_message = Message(400, 400, 300, 40, f'Experience = {str(pokemon.get_xp())} / {str(pokemon.get_xp_max())}', 'black', 'red')
            xp_point_message.message_render(font_long, screen)
            # if pokemon.get_in_stockage() == 1:
            #     in_stockage_message = Message(400, 450, 300, 40, f'{pokemon.get_name()} vous accomapgne!')
            #     in_stockage_message.message_render(font_long, screen)
            # else:
            #     add_to_stockage_button = Button_rect(400, 500, 300, 400, 'Ajouter au stockage', 'black', 'red')
            #     add_to_stockage_button.collision(font_long, screen)
            return_button = Button_rect(80, 530, 150, 60, 'Retour', 'black', 'red')
            return_button.collision(font_button_menu, screen)

