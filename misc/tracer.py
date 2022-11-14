#  turtle.colormode(255)
#  turtle.fillcolor(102,204,255)
#  turtle.pencolor(255,0,0)


from turtle import *
from random import randint

colormode(255)


speed(0)
hideturtle()
bgcolor(0, 0, 0)
tracer(100)  # 0-instant     otherwise delay
width(2)

h = 0.001

for i in range(90):
    color(randint(0, 255), randint(0, 255), randint(0, 255))
    forward(100)
    left(60)
    forward(100)
    right(120)
    circle(50)
    left(240)
    forward(100)
    left(60)
    forward(100)
    h += 0.02
    color(randint(0, 255), randint(0, 255), randint(0, 255))
    forward(100)
    right(60)
    forward(100)
    left(120)
    circle(-50)
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)
    h += 0.02
done()
