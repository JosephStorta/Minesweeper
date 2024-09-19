from pygame import Surface

class State:
    def __init__(self):
        self.exit = False
        self.change = False
        self.next = None

    def update(self, delta: int):
        pass

    def handleEvents(self, event):
        pass

    def draw(self, display: Surface):
        pass