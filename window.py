from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Title")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill = fill_color, width = 2)

class Cell():
    def __init__(self, x1, y1, x2, y2, window):
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_top_wall = False
        self.has_bottom_wall = False
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window

    def draw(self, fill_color):
        point_tl = Point(self._x1, self._y1)
        point_tr = Point(self._x2, self._y1)
        point_bl = Point(self._x1, self._y2)
        point_br = Point(self._x2, self._y2)
        if self.has_left_wall:
            left_line = Line(point_tl, point_bl)
            self._win.draw_line(left_line, fill_color)
        if self.has_right_wall:
            right_line = Line(point_tr, point_br)
            self._win.draw_line(right_line, fill_color)
        if self.has_top_wall:
            top_line = Line(point_tl, point_tr)
            self._win.draw_line(top_line, fill_color)
        if self.has_bottom_wall:
            bottom_line = Line(point_bl, point_br)
            self._win.draw_line(bottom_line, fill_color)

    def draw_move(self, to_cell, undo=False):
        center_from_x = (self._x2 - self._x1) // 2 + self._x1
        center_from_y = (self._y2 - self._y1) // 2 + self._y1
        center_point_from = Point(center_from_x, center_from_y)
        print(center_from_x, center_from_y)
        center_to_x = (to_cell._x2 - to_cell._x1) // 2 + to_cell._x1
        center_to_y = (to_cell._y2 - to_cell._y1) // 2 + to_cell._y1
        print(center_to_x, center_to_y)
        center_point_to = Point(center_to_x, center_to_y)
        from_to_line = Line(center_point_from, center_point_to)
        if undo:
            self._win.draw_line(from_to_line, 'gray')
        else:
            self._win.draw_line(from_to_line, 'red')
