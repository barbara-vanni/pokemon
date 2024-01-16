"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Creation of Button_rect classes how allow to click on a Message.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pygame

from .Message import *

class Button_rect(Message):
    def __init__ (self, x, y, width, height, text, color_rect, color_font):
        Message.__init__(self, x, y, width, height, text, color_rect, color_font)
        self.__clicked = False

    def get_clicked(self):
        return self.__clicked
    def set_clicked(self):
        self.__clicked = not self.__clicked

    def collision(self, font, screen):
        self.__collision_rect = self.message_render(font, screen)
        pos = pygame.mouse.get_pos()
        if self.__collision_rect.collidepoint(pos):
            self.set_clicked()
