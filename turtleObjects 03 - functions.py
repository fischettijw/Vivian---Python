import turtle
import random


def name_of_object(arg):
    # check __name__ attribute (functions)
    try:
        return arg.__name__
    except AttributeError:
        pass

    for name, value in globals().items():
        if value is arg and not name.startswith("_"):
            return name


def setUpTurtle(t, clr, initX, initY):
    t.shape("turtle")
    t.turtlesize(2)
    t.color(clr)
    t.pensize(5)
    t.speed(10)
    t.pencolor(clr)
    t.penup()
    t.hideturtle()
    t.setpos(initX, initY)
    t.showturtle()
    t.pendown()
    t.speed(1)


def turtleMove(t):
    moveTurtle = random.randint(5, 30)
    if t.position()[0] + moveTurtle >= finishLine - 30:
        t.setx(finishLine - 30)
        raceTrack.title(
            f"{name_of_object(t).upper()} Turtle Wins !!!"  #   Red X: {int(red.position()[0])}     Green X: {int(green.position()[0])}"
        )
        return True
    else:
        t.forward(moveTurtle)
        return False


def drawLines():
    lines = turtle.Turtle()
    lines.hideturtle()
    lines.penup()
    lines.setpos(finishLine, 275)
    lines.pendown()
    lines.setpos(finishLine, -275)


finishLine = 300

raceTrack = turtle.Screen()
# raceTrack.screensize(canvwidth=800, canvheight=600, bg="cyan")     # this creates the canvas - may need to scroll
raceTrack.setup(800, 600)  # this sets up the Window

raceTrack.clear()

drawLines()
red = turtle.Turtle()
green = turtle.Turtle()
yellow = turtle.Turtle()
blue = turtle.Turtle()
magenta = turtle.Turtle()
cyan = turtle.Turtle()

setUpTurtle(red, "red", -370, 250)
setUpTurtle(green, "green", -370, 150)
setUpTurtle(yellow, "yellow", -370, 50)
setUpTurtle(blue, "blue", -370, -50)
setUpTurtle(magenta, "magenta", -370, -150)
setUpTurtle(cyan, "cyan", -370, -250)


for m in range(200):
    if turtleMove(red):
        break

    if turtleMove(green):
        break

    if turtleMove(yellow):
        break

    if turtleMove(blue):
        break

    if turtleMove(magenta):
        break

    if turtleMove(cyan):
        break

    if red.position()[0] > green.position()[0]:
        raceTrack.bgcolor("pink")
    if green.position()[0] > red.position()[0]:
        raceTrack.bgcolor("lime green")


turtle.exitonclick()
