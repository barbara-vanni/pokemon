import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font_title = pygame.font.Font('./assets/font/Pokemon_Solid.ttf',120)
font_title_in_page = pygame.font.Font('./assets/font/Pokemon_Solid.ttf',50)
font_title_in = pygame.font.Font('./assets/font/Pokemon_text.ttf', 28)
font_title_water = pygame.font.Font('./assets/font/Pokemon_Solid.ttf',20)
font_button_menu = pygame.font.Font('./assets/font/Pokemon_text.ttf',40)
font_button_menu_in = pygame.font.Font('./assets/font/Pokemon_text.ttf',30)
font_input = pygame.font.Font('./assets/font/Pokemon_text.ttf',40)
font_long = pygame.font.Font('./assets/font/Pokemon_text.ttf',20)
font_ingame = pygame.font.Font('./assets/font/Pokemon_text.ttf',15)
font_little = pygame.font.Font('./assets/font/Pokemon_text.ttf',14)
font_tiny = pygame.font.Font('./assets/font/Pokemon_text.ttf',10)

text_choix = (f"Hello (user_name), now you're gonna choose your first pokemon . . . . .  Choose wisely !")
num_words = 0

menu = 0
def get_menu():
    return menu
def set_menu(new_menu):
    global menu
    menu = new_menu


combat = 0
def get_combat():
    return combat
def set_combat(new_combat):
    global combat
    combat = new_combat

pokedex_render = 0
def get_pokedex_render():
    return pokedex_render
def set_pokedex_render(new_pokedex_render):
    global pokedex_render
    pokedex_render = new_pokedex_render

