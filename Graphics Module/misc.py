import graphics as g
import time

win = g.GraphWin("My Circle", 500, 500)
while True:
    c = g.Circle(g.Point(100, 200), 50)
    c.setOutline("red")
    c.setFill("red")
    c.draw(win)
    time.sleep(0.1)
    c.undraw()
    time.sleep(0.1)
    if win.checkMouse() != None:
        break

# win.getMouse()  # pause for click in window
win.close()
