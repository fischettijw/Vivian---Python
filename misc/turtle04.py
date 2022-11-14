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
    origPosX = t.xcor()
    origPosy = t.ycor()
    origHeading = t.heading()
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
    t.setpos(origPosX, origPosy)
    t.setheading(origHeading)
    t.pendown()
    t.showturtle()


def squareXY(t, x, y, size):
    origPosX = t.xcor()
    origPosy = t.ycor()
    origHeading = t.heading()
    t.hideturtle()
    t.penup()
    t.setpos(x, y)
    t.forward(-size / 2)
    t.right(90)
    t.forward(size / 2)
    t.left(90)
    t.pendown()
    square(t, size)
    t.penup()
    t.setpos(x, y)
    t.setpos(origPosX, origPosy)
    t.setheading(origHeading)
    t.pendown()
    t.showturtle()


# -----------------------------------------------------------------------------------


screen = turtle.Screen()
setUpScreen(screen, 800, 600, "Turtle Graphics by Vivian", "pink")

doggie = turtle.Turtle()
setUpTurtle(doggie, "magenta", "magenta", 2, 3, 10, -200, -200)


kitty = turtle.Turtle()
setUpTurtle(kitty, "yellow", "green", 2, 3, 0, 200, 200)

square(doggie, 100)
triangle(doggie, 100)
# doggie.circle(100)
# doggie.hideturtle()


# square(kitty, 100)
# triangle(kitty, 100)
# kitty.circle(100)
# kitty.hideturtle()


# circleXY(kitty, kitty.pos()[0], kitty.pos()[1], 100)

doggie.hideturtle()
kitty.hideturtle()

# kitty.right(45)

for r in range(25, 300, 25):
    circleXY(kitty, 0, 0, r)
    squareXY(kitty, 0, 0, 2 * r)


kitty.showturtle()
doggie.showturtle()


turtle.exitonclick()
