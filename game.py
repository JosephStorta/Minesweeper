from grid import Grid

GRID_SIZE = (10, 8)
MINE_NUMBER = 20

grid = Grid(GRID_SIZE)
grid.setMines(MINE_NUMBER)

for row in grid.cells:
    for cell in row:
        print(cell.getState(), end=" ")
    
    print()