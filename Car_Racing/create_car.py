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
screen_width = 70
screen_height = 50
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('My Pygame Window Caption')

fps_Clock = pygame.time.Clock()
fps = 30

def draw_car(x,y, clr1, clr2):                                      # car is in a 70X50 rectangle
    pygame.draw.rect(screen, clr2, (x + 10, y, 70 - 30, 20))        # (surface, color top rect, top rect width, top rect height)
    pygame.draw.rect(screen, clr1, (x, y + 20, 70, 20))             # (surface, color middle rect, middle rect width, middle rect height)          
    pygame.draw.circle(screen, 'black', (x + 15, y + 40), 10)       # (surface, wheel color, x-y middle of back wheel)
    pygame.draw.circle(screen, 'black', (x + 55, y + 40), 10)       # (surface, wheel color, x-y middle of front wheel)

# Game Loop
done = False
while done == False:
    screen.fill("cyan")

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Drawing/Game Code
    draw_car(0, 0, "magenta", "pink")

    # FPS Clock and FLIP (update) Screen
    fps_Clock.tick(fps)
    pygame.display.flip()


pygame.quit()