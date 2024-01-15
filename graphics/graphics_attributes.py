import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font_title = pygame.font.Font('./assets/font/Pokemon_Solid.ttf',120)
font_button_menu = pygame.font.Font('./assets/font/Pokemon_text.ttf',40)
font_long = pygame.font.Font('./assets/font/Pokemon_text.ttf',20)
font_ingame = pygame.font.Font('./assets/font/Pokemon_text.ttf',15)

text_attaque = ("Le Pokémon (nom de pokemon) lance l'attaque (nom de l'attaque). C'est (efficacité) efficace.")
text_choix = (f"Hello (user_name), now you're gonna choose your first pokemon . . . . .  Choose wisely !")
num_words = 0
