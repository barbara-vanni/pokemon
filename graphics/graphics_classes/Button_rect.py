"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Creation of Button_rect classes how allow to click on a Message.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import Pygame
from Message import *

class Button_rect(Message):
    def __init__ (self, x, y, width, height, text, color_rect, color_font):
        Message.__init__(self, x, y, width, height, text, color_rect, color_font)
        self.__clicked = False

        def get_clicked(self):
            return self.__clicked

        def set_clicked(self):
            self.__clicked = not self.__clicked

    def collision(self, font, screen):
        self.message_render(font, screen)
        pos = Pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and self.__clicked == False:
            self.set_clicked()
