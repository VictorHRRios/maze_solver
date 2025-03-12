from window import Point, Line
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()


    def _create_cells(self):
        self._cells = []
        if self._num_rows < 1 or self._num_cols < 1:
            raise ValueError('Number of rows and columns needs to be a positive integer')
        if self._cell_size_x < 1 or self._cell_size_y < 1:
            raise ValueError('Size of cells needs to be a positive integer')
        for col in range(self._num_cols):
            row_cells = []
            for row in range(self._num_rows):
                row_cells.append(Cell(self._win))
            self._cells.append(row_cells)

        if not self._win:
            return
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)
    
    def _draw_cell(self, i, j):
        self._cells[i][j]._x1 = self._x1 + (self._cell_size_x * i),
        self._cells[i][j]._y1 = self._y1 + (self._cell_size_y * j),
        self._cells[i][j]._x2 = self._x1 + (self._cell_size_x * (i + 1)),
        self._cells[i][j]._y2 = self._y1 + (self._cell_size_y * (j + 1)),
        self._cells[i][j].has_bottom_wall = True
        self._cells[i][j].has_left_wall = True
        self._cells[i][j].has_top_wall = True
        self._cells[i][j].has_right_wall = True
        self._cells[i][j].draw('black')
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)


class Cell():
    def __init__(self, window=None):
        self.has_left_wall = False
        self.has_right_wall = False
        self.has_top_wall = False
        self.has_bottom_wall = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, fill_color):
        if not self._x1 or not self._x2 or not self._y1 or not self._y1:
            raise ValueError("No points indicated in cell")
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
    
    def __repr__(self):
        return f"{self._x1}, {self._y1} -> {self._x2}, {self._y2}\n"