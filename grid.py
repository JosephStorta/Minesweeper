from cell import Cell

class Grid:
    def __init__(self, grid_size):
        self.grid_size = grid_size

        self.cells = [[Cell for x in grid_size[0]] for y in grid_size[1]]
    
    def getCell(self, x, y) -> Cell:
        return self.cells[y][x]
    
    def checkNeighbor(self, neighbor_x, neighbor_y) -> int:
        if not self.isCellValid(neighbor_x, neighbor_y):
            return 0
    
    def isCellValid(self, cell_x, cell_y) -> bool:
        return cell_x >= 0 and cell_y >= 0 and cell_x < self.grid_size[0] and cell_y < self.grid_size[1]