import pygame
from globals import SCREEN_SIZE, readTiles
from game import Game

pygame.init()
display = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
delta = 0
running = True

game = Game((16, 10), 20)

readTiles()

while running:
    for event in pygame.event.get():
        game.handleEvents(event)

        if event.type == pygame.QUIT:
            running = False
    
    game.update(delta)

    display.fill("black")
    game.draw(display)

    pygame.display.flip()

    delta = clock.tick(60)

pygame.quit()