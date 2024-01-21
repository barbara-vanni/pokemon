import pygame
from graphics import *

class Image:
    def __init__(self, image, image_pos):
        self.__image = image
        self.__image_pos = image_pos
        self.__image_surface = None 

    def get_image(self):
        return self.__image

    def set_image(self, image):
        self.__image = image
        self.__image_surface = None
        
    def get_image_pos(self):
        return self.__image_pos

    def get_image_surface(self):
        if self.__image_surface is None:
            self.__image_surface = pygame.image.load(self.__image).convert_alpha()
        return self.__image_surface

    def draw_image(self, screen):
        screen.blit(self.get_image_surface(), self.__image_pos)
    
    def scale_image(self, scale):
        self.__image_surface = pygame.transform.scale(self.get_image_surface(), scale)
    
    def scale_image_bis(self, width_scale, height_scale):
        original_surface = self.get_image_surface()
        scaled_surface = pygame.transform.scale(original_surface, (int(original_surface.get_width() * width_scale), int(original_surface.get_height() * height_scale)))
        self.__image_surface = scaled_surface