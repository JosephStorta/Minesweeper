class Cell:
    def __init__(self, state: int = 0):
        self.state = state
    
    def getState(self) -> int:
        return self.state
    
    def setState(self, state: int):
        self.state = state