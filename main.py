import pygame
from pygame import display, event, time


SCREEN_SIZE = (640, 480)

pygame.init()
window = display.set_mode(SCREEN_SIZE)
clock = time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill("purple")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()