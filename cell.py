from window import Point, Line


class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2, fill_collor='black'):
        if not self._win:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        point_tl = Point(self._x1, self._y1)
        point_tr = Point(self._x2, self._y1)
        point_bl = Point(self._x1, self._y2)
        point_br = Point(self._x2, self._y2)

        left_line = Line(point_tl, point_bl)
        right_line = Line(point_tr, point_br)
        top_line = Line(point_tl, point_tr)
        bottom_line = Line(point_bl, point_br)

        if self.has_left_wall:
            self._win.draw_line(left_line, fill_collor)
        else:
            self._win.draw_line(left_line, '#d9d9d9')

        if self.has_right_wall:
            self._win.draw_line(right_line, fill_collor)
        else:
            self._win.draw_line(right_line, '#d9d9d9')

        if self.has_top_wall:
            self._win.draw_line(top_line, fill_collor)
        else:
            self._win.draw_line(top_line, '#d9d9d9')

        if self.has_bottom_wall:
            self._win.draw_line(bottom_line, fill_collor)
        else:
            self._win.draw_line(bottom_line, '#d9d9d9')

    def draw_move(self, to_cell, undo=False):
        if not self._win:
            return
        center_from_x = (self._x2 - self._x1) // 2 + self._x1
        center_from_y = (self._y2 - self._y1) // 2 + self._y1
        center_point_from = Point(center_from_x, center_from_y)
        center_to_x = (to_cell._x2 - to_cell._x1) // 2 + to_cell._x1
        center_to_y = (to_cell._y2 - to_cell._y1) // 2 + to_cell._y1
        center_point_to = Point(center_to_x, center_to_y)
        from_to_line = Line(center_point_from, center_point_to)
        if undo:
            self._win.draw_line(from_to_line, 'gray')
        else:
            self._win.draw_line(from_to_line, 'red')

    def __repr__(self):
        return f"({self._x1}, {self._y1}) -> ({self._x2}, {self._y2})\n"

    def __eq__(self, other):
        return (self._x1 == other._x1 and
                self._y1 == other._y1 and
                self._x2 == other._x2 and
                self._y2 == other._y2)
