# import pygame

# class Event:
#     def __init__(self):
#         self.__event = self.event_boucle()

#     def get_event(self):
#         return self.__event   
#     def set_event(self):
#         self.__event = self.event_boucle()

#     def event_boucle(self):
#         for self.__event in pygame.event.get():
#             self.set_event()
    
#     def quit_event(self, continuer):
#         if self.__event.type == pygame.QUIT:
#             return False
#         return continuer

#     def mouse_button_event(self, event, button_object):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if button_object.collision():
#                 print('clic')
# def quit_event(event, continuer):
#     if event.type == pygame.QUIT:
#         return False
#     return continuer

import pygame

class Event:
    def __init__(self):
        self.__event = None

    def get_event(self):
        return self.__event

    def event_boucle(self):
        for event in pygame.event.get():
            return event

    def quit_event(self, continuer, event_boucle_result):
        if event_boucle_result and event_boucle_result.type == pygame.QUIT:
            return False
        return continuer

