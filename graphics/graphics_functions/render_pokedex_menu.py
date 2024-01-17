import pygame
from game import *
from graphics import *
from graphics.graphics_attributes import *

def render_pokemon_menu():
    titre = Message(200, 20, 400, 100, 'Pokedex', 'black', 'red')
    titre.message_render(font_title, screen)
    
    for i in range(4):  # 4 colonnes
        x = 75 + 200 * i
        
        for j in range(4):  # 4 lignes par colonne
            y = 150 + 110 * j
            index = j * 4 + i + 1
            image_path = f'./assets/images/type/badges_{str(index)}.jpg'
            image = pygame.image.load(image_path)
            message_type = Message(x, y + 80, 75, 15, pokemon_types[index - 1], 'black', 'white')
            message_type.message_render(font_ingame, screen)
            button_types = Button_image(x, y, image, 1)
            button_types.draw(screen)
