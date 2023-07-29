import pygame
import random

def rnd_color():     # create random color function
	clr = pygame.Color(random.randint(1, 255),
						  random.randint(1, 255),
						  random.randint(1, 255))
	return clr
	

# define screen size, fps, and create a Clock
width = 300
height = 300
fps = 30
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

x_ball = width / 2
y_ball = height / 2
x_speed = 3 #random.randint(3, 8)
y_speed = 6 #random.randint(3, 8)
# ball_color = pygame.Color(255,0,0)    # R G B  color
# ball_color = pygame.Color(random.randint(1, 255),
# 						  random.randint(1, 255),
# 						  random.randint(1, 255),0)    # R G B
ball_color = rnd_color()
radius = 20

# Game loop
running = True
while running:
    clock.tick(fps)  # set frames per second
    for event in pygame.event.get():  # process events
        if event.type == pygame.QUIT:  # check for closing window
            running = False

    # Update (locations)
    x_ball += x_speed
    y_ball += y_speed

    if x_ball > (width - radius) or x_ball < (0 + radius):
        x_speed *= -1
        ball_color = rnd_color()

    if y_ball > (height - radius) or y_ball < radius:
        y_speed *= -1
        ball_color = rnd_color()
	
    # Draw to Buffer
    screen.fill("yellow")
    pygame.draw.circle(screen, ball_color, (x_ball, y_ball), radius)

    # Render to Screen
    pygame.display.flip()

pygame.quit()
