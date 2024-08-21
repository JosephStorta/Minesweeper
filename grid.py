from cell import Cell
from random import randint

class Grid:
    def __init__(self, grid_size: tuple):
        self.grid_size = grid_size

        self.cells = [[Cell() for x in range(grid_size[0])] for y in range(grid_size[1])]
    
    def getCell(self, cell_x: int, cell_y: int) -> Cell:
        if self.isCellValid(cell_x, cell_y):
            return self.cells[cell_y][cell_x]
    
    def setMines(self, mine_number: int):
        while mine_number > 0:
            mine_x = randint(0, self.grid_size[0] - 1)
            mine_y = randint(0, self.grid_size[1] - 1)

            cell = self.getCell(mine_x, mine_y)
            if cell.getState() == 9:
                continue

            cell.setState(9)

            mine_number -= 1
    
    def checkNeighbor(self, neighbor_x: int, neighbor_y: int) -> int:
        if not self.isCellValid(neighbor_x, neighbor_y):
            return 0
    
    def isCellValid(self, cell_x: int, cell_y: int) -> bool:
        return cell_x >= 0 and cell_y >= 0 and cell_x < self.grid_size[0] and cell_y < self.grid_size[1]