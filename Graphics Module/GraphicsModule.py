import graphics as g


# def main():
win = g.GraphWin("Abigail: Part One", 500, 500)
win.setBackground(g.color_rgb(0, 0, 0))

g.drawBullseye(win)  # In 'graphics.ps' T LINE #964

txt = g.Text(g.Point(250, 40), "Abigail Lightle")
txt.setTextColor(g.color_rgb(0, 255, 255))
txt.setSize(36)
txt.setFace("comic sans ms")
txt.draw(win)

win.getMouse()
win.close()


# main()
