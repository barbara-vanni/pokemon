import pygame
from graphics.graphics_attributes import *

def attack_button_event(event, button_object):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_object.get_clicked() == True:
            set_combat(1)