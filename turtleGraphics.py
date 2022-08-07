import turtle as t


def square(size):
    for n in range(4):
        t.forward(size)
        t.right(90)


def triangle(size):
    for n in range(3):
        t.forward(size)
        t.right(120)


t.setup(width=300, height=600)
t.bgcolor("pink")
t.pen(pencolor="green", pensize=5)
t.shape("triangle")  # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
t.penup()
t.goto(0, 0)
t.pendown()
square(50)
t.penup()
t.goto(100, 100)
t.pendown()
t.pen(pencolor="magenta", pensize=5)
square(50)
t.hideturtle()

t.penup()
t.goto(-100, -100)
t.pendown()

triangle(100)
t.showturtle()

t.exitonclick()
