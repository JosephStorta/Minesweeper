from pygame import Surface, font, transform
from globals import SCREEN_SIZE, TILE_SIZE, TILE_SCALE, TILE_SPRITES
from grid import Grid

class Game:
    def __init__(self, grid_size: tuple, mine_number: int):
        self.__grid_size = grid_size
        self.__mine_number = mine_number

        self.__grid = Grid(grid_size, mine_number)

        self.__timer = 0.0
        self.__font = font.Font(None, 64)

    def update(self, delta: int):
        self.__grid.revealCell(5, 4)

        self.__timer += delta / 1000

    def draw(self, display: Surface):
        self.__drawBoard(display)
        self.__drawTimer(display)
        self.__drawMines(display)
    
    def __drawBoard(self, display: Surface):
        y = 100

        for row in self.__grid.getCells():
            x = (SCREEN_SIZE[0] - (self.__grid_size[0] * TILE_SIZE[0] * TILE_SCALE)) // 2
            for cell in row:
                if cell.isRevealed():
                    sprite = TILE_SPRITES[cell.getState()]
                else:
                    sprite = TILE_SPRITES[10]
                
                display.blit(transform.scale_by(sprite, TILE_SCALE), (x, y))

                x += TILE_SIZE[0] * TILE_SCALE

            y += TILE_SIZE[1] * TILE_SCALE
    
    def __drawTimer(self, display: Surface):
        minutes = int(self.__timer) // 60
        seconds = int(self.__timer) % 60

        time_display = f"{minutes:02d}" + ":" +  f"{seconds:02d}"

        timer = self.__font.render(time_display, False, (255, 255, 255))
        rect = timer.get_rect(centerx = 80, y = 10)
        display.blit(timer, rect)
    
    def __drawMines(self, display: Surface):
        mines = self.__font.render(str(self.__mine_number), False, (255, 255, 255))
        rect = mines.get_rect(centerx = SCREEN_SIZE[0] - 80, y = 10)
        display.blit(mines, rect)