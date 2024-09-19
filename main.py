import pygame
from globals import SCREEN_SIZE, readTiles
from states.main_menu import MainMenu

pygame.init()
display = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
delta = 0
running = True

state = MainMenu()

readTiles()

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

    pygame.display.flip()

    delta = clock.tick(60)

pygame.quit()