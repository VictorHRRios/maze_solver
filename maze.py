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
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()


    def _create_cells(self):
        if self._num_rows < 1 or self._num_cols < 1:
            raise ValueError('Number of rows and columns needs to be a positive integer')
        if self._cell_size_x < 1 or self._cell_size_y < 1:
            raise ValueError('Size of cells needs to be a positive integer')
        for col in range(self._num_cols):
            col_cells = []
            for row in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        if not self._win:
            return
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)
        self._break_entrance_and_exit()
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * i),
        y1 = self._y1 + (self._cell_size_y * j),
        x2 = self._x1 + (self._cell_size_x * (i + 1)),
        y2 = self._y1 + (self._cell_size_y * (j + 1)),
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)



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

    def draw(self, x1, y1, x2, y2, fill_collor='black'):
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