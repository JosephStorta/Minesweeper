import pygame
from pygame import Surface, font, mouse
from globals import SCREEN_SIZE
from states.state import State
from states.game import Game

class MainMenu(State):
    def __init__(self):
        super().__init__()

    def update(self, delta: int):
        pass

    def handleEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change = True
                self.next = Game((10, 8), 5)

    def draw(self, display: Surface):
        pass