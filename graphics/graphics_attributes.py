import pygame
from assets import *

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font_title = pygame.font.Font('./assets/font/Pokemon_Solid.ttf',120)
font_button_menu = pygame.font.Font('./assets/font/Pokemon_text.ttf',40)
font_long = pygame.font.Font('./assets/font/Pokemon_text.ttf',20)
font_ingame = pygame.font.Font('./assets/font/Pokemon_text.ttf',15)
