import pygame
import globals
from game import Game

pygame.init()
display = pygame.display.set_mode(globals.SCREEN_SIZE)
clock = pygame.time.Clock()
delta = 0
running = True

game = Game((10, 8), 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game.update(delta)

    display.fill("black")
    game.draw(display)

    pygame.display.flip()

    delta = clock.tick(60)

pygame.quit()