"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Creation of Button_rect classes how allow to click on a Message.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pygame

from graphics.graphics_classes.Message import *

class Button_rect(Message):
    def __init__ (self, x, y, width, height, text, color_rect, color_font):
        Message.__init__(self, x, y, width, height, text, color_rect, color_font)
        self.__clicked = False

    def get_clicked(self):
        return self.__clicked
    def set_clicked(self):
        self.__clicked = not self.__clicked

    def collision(self, font, screen):
        rectangle = self.message_render(font, screen)
        pos = pygame.mouse.get_pos()
        if rectangle.collidepoint(pos):
            print('clic')
            self.set_clicked()
