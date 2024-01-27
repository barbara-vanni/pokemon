from game import Pokedex
from game.games_attributes import *
from graphics import *
from graphics.graphics_attributes import *
import graphics.graphics_functions.render_combat as render_combat
import game.current_render as Current_render
from graphics.graphics_functions.render_new_game import *
import graphics.graphics_functions.render_pokedex_menu as render_pokedex

def render_choose_fight():
    if get_pokedex_render() == 0:

        image_font_choose_fight = pygame.image.load('./assets/images/background_menu.png')
        titre_choose_fight = Message(100, 20, 400, 100, 'Ready ?', 'black', 'red')
        image_trainer_choose_fight = pygame.image.load('./assets/images/ash1.png')
        screen.blit(image_font_choose_fight, (0, 0))

        pokemon_front_view = Image(trainer.get_actif_pokemon().get_image_front(), (200, 300))
        pokemon_front_view.scale_image((250, 250))
        pokemon_front_view.draw_image(screen)
        titre_choose_fight.message_render(font_button_menu, screen)

        
    if button_survival.render(screen):
        set_state_combat(0)
        Current_render.set_state(render_combat.render_combat_pokemon)
    elif button_pokedex.render(screen):
        Current_render.set_state(render_pokedex.render_pokedex_menu) 

    screen.blit(image_trainer_choose_fight, (-10, 180))