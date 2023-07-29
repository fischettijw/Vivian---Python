# Pygame Documentation    https://www.pygame.org/docs/
# Displaying Text         https://youtu.be/ndtFoWWBAoE

import pygame
import random
import os

# Clear Terminal
os.system("cls")

class Car():
    race_over = None
    race_length = None
    car_width = None
    car_min_speed = None
    car_max_speed = None
    win = None
    
    pygame.font.init()
    my_font = pygame.font.SysFont("Courier", 50, bold=True)
    
    def __init__(self, x, y, clr1, clr2):
        self.x = x
        self.y = y
        self.clr1 = clr1
        self.clr2 = clr2
        
    def draw_car(self):
        pygame.draw.rect(Car.win, self.clr1, (self.x, self.y, Car.car_width, 20))
        pygame.draw.rect(Car.win, self.clr2, (self.x + 10, self.y -20, Car.car_width - 30, 20))
        pygame.draw.circle(Car.win, 'black',(self.x + 15,self.y + 20), 10)
        pygame.draw.circle(Car.win, 'black',(self.x + 55,self.y + 20), 10)
        
    def move_car(self):
        self.x += random.randint(Car.car_min_speed, Car.car_max_speed)
        self.draw_car()
        
    def checker_flag(self):
        if self.x > Car.race_length - Car.car_width:
            return True
        else:
            return False
        
    def draw_lines():
        pygame.draw.line(Car.win, "black", (0, 50), (Car.race_length, 50), 5)
        pygame.draw.line(Car.win, "black", (0, 150), (Car.race_length, 150), 5)
        pygame.draw.line(Car.win, "black", (0, 250), (Car.race_length, 250), 5)
        pygame.draw.line(Car.win, "black", (0, 350), (Car.race_length, 350), 5)
        
    def draw_text(text, text_color, point):
        img = Car.my_font.render(text, True ,text_color)
        Car.win.blit(img, point)
        
########################################################################################

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

bg_image = pygame.image.load("Car_Racing\grass_background.jpg").convert()

Car.race_length = screen_width
Car.car_width = 70
Car.car_min_speed = 2
Car.car_max_speed = 3
Car.race_over = False
Car.win = screen

# Game Loop Start
while Car.race_over == False:
    # screen.fill("cyan")
    
    screen.blit(bg_image,(0,0))
    Car.draw_text("Vivian's Car Racing Game", "black", (300, 10))
    Car.draw_lines()

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
pygame.time.wait(1000)
pygame.quit()