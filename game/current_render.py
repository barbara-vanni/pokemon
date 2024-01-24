from graphics.graphics_functions import render_main
# from graphics.graphics_functions import render_combat
from graphics.graphics_classes.Button import *
from graphics.graphics_attributes import *

state = render_main.render_main_menu

def get_state():
    return state

def set_state(new_state):
    global state
    state = new_state

# def get_state_combat():
#     return state_combat

# def set_state_combat(new_state_combat):
#     global state_combat
#     state_combat = new_state_combat