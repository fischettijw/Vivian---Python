import pygame
import os

# Clear Terminal
os.system("cls")

# Screen Size
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)

# Pygame Initialization
pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('My Pygame Window Caption')

fps_Clock = pygame.time.Clock()
fps = 30


# Game Loop Start
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
# Game loop End

pygame.quit()