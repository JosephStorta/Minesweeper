import pygame

from globals import SCREEN_SIZE, readTiles
from states.main_menu import MainMenu

def run_game():
    """Initialize Pygame and runs the main game loop."""
    pygame.init()
    display = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    delta = 0 # Tracks time between frames
    running = True

    # Load initial game state
    state = MainMenu()

    readTiles()

    # Main loop
    while running:
        for event in pygame.event.get():
            state.handleEvents(event)

            if event.type == pygame.QUIT:
                running = False
        
        state.update(delta)

        if state.exit:
            running = False
        
        if state.change:
            state = state.next

        display.fill("black")
        state.draw(display)

        # Updates the screen
        pygame.display.flip()

        delta = clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run_game()
