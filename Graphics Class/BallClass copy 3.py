import graphics as g
import time


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

balls = []
balls.append(Ball(win, 25, "red", 25, 25, 1, 1))
balls.append(Ball(win, 30, "blue", 50, 50, 5, 3))
balls.append(Ball(win, 35, "white", 75, 75, 3, 1))
balls.append(Ball(win, 40, "green", 100, 100, 2, 2))

delay = 0.005

loopOnBalls = True
while loopOnBalls:
    for ball in balls:
        ball.moveBall()
    time.sleep(delay)
    if win.checkMouse() != None:
        loopOnBalls = False

win.close()
