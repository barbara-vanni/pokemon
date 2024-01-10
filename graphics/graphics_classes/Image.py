import pygame
from graphics.graphics_attributes import *

class Image:
    def __init__(self, image, image_pos):
        self.__image = image
        self.__image_pos = image_pos
    
    def get_image(self):
        return self.__image
    def set_image(self, image):
        self.__image = image
    
    def get_image_pos(self):
        return self.__image_pos
    def set_image(self, image_pos):
        self.__image_pos = image_pos
        
    def draw_image(self):
        pygame.image.load(self.__image).convert_alpha()
        screen.blit(self.__image, self.__image_pos)