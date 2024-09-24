import pygame
from pygame import Surface

class Button:
    def __init__(self, size, position, color):
        self.__surface = Surface(size)
        self.__surface.fill(color)

        self.__position = position

        self.__hover = False
        self.__pressed = False
    
    def getPressed(self):
        return self.__pressed

    def update(self, delta: int):
        pass

    def handleEvents(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.__surface.get_rect(center = self.__position).collidepoint(event.pos):
                self.__hover = True
            else:
                self.__hover = False

        if event.type == pygame.MOUSEBUTTONUP and self.__hover:
            self.__pressed = True
        else:
            self.__pressed = False

    def draw(self, display: Surface):
        display.blit(self.__surface, (self.__position[0] - self.__surface.get_width() / 2, self.__position[1] - self.__surface.get_height() / 2))