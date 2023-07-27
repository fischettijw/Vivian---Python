# Snippet Generator
# https://snippet-generator.app/

# Pygame Documentation    https://www.pygame.org/docs/

import pygame
import os
from Pygame_Helper_Functions import random_color, \
       WHITE, BLACK, GRAY, RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN

# Clear Terminal
os.system("cls")

# Color Constants
# Color RGB Chart  https://www.rapidtables.com/web/color/RGB_Color.html
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (224, 224, 224)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# MAGENTA = (255, 0, 255)
# CYAN = (0, 255, 255)

circle_color = RED

# Screen Size
screen_width = 1024
screen_height = 768
screen_size = (screen_width, screen_height)

# Pygame Initialization
pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('My Pygame Window Caption')

fps_Clock = pygame.time.Clock()
fps = 30

# Game Loop
done = False
while done == False:
    screen.fill(CYAN)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            circle_color = random_color()

    # Drawing/Game Code
    # circle(surface, color, center, radius, width)
    pygame.draw.circle(screen, circle_color, (300, 250), 100, 0) 

    # FPS Clock and FLIP (update) Screen
    fps_Clock.tick(fps)
    pygame.display.flip()


pygame.quit()