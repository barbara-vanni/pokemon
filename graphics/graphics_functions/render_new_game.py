# import pygame
from graphics.graphics_attributes import *
from graphics.graphics_classes import *
import sys
import json


def render_new_game():
    bcg_new_game = Image('./assets/images/professor_chen_classico.png', (0, 0))
    bcg_new_game.draw_image(screen)
    enter_name = Message(300, 100, 600, 60, 'Who are you ?', 'white', 'white')
    enter_name.message_render(font_long, screen)

    # Input box for name user
    input_rect = pygame.Rect(100, 450, 200, 50)
    input_text = ""
    font = font_input
    color = (255,245,255)
    max_char = 13

    valider_button = Button_image('./assets/images/forward.png', (650, 455))
    valider_button.draw_image(screen)
    valider_button.collision()


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(input_text)
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                if len(input_text) < max_char:
                    input_text += event.unicode
    pygame.draw.rect(screen, color, input_rect) 
    text_surface = font.render(input_text, True, (0,0,0))
    width = max(200, text_surface.get_width()+10)
    input_rect.w = width
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    valider_button.draw_image(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(60)
    # return render_new_game




# def save_user_name(input_text):
#     data = {'user_name': input_text}
#     with open('user_data.json', 'w') as file:
#         json.dump(data, file)


