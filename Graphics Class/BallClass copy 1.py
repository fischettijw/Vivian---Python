import graphics as g
import time


class Ball:
    numOfBalls = 0

    def __init__(self, win, size, color, x, y):
        self.win = win
        self.size = size
        self.color = color
        self.x = x
        self.y = y
        pt = g.Point(self.x, self.y)
        self.ball = g.Circle(pt, self.size)
        self.ball.setFill(self.color)
        self.ball.draw(win)
        Ball.numOfBalls += 1

    def moveBall(self, dx, dy):
        self.ball.move(dx, dy)


win = g.GraphWin("Moving Ball", 800, 800)
win.setBackground("yellow")
delay = 0.005

ball1 = Ball(win, 20, "green", 0, 0)
ball2 = Ball(win, 25, "red", 25, 25)
ball3 = Ball(win, 30, "blue", 50, 50)
ball4 = Ball(win, 35, "white", 75, 75)

print(Ball.numOfBalls)
win.getMouse()
for i in range(250):
    ball1.moveBall(1, 1)
    ball2.moveBall(2, 1)
    ball3.moveBall(2, 3)
    ball4.moveBall(2 / 2, 3 / 2)
    time.sleep(delay)


win.getMouse()
win.close()
