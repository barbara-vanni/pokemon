from graphics.graphics_attributes import *
from graphics.graphics_classes import *
# from game.current_render import *
from graphics.graphics_classes.Button import *
import game.current_render as Current_render
from graphics.graphics_functions.render_pokemon_choice import state_pokemon_choices


user_text = ''
input_rect = pygame.Rect(100, 450, 200, 50)
active = False
# color_active = pygame.Color('green')
# # color of input box
# color_passive = pygame.Color('red')
color = (255,245,255)


def render_new_game():
    global active, user_text
    bcg_new_game = Image('./assets/images/professor_chen_classico.png', (0, 0))
    bcg_new_game.draw_image(screen)
    enter_name = Message(300, 100, 600, 60, 'Who are you ?', 'white', 'white')
    enter_name.message_render(font_long, screen)

    input_box_state()
    # Input box for name user
    # input_rect = pygame.Rect(100, 450, 200, 50)
    # color = (255,245,255)
    # active = False
    # font = font_input
    # max_char = 13
    # input_text = ""
    # text_surface = font.render(input_text, True, (0,0,0))
    # width = max(200, text_surface.get_width()+10)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    # Save the entered name to the JSON file when Enter key is pressed
                    print(user_text)
                    # save_data(user_text, 0)  
                else:
                    user_text += event.unicode
                    if event.key == pygame.K_SPACE:
                        game_paused = True
        if valider_new_game_button.render(screen):
            Current_render.set_state(state_pokemon_choices)

    valider_new_game_button.render(screen)


def input_box_state():
    global user_text  
    # if active:
    #     color = color_active
    # else:
    #     color = color_passive

    # draw rectangle for input box
    pygame.draw.rect(screen, color, input_rect)
    text_surface = font_input.render(user_text, True, (0, 0, 0))
    # render
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    # set field for the text so it cannot get outside of the box
    input_rect.w = max(100, text_surface.get_width() + 10)

    return user_text


# def save_user_name(input_text):
#     data = {'user_name': input_text}
#     with open('user_data.json', 'w') as file:
#         json.dump(data, file)


