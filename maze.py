from window import Point, Line
import time
import random

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
            seed=None,
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
        self.seed = seed if seed else random.seed(seed) 


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

        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)
                print(col, row)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + (self._cell_size_x * i),
        y1 = self._y1 + (self._cell_size_y * j),
        x2 = self._x1 + (self._cell_size_x * (i + 1)),
        y2 = self._y1 + (self._cell_size_y * (j + 1)),
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
    
    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            top = j-1
            bottom = j+1
            right = i + 1
            left = i - 1
            print(i, j)

            if top >= 0 and not self._cells[i][top].visited:
                cells_to_visit.append((i, top))

            if left >= 0 and not self._cells[left][j].visited:
                cells_to_visit.append((left, j))

            if bottom < self._num_rows and not self._cells[i][bottom].visited:
                cells_to_visit.append((i, bottom))

            if right < self._num_cols and not self._cells[right][j].visited:
                cells_to_visit.append((right, j))
            if len(cells_to_visit) == 0:
                self._draw_cell(i,j)
                return
            else:
                new_i, new_j = cells_to_visit[random.randrange(0, len(cells_to_visit))]
                if new_j < j:
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i,j)
                    self._cells[i][top].has_bottom_wall = False
                    self._draw_cell(i,top)
                elif new_j > j:
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i,j)
                    self._cells[i][bottom].has_top_wall = False
                    self._draw_cell(i,bottom)
                elif new_i < i:
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i,j)
                    self._cells[left][j].has_right_wall = False
                    self._draw_cell(left,j)
                else:
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i,j)
                    self._cells[right][j].has_left_wall = False
                    self._draw_cell(right,j)
                self._break_walls_r(new_i, new_j) 





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