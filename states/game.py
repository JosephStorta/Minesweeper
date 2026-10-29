import pygame
from pygame import Surface, transform

from globals import SCREEN_SIZE, FONT, TILE_SIZE, TILE_SCALE, TILE_SPRITES
from grid import Grid
from button import Button
from states import main_menu
from states.state import State

class Game(State):
    def __init__(self, grid_size: tuple, mine_number: int):
        super().__init__()

        self.__grid_size = grid_size
        self.__mine_number = mine_number
        self.__flagged_cells = 0

        self.__lose = False
        self.__win = False

        self.__grid = Grid(grid_size, mine_number)
        self.__board_position = (
            (SCREEN_SIZE[0] - (self.__grid_size[0] * TILE_SIZE[0] * TILE_SCALE)) // 2,
            (SCREEN_SIZE[1] - (self.__grid_size[1] * TILE_SIZE[1] * TILE_SCALE)) // 2 + 32
        )

        self.__timer = 0.0

        self.__menu_button = Button((100, 50), (SCREEN_SIZE[0] / 2, 57), "./sprites/menu_button.png")

        self.__win_message_color = [255.0, 0.0, 0.0]
        self.__color_transition = 0 # Determines which color channel to update

    def update(self, delta: int):
        self.__menu_button.update(delta)

        if self.__menu_button.getPressed():
            self.change = True
            self.next = main_menu.MainMenu()

        if self.__lose or self.__win:
            return

        self.__timer += delta / 1000
    
    def handleEvents(self, event):
        self.__menu_button.handleEvents(event)

        if self.__lose or self.__win:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            cell_position = ( # Convert screen position to cell grid position
                (mouse_position[0] - self.__board_position[0]) // TILE_SIZE[0] // TILE_SCALE,
                (mouse_position[1] - self.__board_position[1]) // TILE_SIZE[1] // TILE_SCALE
            )

            # Left click
            if event.button == 1:
                self.__lose = self.__grid.revealCell(cell_position[0], cell_position[1])
                self.__win = self.__grid.checkGrid()

            # Right click
            if event.button == 3:
                flagged = None

                if self.__flagged_cells < self.__mine_number:
                    flagged = self.__grid.flagCell(cell_position[0], cell_position[1])
                elif self.__flagged_cells == self.__mine_number:
                    cell = self.__grid.getCell(cell_position[0], cell_position[1])

                    if cell and cell.isFlagged():
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
        self.__drawButtons(display)
        self.__drawMines(display)

        if self.__win:
            message = FONT.render("You Win!", True, [int(i) for i in self.__win_message_color])
            rect = message.get_rect(centerx = SCREEN_SIZE[0] / 2, centery = SCREEN_SIZE[1] / 2)
            display.blit(message, rect)

            self.__update_win_color()
    
    def __drawBoard(self, display: Surface):
        y = self.__board_position[1]

        for row in self.__grid.getCells():
            x = self.__board_position[0]
            for cell in row:
                if self.__lose and cell.getState() == 9:
                    cell.setRevealed(True)

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

        time_display = f"{minutes:02d}:{seconds:02d}"

        timer = FONT.render(time_display, True, (255, 255, 255))
        rect = timer.get_rect(centerx = 80, y = 32)
        display.blit(timer, rect)
    
    def __drawButtons(self, display: Surface):
        self.__menu_button.draw(display)
    
    def __drawMines(self, display: Surface):
        mines = FONT.render(str(self.__mine_number - self.__flagged_cells), True, (255, 255, 255))
        rect = mines.get_rect(centerx = SCREEN_SIZE[0] - 80, y = 32)
        display.blit(mines, rect)
    
    def __update_win_color(self):
        """Cycle the color of the win message."""
        if self.__win_message_color[self.__color_transition + 1 if self.__color_transition < 2 else 0] < 255:
            self.__win_message_color[self.__color_transition + 1 if self.__color_transition < 2 else 0] += 255 / 20
        else:
            self.__win_message_color[self.__color_transition] -= 255 / 20

        if self.__win_message_color[self.__color_transition] <= 0:
            self.__color_transition = self.__color_transition + 1 if self.__color_transition < 2 else 0
