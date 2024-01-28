import pygame
from graphics.graphics_attributes import font_button_menu, font_ingame, font_long
from game.mouse_click import get_mouse_click
import time

class Button():
    def __init__(self, x, y, text, font, scale, color, hover_color):
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.clicked = False
        self.active = True
        self.last_click_time = time.time()

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
        if self.clicked and time.time() - self.last_click_time < 0.5:

            return False
        if self.rect.collidepoint(pos) and get_mouse_click():
                self.last_click_time = time.time()
                self.clicked = True
                action = True
                print(f"{self.text} clicked")
        else:
            self.clicked = False


        return action

    def render(self, screen):
        if self.active:
            self.draw(screen)
            return self.check_clicked()
        else:
            return False 




#create button instances
new_game_button = Button(240, 300, "NEW-GAME", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
continue_button = Button(240, 400, "CONTINUE", font_button_menu, 1, (255, 0, 0), (0, 255, 0))
attack_button = Button(150, 450, "FIGHT", font_ingame, 1, (0, 0, 0), (50, 50, 50))
object_button = Button(450, 450, "OBJECT", font_ingame, 1, (0, 0, 0), (50, 50, 50))
flee_button = Button(150, 510, "RUN", font_ingame, 1, (0, 0, 0), (50, 50, 50))
change_poke_button = Button(450, 510, "CHANGE POKEMON", font_ingame, 1, (0, 0, 0), (50, 50, 50))
suite_button = Button(680, 485, 'X', font_button_menu, 1, (0, 0, 0), (50, 50, 50))
valider_button = Button(20, 560, 'CHOOSE', font_ingame, 1, (0, 0, 0), (50, 50, 50))
valider_new_game_button = Button(680, 455, 'X', font_button_menu, 1, (0, 0, 0), (50, 50, 50))
choice_pokemon_1_button = Button(100, 320, "WATER", font_ingame, 1, (0, 0, 0), (50, 50, 50))
choice_pokemon_2_button = Button(370, 320, "FIRE", font_ingame, 1, (0, 0, 0), (50, 50, 50))
choice_pokemon_3_button = Button(610, 320, "GRASS", font_ingame, 1, (0, 0, 0), (50, 50, 50))
back_button = Button(720, 560, "BACK", font_ingame, 1, (0, 0, 0), (0, 255, 0))
# quit_button = Button.Button(200, 100, "Cliquez-moi", None, 2, (255, 0, 0), (0, 255, 0))


#button to choose the number of pokemon in the team
button_survival = Button(572, 200, 'Fight', font_long, 1, (0, 0, 0), (255, 0, 0))
button_pokedex = Button(575, 400, 'POKEDEX', font_long, 1, (0, 0, 0), (255, 0, 0))
button_add_pokemon = Button(475, 450, 'Add Pokemon', font_ingame, 1, (255, 0, 0), (0, 255, 0))
button_remove_pokemon = Button(475, 450, 'Remove Pokemon', font_ingame, 1, (255, 0, 0), (0, 255, 0))


#button to choose the different objects
button_potion = Button(150, 490, "Potion", font_ingame, 1, (0, 0, 0), (50, 50, 50))
button_pokeball = Button(500, 490, "Pokeball", font_ingame, 1, (0, 0, 0), (50, 50, 50))