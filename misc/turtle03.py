#  ctrl-shift-alt t     or     ctrl-alt n         Run Python Code
#  https://docs.python.org/3/library/turtle.html#turtle-methods


import turtle


def setUpTurtle(t, turtleClr, penClr, turtleSize, penSize, turtleSpeed, initX, initY):
    t.shape("turtle")  # 'arrow','turtle','circle','square','triangle','classic'
    t.turtlesize(turtleSize)
    t.color(turtleClr)
    t.pensize(penSize)  # 1,2,3, ...
    t.speed(turtleSpeed)  # 1 - 10 and 0
    t.pencolor(penClr)
    t.penup()
    t.hideturtle()
    t.setpos(initX, initY)
    t.showturtle()
    t.pendown()


def setUpScreen(scr, widht, height, title, scrColor):
    scr.setup(widht, height)
    scr.title(title)
    scr.bgcolor(scrColor)


def square(t, size):
    for m in range(4):
        t.forward(size)
        t.left(90)


def triangle(t, size):
    for m in range(3):
        t.forward(size)
        t.left(120)


def circleXY(t, x, y, radius):
    t.hideturtle()
    t.penup()
    t.setpos(x, y)
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)
    t.pendown()
    t.showturtle()


def squareXY(t, x, y, size):
    t.hideturtle()
    t.penup()
    t.setpos(x, y)
    t.right(90)
    t.forward(size / 2)
    t.right(90)
    t.pendown()
    square(t, size)
    # t.penup()
    # t.setpos(x, y)
    # t.left(180)
    # t.right(180)
    # t.forward(size / 2)
    # t.left(90)
    t.pendown()
    t.showturtle()


# -----------------------------------------------------------------------------------


screen = turtle.Screen()
setUpScreen(screen, 800, 600, "Turtle Graphics by Vivian", "pink")

doggie = turtle.Turtle()
setUpTurtle(doggie, "magenta", "magenta", 2, 3, 10, 0, 0)

kitty = turtle.Turtle()
setUpTurtle(kitty, "yellow", "green", 2, 3, 0, 100, -100)

# square(doggie, 100)
# triangle(doggie, 100)
# doggie.circle(100)
# doggie.hideturtle()


# square(kitty, 100)
# triangle(kitty, 100)
# kitty.circle(100)
# kitty.hideturtle()


# circleXY(kitty, kitty.pos()[0], kitty.pos()[1], 100)

doggie.hideturtle()
kitty.hideturtle()
for m in range(25, 200, 25):
    circleXY(kitty, 0, 0, m)
    squareXY(kitty, 0, 0, m)
# kitty.hideturtle()
kitty.showturtle()


turtle.exitonclick()
