# Snippet Generator
# https://snippet-generator.app/

# Pygame Documentation    https://www.pygame.org/docs/

import pygame
import os

# Clear Terminal
os.system("cls")

# Pygame Initialization
pygame.init()

# Screen Size & Caption
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('My Pygame Window Caption')

# Pygame Clock & FPS
fps_Clock = pygame.time.Clock()
fps = 30

# Game Loop
done = False
while done == False:
    screen.fill("cyan")

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # FPS Clock and FLIP (update) Screen
    fps_Clock.tick(fps)
    pygame.display.flip()


pygame.quit()