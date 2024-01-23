import pygame
from game import Pokedex
from graphics import *
from graphics.graphics_attributes import *
import random
import os



def render_choose_fight(pokemon1):
    if get_pokedex_render() == 0:       
        pokedex = Pokedex()
       

        image_font = pygame.image.load('./assets/images/background_menu.png')
        titre = Message(100, 20, 400, 100, 'Ready ?', 'black', 'red')
        image_trainer = pygame.image.load('./assets/images/ash1.png')

        pokemon_front_folder = './assets/images/pokemon_front'
        pokemon_images = [f for f in os.listdir(pokemon_front_folder) if os.path.isfile(os.path.join(pokemon_front_folder, f))]

        random_pokemon_image = random.choice(pokemon_images)
    
        image_random_pokemon = pygame.image.load(os.path.join(pokemon_front_folder, random_pokemon_image))
        image_random_pokemon = pygame.transform.scale(image_random_pokemon, (300, 400))



        screen.blit(image_font, (0, 0))
        titre.message_render(font_title_in_page, screen)
        screen.blit(image_trainer, (-10, 180))
        screen.blit(image_random_pokemon, (200, 160))
        pygame.display.flip()
        pygame.time.delay(2000)

     