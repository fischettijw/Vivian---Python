# Pygame Documentation    https://www.pygame.org/docs/

import pygame
import random
import os

os.system('cls')

# Functions
def draw_car(x, y, num):
    # pygame.draw.rect(screen, 'blue', (x, y, 70, 20))
    # pygame.draw.rect(screen, 'yellow', (x + 10, y - 20, 70 - 30, 20))
    # pygame.draw.circle(screen, 'black', (x + 15, y + 20), 10)
    # pygame.draw.circle(screen, 'black', (x + 55, y + 20), 10)
    
    # img = my_font.render(num, True, 'magenta')
    # screen.blit(img, (x + 25, y - 20))
    
    if num == "1":
        car_cyan_image = pygame.image.load("Car_Racing\car_cyan.png").convert_alpha()
        screen.blit(car_cyan_image, (x - 50, y - 20))
        img = my_font.render(num, True, 'black')
        screen.blit(img, (x - 8, y + 4))
        
    if num == "2":
        car_cyan_image = pygame.image.load("Car_Racing\car_purple.png").convert_alpha()
        screen.blit(car_cyan_image, (x - 50, y - 20))
        img = my_font.render(num, True, 'black')
        screen.blit(img, (x - 8, y + 4))
    

    

# Screen Size
screen_width = 1024
screen_height = 300


# Pygame Initialization
pygame.init()

# Initialize Font
my_font = pygame.font.SysFont(None, 32, bold=False, italic=True)

# Create screen
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
winner = None
running = True
while running == True:
    # Clear Entire Screen with CYAN
    screen.fill("cyan")

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_car(car1_x, car1_y, "1")
    car1_x += random.randint(car_min_speed, car_max_speed)
    if car1_x + 70 >= screen_width:
        running = False
    
    draw_car(car2_x, car2_y, "2")
    car2_x += random.randint(car_min_speed, car_max_speed)
    if car2_x + 70 >= screen_width:
        running = False   

    # FPS Clock and FLIP Screen
    fps_Clock.tick(fps)
    pygame.display.flip()
# Game Loop End

###############################################

print(car1_x, car2_x)
 
pygame.time.wait(1000)
pygame.quit()
