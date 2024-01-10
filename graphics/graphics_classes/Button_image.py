from graphics.graphics_classes.Image import *

class Button_image(Image):
    def __init__(self, image, image_pos):
        Image.__init__(self, image, image_pos)
        self.__rect = Image.get_image().get_rect()
        self.__clicked = False
        
    def get_clicked(self):
        return self.__clicked
    def set_clicked(self):
        self.__clicked = not self.__clicked

    def collision(self, screen):
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            print('clic')
            self.set_clicked()
