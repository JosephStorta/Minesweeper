from cell import Cell
from random import randint

class Grid:
    def __init__(self, grid_size: tuple, mine_number: int):
        self.__grid_size = grid_size
        self.__mine_number = mine_number
        self.__cells = [[Cell() for x in range(grid_size[0])] for y in range(grid_size[1])]

        self.__generated = False
    
    def getSize(self) -> tuple:
        return self.__grid_size
    
    def getMineNumber(self) -> int:
        return self.__mine_number
    
    def getCells(self) -> list[list[Cell]]:
        return self.__cells

    def getCell(self, cell_x: int, cell_y: int) -> Cell:
        if self.__isCellValid(cell_x, cell_y):
            return self.__cells[cell_y][cell_x]
    
    def revealCell(self, cell_x: int, cell_y: int) -> bool:
        if not self.__isCellValid(cell_x, cell_y):
            return False
        
        cell = self.getCell(cell_x, cell_y)
        if cell.isRevealed() or cell.isFlagged():
            return False
        
        cell.setRevealed(True)

        if not self.__generated:
            self.__populateGrid()

        if cell.getState() == 0:
            self.__revealNeighbors(cell_x, cell_y)

        return cell.getState() == 9
    
    def flagCell(self, cell_x: int, cell_y: int) -> bool:
        if not self.__isCellValid(cell_x, cell_y):
            return
        
        cell = self.getCell(cell_x, cell_y)
        if cell.isRevealed():
            return
        
        cell.setFlagged(not cell.isFlagged())
        return cell.isFlagged()

    def checkGrid(self) -> bool:
        for row in self.__cells:
            for cell in row:
                if cell.isRevealed():
                    if cell.getState() == 9:
                        return False
                else:
                    if cell.getState() < 9:
                        return False
        
        return True

    def __revealNeighbors(self, cell_x: int, cell_y: int):
        self.revealCell(cell_x - 1, cell_y - 1)
        self.revealCell(cell_x    , cell_y - 1)
        self.revealCell(cell_x + 1, cell_y - 1)
        self.revealCell(cell_x - 1, cell_y    )
        self.revealCell(cell_x + 1, cell_y    )
        self.revealCell(cell_x - 1, cell_y + 1)
        self.revealCell(cell_x    , cell_y + 1)
        self.revealCell(cell_x + 1, cell_y + 1)

    def __populateGrid(self):
        self.__generateMines(self.__mine_number)

        for y in range(self.__grid_size[1]):
            for x in range(self.__grid_size[0]):
                cell = self.getCell(x, y)

                if cell.getState() < 9:
                    cell.setState(self.__checkNeighbors(x, y))
        
        self.__generated = True

    def __generateMines(self, mine_number: int):
        while mine_number > 0:
            mine_x = randint(0, self.__grid_size[0] - 1)
            mine_y = randint(0, self.__grid_size[1] - 1)

            cell = self.getCell(mine_x, mine_y)
            if cell.getState() == 9 or cell.isRevealed() or self.__hasRevealedNeighbors(mine_x, mine_y):
                continue

            cell.setState(9)

            mine_number -= 1
    
    def __hasRevealedNeighbors(self, cell_x: int, cell_y: int) -> bool:
        has_revealed_neighbors = False

        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x - 1, cell_y - 1)
        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x    , cell_y - 1)
        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x + 1, cell_y - 1)
        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x - 1, cell_y    )
        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x + 1, cell_y    )
        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x - 1, cell_y + 1)
        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x    , cell_y + 1)
        has_revealed_neighbors |= self.__isNeighborRevealed(cell_x + 1, cell_y + 1)

        return has_revealed_neighbors
    
    def __isNeighborRevealed(self, neighbor_x: int, neighbor_y: int) -> bool:
        if not self.__isCellValid(neighbor_x, neighbor_y):
            return False
        
        cell = self.getCell(neighbor_x, neighbor_y)
        return cell.isRevealed()

    def __checkNeighbors(self, cell_x: int, cell_y: int) -> int:
        mines = 0

        mines += self.__checkNeighbor(cell_x - 1, cell_y - 1)
        mines += self.__checkNeighbor(cell_x    , cell_y - 1)
        mines += self.__checkNeighbor(cell_x + 1, cell_y - 1)
        mines += self.__checkNeighbor(cell_x - 1, cell_y    )
        mines += self.__checkNeighbor(cell_x + 1, cell_y    )
        mines += self.__checkNeighbor(cell_x - 1, cell_y + 1)
        mines += self.__checkNeighbor(cell_x    , cell_y + 1)
        mines += self.__checkNeighbor(cell_x + 1, cell_y + 1)

        return mines

    def __checkNeighbor(self, neighbor_x: int, neighbor_y: int) -> int:
        if not self.__isCellValid(neighbor_x, neighbor_y):
            return 0
        
        cell = self.getCell(neighbor_x, neighbor_y)
        return cell.getState() == 9
    
    def __isCellValid(self, cell_x: int, cell_y: int) -> bool:
        return cell_x >= 0 and cell_y >= 0 and cell_x < self.__grid_size[0] and cell_y < self.__grid_size[1]