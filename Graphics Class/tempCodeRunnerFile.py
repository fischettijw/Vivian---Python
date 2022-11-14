
        if self.x > (self.win.width - self.size) or (self.x - self.size) < 0:
            self.dx *= -1
        if self.y > (self.win.height - self.size) or (self.y - self.size) < 0:
            self.dy *= -1
