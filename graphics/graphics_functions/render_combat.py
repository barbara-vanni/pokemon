from graphics.graphics_attributes import *
from graphics.graphics_classes.Image import *
from graphics.graphics_classes.Message import *

def render_combat():
    screen.fill((150,150,150))
    nom_good = Message(450, 280, 300, 20, 'carapuce lvl 1', 'green', 'black')
    pv_good = Message(450, 320, 300, 20, '100 / 100 pv', 'green', 'black')
    bcg_combat = Image('./assets/images/bcg_combat.png', (0,0))
    bcg_combat.draw_image(screen)
    pokemon_good = Image('./assets/images/carapuce.png', (0, 150))
    pokemon_good.draw_image(screen)
    pokemon_bad = Image('./assets/images/salameche.png', (500, 0))
    pokemon_bad.draw_image(screen)
    nom_good.message_render(font_ingame, screen)
    pv_good.message_render(font_ingame, screen)
