"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Creation of Rectangle classes how allow you to draw Rectangle. 
Creation of setter and getter for the x, y, width, height attributes
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import pygame

class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    
    def set_y(self, y):
        self.__y = y
    def get_y(self):
        return self.__y
    
    def set_width(self, width):
        self.__width = width
    def get_width(self):
        return self.__width
    
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height
    
    def draw_rectangle(self):
        return pygame.Rect(self.__x, self.__y, self.__width, self.__height)