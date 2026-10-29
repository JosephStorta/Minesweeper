from pygame import Surface

from globals import SCREEN_SIZE
from button import Button
from states import game
from states.state import State

class MainMenu(State):
    def __init__(self):
        super().__init__()

        self.start_button = Button((100, 50), (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 4), "./sprites/start_button.png")
        self.quit_button = Button((100, 50), (SCREEN_SIZE[0] / 2, 2 * SCREEN_SIZE[1] / 4), "./sprites/exit_button.png")

    def update(self, delta: int):
        self.start_button.update(delta)
        self.quit_button.update(delta)

        if self.start_button.getPressed():
            self.change = True
            self.next = game.Game((16, 10), 16)
        
        if self.quit_button.getPressed():
            self.exit = True

    def handleEvents(self, event):
        self.start_button.handleEvents(event)
        self.quit_button.handleEvents(event)

    def draw(self, display: Surface):
        self.start_button.draw(display)
        self.quit_button.draw(display)
