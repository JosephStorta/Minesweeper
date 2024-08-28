import pygame
from pygame import Surface, font, transform
from globals import SCREEN_SIZE, TILE_SIZE, TILE_SCALE, TILE_SPRITES
from grid import Grid

class Game:
    def __init__(self, grid_size: tuple, mine_number: int):
        self.__grid_size = grid_size
        self.__mine_number = mine_number
        self.__flagged_cells = 0

        self.__grid = Grid(grid_size, mine_number)
        self.__board_position = ((SCREEN_SIZE[0] - (self.__grid_size[0] * TILE_SIZE[0] * TILE_SCALE)) // 2, 100)

        self.__timer = 0.0
        self.__font = font.Font(None, 64)

    def update(self, delta: int):
        self.__timer += delta / 1000
    
    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            cell_position = ((mouse_position[0] - self.__board_position[0]) // TILE_SIZE[0] // TILE_SCALE, (mouse_position[1] - self.__board_position[1]) // TILE_SIZE[1] // TILE_SCALE)
            
            if event.button == 1:
                self.__grid.revealCell(cell_position[0], cell_position[1])
            
            if event.button == 3:
                flagged = self.__grid.flagCell(cell_position[0], cell_position[1])

                if flagged == None:
                    return

                if flagged:
                    self.__flagged_cells += 1
                else:
                    self.__flagged_cells -= 1
                    
    def draw(self, display: Surface):
        self.__drawBoard(display)
        self.__drawTimer(display)
        self.__drawMines(display)
    
    def __drawBoard(self, display: Surface):
        y = self.__board_position[1]

        for row in self.__grid.getCells():
            x = self.__board_position[0]
            for cell in row:
                if cell.isRevealed():
                    sprite = TILE_SPRITES[cell.getState()]
                else:
                    if cell.isFlagged():
                        sprite = TILE_SPRITES[11]
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
        rect = timer.get_rect(centerx = 80, y = 32)
        display.blit(timer, rect)
    
    def __drawMines(self, display: Surface):
        mines = self.__font.render(str(self.__mine_number - self.__flagged_cells), False, (255, 255, 255))
        rect = mines.get_rect(centerx = SCREEN_SIZE[0] - 80, y = 32)
        display.blit(mines, rect)