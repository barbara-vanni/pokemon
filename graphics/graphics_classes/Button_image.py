from graphics.graphics_classes.Image import *

class Button_image(Image):
    def __init__(self, image, image_pos):
        Image.__init__(self, image, image_pos)
        self.__rect = self.get_image_surface().get_rect(topleft=image_pos)
        self.__clicked = False
        
    def get_clicked(self):
        return self.__clicked
    def set_clicked(self):
        self.__clicked = not self.__clicked

    def collision(self):
        pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(pos):
            self.set_clicked()
            return True
        return False

