import turtle
import random


finishLine = 300
clrs = ["red", "green", "brown", "blue", "magenta", "cyan"]
clrsBG = ["pink", "lightgreen", "khaki", "slateblue", "hotpink", "lightcyan"]
turtles = []


def maxTurtle():
    max = 0
    for t in range(6):
        if turtles[t].position()[0] > turtles[max].position()[0]:
            max = t
    return max


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
    moveTurtle = random.randint(10, 50)
    if turtles[t].position()[0] + moveTurtle >= finishLine - 30:
        turtles[t].setx(finishLine - 30)
        raceTrack.title(
            f"{clrs[t].upper()} Turtle Wins !!!"  #   Red X: {int(red.position()[0])}     Green X: {int(green.position()[0])}"
        )
        return True
    else:
        turtles[t].forward(moveTurtle)
        return False


def drawLines():
    lines = turtle.Turtle()
    lines.hideturtle()
    lines.penup()
    lines.setpos(finishLine, 275)
    lines.pendown()
    lines.setpos(finishLine, -275)


raceTrack = turtle.Screen()
# raceTrack.screensize(canvwidth=800, canvheight=600, bg="cyan")     # this creates the canvas - may need to scroll
raceTrack.setup(800, 600)  # this sets up the Window
raceTrack.title("Racing Turtles")
raceTrack.clear()

drawLines()

for tur in range(len(clrs)):
    turtles.append(turtle.Turtle())
    setUpTurtle(turtles[tur], clrs[tur], -370, 250 - (tur * 100))


winner = False
for m in range(200):

    for tur in range(6):
        if turtleMove(tur):
            winner = True
            break
    if winner:
        break

    raceTrack.bgcolor(clrsBG[maxTurtle()])


turtle.exitonclick()
