import pygame
from pygame import Surface, image

class Button:
    def __init__(self, size, position, sprite):
        self.__sprite = image.load(sprite).convert()

        self.__size = size

        self.__position = position

        self.__hover = False
        self.__pressed = False
    
    def getPressed(self):
        return self.__pressed

    def update(self, delta: int):
        pass

    def handleEvents(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.__sprite.get_rect(center = self.__position).collidepoint(event.pos):
                self.__hover = True
            else:
                self.__hover = False

        if event.type == pygame.MOUSEBUTTONUP and self.__hover:
            self.__pressed = True
        else:
            self.__pressed = False

    def draw(self, display: Surface):
        display.blit(self.__sprite, (self.__position[0] - self.__size[0] / 2, self.__position[1] - self.__size[1] / 2))