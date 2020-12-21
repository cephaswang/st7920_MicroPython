def raiseError(*a, **k):
    raise NotImplementedError()

class Canvas:

    width=128
    height=64
    clear = raiseError
    plot = raiseError
    redraw = raiseError
#    create_plotter = raiseError

    def line(self, x1, y1, x2, y2, set=True):
        diffX = abs(x2 - x1)
        diffY = abs(y2 - y1)
        shiftX = 1 if (x1 < x2) else -1
        shiftY = 1 if (y1 < y2) else -1
        err = diffX - diffY
        while True:
            self.plot(x1, y1, set=True)
            if x1 == x2 and y1 == y2:
                break
            err2 = 2 * err
            if err2 > -diffY:
                err -= diffY
                x1 += shiftX
            if err2 < diffX:
                err += diffX
                y1 += shiftY

    def fill_rect(self, x1, y1, x2, y2,  set=True):
        for y in range(y1, y2):
            self.line(x1, y, x2, y,  set=True)

    def rect(self, x1, y1, x2, y2,  set=True):
        self.line(x1, y1, x2, y1,  set=True)
        self.line(x2, y1, x2, y2,  set=True)
        self.line(x2, y2, x1, y2,  set=True)
        self.line(x1, y2, x1, y1,  set=True)
