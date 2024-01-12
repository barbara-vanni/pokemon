"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Creation Message classes children of Rectangle. Allow to draw message
Creation of setter and getter for the x, y, width, height attributes
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from graphics.graphics_classes.Rectangle import *

class Message(Rectangle):
    def __init__(self, x, y, width, height, text, color_rect, color_font):
        Rectangle.__init__(self, x, y, width, height)
        self.__text = text
        self.__color_rect = color_rect
        self.__color_font = color_font

    def get_text(self):
        return self.__text
    def set_text(self, text):
        self.__text = text

    def get_color_rect(self):
        return self.__color_rect
    def set_color_rect(self, color_rect):
        self.__color_rect = color_rect

    def get_color_font(self):
        return self.__color_font
    def set_color_font(self, color_font):
        self.__color_font = color_font
    
    def message_render_color(self, font, screen):
        rectangle = Rectangle.draw_rectangle(self)
        pygame.draw.rect(screen, self.__color_rect, rectangle, 0, 0)
        text_font = font.render(self.__text, True, self.__color_font)
        text_rect = text_font.get_rect(center=rectangle.center)
        screen.blit(text_font, text_rect)
        return rectangle
    
    def message_render(self, font, screen):
        rectangle = Rectangle.draw_rectangle(self)
        text_font = font.render(self.__text, True, self.__color_font)
        text_rect = text_font.get_rect(center=rectangle.center)
        screen.blit(text_font, text_rect)
        return rectangle