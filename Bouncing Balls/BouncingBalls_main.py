import pygame
import random
import BouncingBalls_class

# define screen size and frames per second
width = 400
height = 300
fps = 15

# initialize pygame, screen, and create a Clock
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Balls by Mr. Joe")
clock = pygame.time.Clock()

# initialze ball list and define number of balls to create 
balls = []
number_of_balls = 100

# create all balls and add to list
for i in range(number_of_balls):
    balls.append(
        BouncingBalls_class.Ball(
            random.randint(15, 30),       # radius
            random.randint(40,width-40),  # initial x
            random.randint(40,height-40), # initial Y
            random.randint(-10,10),       # speed x
            random.randint(-15,15),       # speed y
            -1,                        # color  (-1 => random)
            screen                        # display screen
        )
    )


# Game loop
running = True
while running:
    clock.tick(fps)  # set frames per second
    for event in pygame.event.get():  # process events
        if event.type == pygame.QUIT:  # check for closing window
            running = False

    # Clear screen for to create current frame
    screen.fill('yellow')

	# update and draw all balls
    for ball in balls:
        ball.update()
        ball.draw()
        # ball.render()   # do not display each ball individually

	# transfer buffer to visual screen
    pygame.display.flip()

pygame.quit()
