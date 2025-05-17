from window import Line, Point

class Cell:
    def __init__ (self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        centerx1 = abs(self.x2 - self.x1) // 2 + self.x1
        centery1 = abs(self.y2 - self.y1) // 2 + self.y1
        centerx2 = abs(to_cell.x2 - to_cell.x1) // 2 + to_cell.x1
        centery2 = abs(to_cell.y2 - to_cell.y1) // 2 + to_cell.y1
        if undo is True:
            fill_color = "dark blue"
        else:
            fill_color = "red"
        line = Line(Point(centerx1, centery1), Point(centerx2, centery2))
        self._win.draw_line(line, fill_color)
