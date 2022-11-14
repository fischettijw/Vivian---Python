# https://www.youtube.com/watch?v=R39vTAj1u_8&list=PLmzkEJ1Zz_uZ5nvTOLaGHfinCzEVEVBlz
# https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

# from graphics import *
# from typing import Text

# from attr import s
import graphics as g


def main():
    # PART 1
    win = g.GraphWin("My Window: Part 1", 500, 500)
    win.setBackground("black")  # color_rgb(255, 0, 0)

    pt = g.Point(250, 250)
    cir = g.Circle(pt, 50)  # Circle(Point(250, 250), 50)
    cir.setFill(g.color_rgb(100, 255, 50))
    cir.draw(win)
    # cir.move(100,100)

    win.getMouse()
    win.close()

    # -----------------------------------------------------------

    # PART 2
    win = g.GraphWin("My Window: Part 2", 500, 500)
    win.setBackground("gray")  # color_rgb(255, 0, 0)

    pt1 = g.Point(250, 250)
    # pt1.setOutline(g.color_rgb(255, 255, 0))
    # pt1.draw(win)
    pt2 = g.Point(250, 350)
    ln = g.Line(pt1, pt2)
    ln.setFill(g.color_rgb(0, 255, 255))
    ln.setWidth(10)
    ln.draw(win)

    rect = g.Rectangle(g.Point(200, 50), g.Point(400, 150))
    rect.setOutline("yellow")
    rect.setFill("magenta")
    rect.setWidth(5)
    rect.draw(win)

    poly = g.Polygon(g.Point(40, 40), g.Point(100, 100), g.Point(40, 100))
    poly.setFill("green")
    poly.draw(win)

    win.getMouse()
    win.close()

    # -----------------------------------------------------------

    # PART 3
    win = g.GraphWin("My Window: Part 3", 500, 500)
    win.setBackground("light green")  # color_rgb(255, 0, 0)

    txt = g.Text(g.Point(250, 450), "This is my Text!")
    txt.setTextColor("blue")
    txt.setSize(36)
    txt.setFace("courier")
    txt.setStyle("bold italic")
    txt.draw(win)

    img = g.Image(g.Point(250, 200), "apple.png")
    img.draw(win)

    # img.move(100, 100)
    # img.draw(win)

    win.getMouse()
    win.close()

    # -----------------------------------------------------------

    # PART 4
    # win = g.GraphWin("My Window: Part 4", 500, 500)
    # win.setBackground("light green")  # color_rgb(255, 0, 0)

    # inputBox = g.Entry(g.Point(250, 250), 10)  # 10 max characters
    # inputBox.draw(win)
    # txt = g.Text(g.Point(250, 280), "")
    # txt.draw(win)

    # while True:
    #     txt.setText(inputBox.getText())

    # win.getMouse()
    # win.close()


main()
