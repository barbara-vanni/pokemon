import pygame
from assets import *
from graphics.graphics_attributes import font_button_menu, font_ingame, font_long

class Button():
    def __init__(self, x, y, text, font, scale, color, hover_color):
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.clicked = False
        self.active = True 

        self.create_button(x, y, scale)

    def create_button(self, x, y, scale):
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def check_clicked(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                print(self.text + " Clicked")
                action = True
        elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
            self.clicked = False
        else:
            self.clicked = False

        if action:
            self.image = self.font.render(self.text, True, self.hover_color)
        else:
            self.image = self.font.render(self.text, True, self.color)

        return action


    # def check_clicked(self):
    #     action = False
    #     pos = pygame.mouse.get_pos()

    #     if self.rect.collidepoint(pos):
    #         if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
    #             self.clicked = True
    #             print(self.text + " Clicked")
    #             action = True
    #         elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
    #             self.clicked = False  
    #     else:
    #         self.clicked = False
    #     return action

    def render(self, screen):
        if self.active:
            self.draw(screen)
            return self.check_clicked()
        else:
            return False 




#create button instances
new_game_button = Button(200, 250, "NEW-GAME", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
continue_button = Button(200, 350, "CONTINUE", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
option_button = Button(200, 450, "OPTION", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
attack_button = Button(150, 450, "FIGHT", font_ingame, 1, (0, 0, 0), (50, 50, 50))
object_button = Button(450, 450, "OBJECT", font_ingame, 1, (0, 0, 0), (50, 50, 50))
flee_button = Button(150, 510, "RUN", font_ingame, 1, (0, 0, 0), (50, 50, 50))
change_poke_button = Button(450, 510, "CHANGE POKEMON", font_ingame, 1, (0, 0, 0), (50, 50, 50))
suite_button = Button(680, 485, 'X', font_button_menu, 1, (0, 0, 0), (50, 50, 50))
valider_button = Button(680, 485, 'X', font_button_menu, 1, (0, 0, 0), (50, 50, 50))
valider_new_game_button = Button(680, 485, 'X', font_button_menu, 1, (0, 0, 0), (50, 50, 50))
choice_pokemon_1_button = Button(20, 300, "Type Eau", font_ingame, 1, (0, 0, 0), (50, 50, 50))
choice_pokemon_2_button = Button(300, 300, "Type Feu", font_ingame, 1, (0, 0, 0), (50, 50, 50))
choice_pokemon_3_button = Button(580, 300, "Type Plante", font_ingame, 1, (0, 0, 0), (50, 50, 50))
back_button = Button(720, 560, "BACK", font_ingame, 1, (0, 0, 0), (0, 255, 0))
# quit_button = Button.Button(200, 100, "Cliquez-moi", None, 2, (255, 0, 0), (0, 255, 0))


#button to choose the number of pokemon in the team
button_one = Button(587, 115, '1 vs 1', font_long, 1, (0, 0, 0), (255, 0, 0))
button_two = Button (587, 175, '2 vs 2', font_long, 1, (0, 0, 0), (255, 0, 0))
button_three = Button(587, 235, '3 vs 3', font_long, 1, (0, 0, 0), (255, 0, 0))
button_four = Button(587, 295, '4 vs 4', font_long, 1, (0, 0, 0), (255, 0, 0))
button_five = Button(587, 355, '5 vs 5', font_long, 1, (0, 0, 0), (255, 0, 0))
button_six = Button(587, 415, '6 vs 6', font_long, 1, (0, 0, 0), (255, 0, 0))
button_pokedex = Button(575, 475, 'POKEDEX', font_long, 1, (0, 0, 0), (255, 0, 0))