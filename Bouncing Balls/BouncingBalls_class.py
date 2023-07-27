import random
import pygame

class Ball:
    def __init__(self, radius, x_init, y_init, x_speed, y_speed, clr, screen):
        self.radius = radius
        self.x = x_init
        self.y = y_init
        self.x_speed = x_speed
        self.y_speed = y_speed
		
        if clr == -1:
            self.clr = (random.randint(0,255),
						random.randint(0,255),
						random.randint(0,255))
        else:
            self.clr = clr
        
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > self.width - self.radius or self.x < self.radius:
            self.x_speed *= -1
        if self.y > self.height - self.radius or self.y < self.radius:
            self.y_speed *= -1

    def draw(self):
        pygame.draw.circle(self.screen, self.clr, (self.x, self.y), self.radius)

    # def render(self):
    #     pygame.display.flip()