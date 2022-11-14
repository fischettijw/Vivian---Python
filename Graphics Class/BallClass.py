import graphics as g
import time


class Ball:
    numOfBalls = 0

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
        Ball.numOfBalls += 1

    def moveBall(self):
        self.ball.move(self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy
        if self.x > (self.win.width - self.size) or (self.x - self.size) < 0:
            self.dx *= -1
        if self.y > (self.win.height - self.size) or (self.y - self.size) < 0:
            self.dy *= -1


winWidth = 800
winHeight = 800

win = g.GraphWin("Moving Ball", winWidth, winHeight)
win.setBackground("yellow")
delay = 0.005

ball1 = Ball(win, 25, "red", 25, 25, 2, 1)
ball2 = Ball(win, 30, "blue", 50, 50, 2, 3)
ball3 = Ball(win, 35, "white", 75, 75, 3, 1)
ball4 = Ball(win, 40, "green", 100, 100, 1, 1)


# win.getMouse()
while True:
    ball1.moveBall()
    ball2.moveBall()
    ball3.moveBall()
    ball4.moveBall()
    time.sleep(delay)

win.getMouse()
win.close()
