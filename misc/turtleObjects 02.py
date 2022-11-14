import turtle
import random

finishLine = 300


raceTrack = turtle.Screen()
# raceTrack.screensize(canvwidth=800, canvheight=600, bg="cyan")     # this creates the canvas - may need to scroll
raceTrack.setup(800, 600)  # this sets up the Window

raceTrack.clear()

lines = turtle.Turtle()
lines.hideturtle()
lines.penup()
lines.setpos(finishLine, 275)
lines.pendown()
lines.setpos(finishLine, -275)


red = turtle.Turtle()
red.shape("turtle")
red.turtlesize(2)
red.color("red")
red.pensize(5)
red.speed(10)

red.pencolor("red")

red.penup()
red.hideturtle()
red.setpos(-370, 250)
red.showturtle()
red.pendown()


green = turtle.Turtle()
green.shape("turtle")
green.turtlesize(2)
green.color("green")
green.pensize(5)
green.speed(10)

green.pencolor("green")

green.penup()
green.hideturtle()
green.setpos(-370, 150)
green.showturtle()
green.pendown()


red.speed(1)
green.speed(1)


for m in range(200):
    redMove = random.randint(5, 30)
    if red.position()[0] + redMove >= finishLine - 30:
        red.setx(finishLine - 30)
        raceTrack.title(
            f"Red Turtle Wins !!!   Red X: {int(red.position()[0])}     Green X: {int(green.position()[0])}"
        )
        break
    else:
        red.forward(redMove)
    raceTrack.title(
        f"Red X: {int(red.position()[0])}     Green X: {int(green.position()[0])}"
    )

    greenMove = random.randint(5, 30)
    if green.position()[0] + greenMove >= finishLine - 30:
        green.setx(finishLine - 30)
        raceTrack.title(
            f"Green Turtle Wins !!!   Red X: {int(red.position()[0])}     Green X: {int(green.position()[0])}"
        )
        break
    else:
        green.forward(greenMove)
    raceTrack.title(
        f"Red X: {int(red.position()[0])}     Green X: {int(green.position()[0])}"
    )

    if red.position()[0] > green.position()[0]:
        raceTrack.bgcolor("pink")
    if green.position()[0] > red.position()[0]:
        raceTrack.bgcolor("lime green")

    raceTrack.title(
        f"Red X: {int(red.position()[0])}     Green X: {int(green.position()[0])}"
    )


turtle.exitonclick()
