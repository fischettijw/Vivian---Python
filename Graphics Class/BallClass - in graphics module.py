import graphics as g
import time
import random as rnd

winWidth = 1600
winHeight = 800

win = g.GraphWin("Bouncing Balls in LIST", winWidth, winHeight)
win.setBackground("yellow")

numBalls = 100
delay = 0.0001 / numBalls

balls = []
for n in range(numBalls):
    size = rnd.randint(20, 50)
    color = g.Ball.randomColor()
    x = rnd.randint(100, winWidth - 100)
    y = rnd.randint(100, winHeight - 100)
    dx = rnd.randint(-30, 30)
    dy = rnd.randint(-30, 30)
    ball = g.Ball(win, size, color, x, y, dx, dy)
    balls.append(ball)

loopOnBalls = True
while loopOnBalls:
    for ball in balls:
        ball.moveBallBounce()
    time.sleep(delay)
    if win.checkMouse() != None:  # "None" means no mouse click since last checked
        loopOnBalls = False

win.close()
