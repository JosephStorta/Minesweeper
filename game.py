from grid import Grid

GRID_SIZE = (10, 8)
MINE_NUMBER = 10

grid = Grid(GRID_SIZE, MINE_NUMBER)
grid.revealCell(4, 3)

for row in grid.getCells():
    for cell in row:
        if cell.isRevealed():
            print(cell.getState(), end=" ")
        else:
            print("#", end=" ")
    
    print()