# Pygame Documentation    https://www.pygame.org/docs/

import pygame
import random
import os

os.system('cls')

# Functions
def draw_car(x, y):
    pygame.draw.rect(screen, 'blue', (x, y, 70, 20))
    pygame.draw.rect(screen, 'yellow', (x + 10, y - 20, 70 - 30, 20))
    pygame.draw.circle(screen, 'black', (x + 15, y + 20), 10)
    pygame.draw.circle(screen, 'black', (x + 55, y + 20), 10)

# Screen Size
screen_width = 1024
screen_height = 300

# Pygame Initialization
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vivan's Car Racing Game")

car1_x = 0
car1_y = 100

car2_x = 0
car2_y = 200

car_min_speed = 3
car_max_speed = 6

fps_Clock = pygame.time.Clock()
fps = 60

# Game Loop Start
winner = ''
running = True
while running == True:
    # Clear Entire Screen with CYAN
    screen.fill("cyan")

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_car(car1_x, car1_y)
    car1_x += random.randint(car_min_speed, car_max_speed)
    if car1_x + 70 >= screen_width:
        if car2_x < car1_x:
            winner = 'Car 1'
        if car1_x < car2_x:
            winner = 'Car 2'
        if car1_x == car2_x:
            winner = 'TIE'
        running = False
    
    draw_car(car2_x, car2_y)
    car2_x += random.randint(car_min_speed, car_max_speed)
    if car2_x + 70 >= screen_width:
        if car1_x < car2_x:
            winner = 'Car 2'
        if car2_x < car1_x:
            winner = 'Car 1'
        if car2_x == car1_x:
            winner = 'TIE'
        running = False   

    # FPS Clock and FLIP Screen
    fps_Clock.tick(fps)
    pygame.display.flip()
# Game Loop End

pygame.time.wait(2000)
if winner == 'tie':
    print('NO WINNER: Both Cars Tied')
else:
    print("WINNING CAR:", winner )
print()
 
pygame.quit()
