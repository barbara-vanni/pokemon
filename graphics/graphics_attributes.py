import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font_title = pygame.font.Font('./assets/font/Pokemon_Solid.ttf',120)
font_button_menu = pygame.font.Font('./assets/font/Pokemon_text.ttf',40)
font_long = pygame.font.Font('./assets/font/Pokemon_text.ttf',20)
font_ingame = pygame.font.Font('./assets/font/Pokemon_text.ttf',15)

text_choix = ("Bienvenue (nom du dresseur) avant de commencer ton aventure tu va devoir choisir ton pokemon. Attention le type de pokemon est important.")
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
