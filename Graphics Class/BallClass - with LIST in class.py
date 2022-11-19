import graphics as g
import time
import random as rnd


class Ball:
    # numOfBalls = 0

    def __init__(self, win, size, color, x, y, dx, dy):
        self.win = win
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        pt = g.Point(self.x, self.y)
        self.ball = g.Circle(pt, self.size)
        self.ball.setOutline(self.color)
        self.ball.setFill(self.color)
        self.ball.draw(win)
        # Ball.numOfBalls += 1

    def moveBallBounce(self):
        self.ball.move(self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        if self.x > (self.win.width - self.size) or (self.x - self.size) < 0:
            self.dx *= -1
        if self.y > (self.win.height - self.size) or (self.y - self.size) < 0:
            self.dy *= -1
        g.update()

    def __str__(self):
        return f"X={self.x if self.x > 1000 else ('0' + str(self.x))}  \
               Y={self.y if self.y > 1000 else ('0' + str(self.y))}  Size ={self.size}  Color={self.color}  \
               dx={self.dx}  dy={self.dy}"


winWidth = 1600
winHeight = 800


win = g.GraphWin("Bouncing Balls in LIST", winWidth, winHeight)
win.setBackground("yellow")


numBalls = 100
delay = 0.0001 / numBalls

balls = []
for n in range(numBalls):
    sz = rnd.randint(20, 50)
    clr = g.color_rgb(rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
    xAxis = rnd.randint(100, winWidth - 100)
    yAxis = rnd.randint(100, winWidth - 100)
    diffX = rnd.randint(-20, 20)
    diffY = rnd.randint(-20, 20)
    balls.append(Ball(win, sz, clr, xAxis, yAxis, diffX, diffY))

loopOnBalls = True
while loopOnBalls:
    for ball in balls:
        ball.moveBallBounce()
    time.sleep(delay)
    if win.checkMouse() != None:
        loopOnBalls = False

# win.getMouse()
win.close()
