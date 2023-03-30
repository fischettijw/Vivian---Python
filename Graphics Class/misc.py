# PyGame Documentation    https://www.pygame.org/docs/tut/PygameIntro.html

import sys, pygame
pygame.init()

width, height = 1200, 800
size = 1200, 800
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

apple = pygame.image.load("apple.png")
applerect = apple.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    applerect = applerect.move(speed)
    if applerect.left < 0 or applerect.right > width:
        speed[0] = -speed[0]
    if applerect.top < 0 or applerect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(apple, applerect)
    pygame.display.flip()