"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Creation Message classes children of Rectangle. Allow to draw message
Creation of setter and getter for the x, y, width, height attributes
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from Rectangle import *

class Message(Rectangle):
    def __init__(self, x, y, width, height, text, color_rect, color_font):
        Rectangle.__init__(self, x, y, width, height)
        self.__text = text
        self.__color_rect = color_rect
        self.__color_font = color_font

        def get_text():
            return self.__text
        def set_text(text):
            self.__text = text

        def get_color_rect():
            return self.__color_rect
        def set_text(color_rect):
            self.__color_rect = color_rect

        def get_color_font():
            return self.__color_font
        def set_text(color_font):
            self.__color_font = color_font

        def message_render(font, screen):
            rectangle = Rectangle.draw_rectangle(x, y, width, height)
            Pygame.draw.rect(screen, get_color_rect(), rectangle, 0, 15)
            text_font = font.render(self.__text, True, get_color_font())
            text_rect = text_font.get_rect(center=rectangle.center)
            screen.blit(text_font, text_rect)