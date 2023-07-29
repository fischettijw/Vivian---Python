# Pygame Documentation    https://www.pygame.org/docs/

import pygame
import random
import os

# Clear Terminal
os.system("cls")

class Car():
    race_over = False
    race_length = 0
    car_width = 0
    car_min_speed = 0
    car_max_speed = 0    
    
    def __init__(self, x, y, clr1, clr2):
        self.x = x
        self.y = y
        self.clr1 = clr1
        self.clr2 = clr2
        
    def draw_car(self):
        pygame.draw.rect(screen, self.clr1, (self.x, self.y, Car.car_width, 20))
        pygame.draw.rect(screen, self.clr2, (self.x + 10, self.y -20, Car.car_width - 30, 20))
        pygame.draw.circle(screen, 'black',(self.x + 15,self.y + 20), 10)
        pygame.draw.circle(screen, 'black',(self.x + 55,self.y + 20), 10)
        
    def move_car(self):
        self.x += random.randint(Car.car_min_speed, Car.car_max_speed)
        self.draw_car()
        
    def checker_flag(self):
        if self.x > Car.race_length - Car.car_width:
            return True
        else:
            return False

# Screen Size
screen_width = 1024
screen_height = 400
screen_size = (screen_width, screen_height)

# Pygame Initialization
pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Vivan's Car Racing Game")

fps_Clock = pygame.time.Clock()
fps = 60

car1 = Car(0, 100, "green", "pink")
car2 = Car(0, 200, "blue", "yellow")
car3 = Car(0, 300, "magenta", "purple")

cars = [car1, car2, car3]

car_min_speed = 3
car_max_speed = 4

Car.race_length = screen_width
Car.car_width = 70
Car.car_min_speed = 3
Car.car_max_speed = 6
Car.race_over = False

# Game Loop Start
while Car.race_over == False:
    screen.fill("cyan")
    
    pygame.display.set_caption(f"Vivan's Car Racing Game    {car1.x}")

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Car.race_over = True
    
    for car in cars:
        car.move_car()
        Car.race_over = Car.race_over or car.checker_flag()      

    # FPS Clock and FLIP (update) Screen
    fps_Clock.tick(fps)
    pygame.display.flip()
# Game Loop End

print(car1.checker_flag(), car2.checker_flag(), car3.checker_flag())
print(car1.checker_flag() + car2.checker_flag() + car3.checker_flag())
pygame.time.wait(5000)
pygame.quit()