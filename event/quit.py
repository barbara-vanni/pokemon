import pygame

def quit_event(event, continuer):
    if event.type == pygame.QUIT:
        return False
    return continuer