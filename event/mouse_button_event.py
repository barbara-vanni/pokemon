import pygame

def mouse_button_event(event, button_object, font, screen):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_object.get_clicked() == True:
            print('aaaaaaaaaaaa')