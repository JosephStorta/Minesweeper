import pygame
from pygame import Surface, font, mouse
from globals import SCREEN_SIZE
from button import Button
import states
import states.game
import states.state

class MainMenu(states.state.State):
    def __init__(self):
        super().__init__()

        self.start_button = Button((100, 50), (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 4), "azure3")
        self.quit_button = Button((100, 50), (SCREEN_SIZE[0] / 2, 2 * SCREEN_SIZE[1] / 4), "azure3")

    def update(self, delta: int):
        self.start_button.update(delta)
        self.quit_button.update(delta)

        if self.start_button.getPressed():
            self.change = True
            self.next = states.game.Game((10, 8), 4)
        
        if self.quit_button.getPressed():
            self.exit = True

    def handleEvents(self, event):
        self.start_button.handleEvents(event)
        self.quit_button.handleEvents(event)

    def draw(self, display: Surface):
        self.start_button.draw(display)
        self.quit_button.draw(display)