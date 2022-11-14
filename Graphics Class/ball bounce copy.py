"""
Show a ball bouncing off the sides of the window.

https://anh.cs.luc.edu/python/hands-on/examples/bounce1.py

"""

from graphics import *
import time, random


def bounceInBox(shape, dx, dy, xLow, xHigh, yLow, yHigh):
    """Animate a shape moving in jumps (dx, dy), bouncing when
    its center reaches the low and high x and y coordinates.
    """

    delay = 0.005
    for i in range(600):
        shape.move(dx, dy)
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()
        if x < xLow:
            dx = -dx
        elif x > xHigh:
            dx = -dx
        if y < yLow:
            dy = -dy
        elif y > yHigh:
            dy = -dy
        time.sleep(delay)


def getRandomPoint(xLow, xHigh, yLow, yHigh):
    """Return a random Point with coordinates in the range specified."""
    x = random.randrange(xLow, xHigh + 1)
    y = random.randrange(yLow, yHigh + 1)
    return Point(x, y)


def makeDisk(center, radius, win):
    """return a red disk that is drawn in win with given center and radius."""
    disk = Circle(center, radius)
    disk.setOutline("red")
    disk.setFill("red")
    disk.draw(win)
    return disk


def bounceBall(dx, dy):
    """Make a ball bounce around the screen, initially moving by (dx, dy)
    at each jump."""

    winWidth = 800  # 290
    winHeight = 600  # 290
    win = GraphWin("Ball Bounce", winWidth, winHeight)
    win.setCoords(0, 0, winWidth, winHeight)

    radius = 10
    xLow = radius  # center is separated from the wall by the radius at a bounce
    xHigh = winWidth - radius
    yLow = radius
    yHigh = winHeight - radius

    center = getRandomPoint(xLow, xHigh, yLow, yHigh)
    ball = makeDisk(center, radius, win)

    bounceInBox(ball, dx, dy, xLow, xHigh, yLow, yHigh)

    win.close()


bounceBall(3, 5)
