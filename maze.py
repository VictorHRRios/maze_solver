from cell import Cell
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
            raise ValueError('Number of rows and columns \
                needs to be a positive integer')
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
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _draw_cell(self, i, j):
        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = self._x1 + self._cell_size_x * (i + 1)
        y2 = self._y1 + self._cell_size_y * (j + 1)
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            # if there is a top wall and is not visited
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                cells_to_visit.append((i, j-1))
            # if there is a left wall and is not visited
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                cells_to_visit.append((i-1, j))
            # if there is a bottom wall and is not visited
            if j+1 < self._num_rows and not self._cells[i][j+1].visited:
                cells_to_visit.append((i, j+1))
            # if there is a right wall and is not visited
            if i+1 < self._num_cols and not self._cells[i+1][j].visited:
                cells_to_visit.append((i+1, j))
            if len(cells_to_visit) == 0:  # If there are no walls to visit
                self._draw_cell(i, j)
                return
            new_i, new_j = cells_to_visit[random.randrange(
                0, len(cells_to_visit))]
            if new_j < j:
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i, j)
                self._cells[i][j-1].has_bottom_wall = False
                self._draw_cell(i, j-1)
            elif new_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i, j)
                self._cells[i][j+1].has_top_wall = False
                self._draw_cell(i, j+1)
            elif new_i < i:
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i, j)
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(i-1, j)
            else:
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(i+1, j)
            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[-1][-1]:
            return True
        # if there is a top wall and is not visited
        if (j-1 >= 0 and
                not self._cells[i][j-1].visited and
                not self._cells[i][j].has_top_wall):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

        if (i-1 >= 0 and
                not self._cells[i-1][j].visited and
                not self._cells[i][j].has_left_wall):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)

        if (j+1 < self._num_rows and
                not self._cells[i][j+1].visited and
                not self._cells[i][j].has_bottom_wall):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)

        if (i+1 < self._num_cols and
                not self._cells[i+1][j].visited and
                not self._cells[i][j].has_right_wall):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        return False
