import pygame
from game import Pokedex
from graphics import *
from graphics.graphics_attributes import *
import graphics.graphics_functions.render_combat as render_combat
import game.current_render as Current_render
from graphics.graphics_functions.render_new_game import *
import random
import os



def render_choose_fight(pokemon1):
    if get_pokedex_render() == 0:       
        pokedex = Pokedex()
       

        image_font_choose_fight = pygame.image.load('./assets/images/background_menu.png')
        titre_choose_fight = Message(100, 20, 400, 100, 'Ready ?', 'black', 'red')
        image_trainer_choose_fight = pygame.image.load('./assets/images/ash1.png')
        
        pokemon_front_folder = './assets/images/pokemon_front'
        pokemon_images = [f for f in os.listdir(pokemon_front_folder) if os.path.isfile(os.path.join(pokemon_front_folder, f))]
        random_pokemon_image = random.choice(pokemon_images)
        image_random_pokemon = pygame.image.load(os.path.join(pokemon_front_folder, random_pokemon_image))
        image_random_pokemon = pygame.transform.scale(image_random_pokemon, (300, 400))


        screen.blit(image_font_choose_fight, (0, 0))
        titre_choose_fight.message_render(font_title_in_page, screen)

        if button_one.render(screen):
            Current_render.set_state(render_new_game)
        if button_two.render(screen):
            Current_render.set_state(render_combat.render_combat)
        if button_three.render(screen):
            Current_render.set_state(render_combat.render_combat)
        if button_four.render(screen):
            Current_render.set_state(render_combat.render_combat)
        if button_five.render(screen):
            Current_render.set_state(render_combat.render_combat)
        if button_six.render(screen):
            Current_render.set_state(render_combat.render_combat)
        if button_pokedex.render(screen):
            Current_render.set_state(render_pokedex)


        screen.blit(image_trainer_choose_fight, (-10, 180))
        screen.blit(image_random_pokemon, (200, 160))
        pygame.display.flip()
        pygame.time.delay(2000)

     