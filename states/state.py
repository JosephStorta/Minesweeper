from pygame import Surface

class State:
    def __init__(self):
        self.exit = False # Whether the game should close
        self.change = False # Whether the state should change
        self.next = None # Stores the next state

    def update(self, delta: int):
        pass

    def handleEvents(self, event):
        pass

    def draw(self, display: Surface):
        pass
