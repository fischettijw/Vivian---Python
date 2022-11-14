#  https://docs.python.org/3/library/turtle.html#turtle-methods

import turtle


screen = turtle.Screen()
screen.setup(600, 400)
screen.title("Vivian's Turtle Graphics")

tDoggie = turtle.Turtle()
tDoggie.speed(1)
tDoggie.shape("turtle")
tDoggie.pencolor("red")
tDoggie.fillcolor("green")
tDoggie.pensize(5)
tDoggie.turtlesize(2)
tDoggie.forward(100)
tDoggie.circle(100)

tDoggie.setpos(0, 0)
tDoggie.clear()

# tDoggie = turtle.Turtle()
tDoggie.speed(10)

tDoggie.shape("turtle")
tDoggie.pencolor("red")
tDoggie.fillcolor("green")
tDoggie.pensize(5)
tDoggie.turtlesize(2)
tDoggie.forward(100)
tDoggie.circle(100)

tDoggie.clear()


turtle.exitonclick()
