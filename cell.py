class Cell:
    def __init__(self, state: int = 0):
        self.__state = state
        self.__revealed = False
        self.__flagged = False
    
    def getState(self) -> int:
        return self.__state
    
    def isRevealed(self) -> bool:
        return self.__revealed

    def isFlagged(self) -> bool:
        return self.__flagged
    
    def setState(self, state: int):
        self.__state = state
    
    def setRevealed(self, revealed: bool):
        self.__revealed = revealed

    def setFlagged(self, flagged: bool):
        self.__flagged = flagged