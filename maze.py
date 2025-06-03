from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, rows, cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.cols = cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.cells = []
        if seed:
            random.seed(seed)
        self.__win.update_text("CREATING GRID...", 160, 25)
        self.create_cells()
        self.__break_entrance_and_exit()
        self.__win.update_text("CREATING MAZE...", 400, 25)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        self.__win.update_text("SOLVING...", 600, 25)

    def create_cells(self):
        for c in range(self.cols):
            col_cells = []
            for r in range(self.rows):
                col_cells.append(Cell(self.__win))
            self.cells.append(col_cells)
        for c in range(self.cols):
            for r in range(self.rows):
                self.draw_cell(c, r)

    def draw_cell(self, c, r):
        if self.__win is None:
            return
        x1 = self.x1 + c * self.cell_size_x
        y1 = self.y1 + r * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.cells[c][r].draw(x1, y1, x2, y2)
        self.animate()

    def __break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[self.cols - 1][self.rows - 1].has_bottom_wall = False
        self.draw_cell(self.cols - 1, self.rows - 1)

    def __break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            visit = []
            if i > 0 and not self.cells[i - 1][j].visited:
                #CAN MOVE RIGHT
                visit.append((i - 1, j))
            if i < self.cols - 1 and not self.cells[i + 1][j].visited:
                #CAN MOVE LEFT
                visit.append((i + 1, j))
            if j > 0 and not self.cells[i][j - 1].visited:
                #CAN MOVE DOWN
                visit.append((i, j - 1))
            if j < self.rows - 1 and not self.cells[i][j + 1].visited:
                #CAN MOVE UP
                visit.append((i, j + 1))
            if not visit:
                self.draw_cell(i, j)
                return
            next_cell = random.choice(visit)
            if next_cell[0] == i - 1:
                self.cells[i - 1][j].has_right_wall = False
                self.cells[i][j].has_left_wall = False
            elif next_cell[0] == i + 1:
                self.cells[i + 1][j].has_left_wall = False
                self.cells[i][j].has_right_wall = False
            elif next_cell[1] == j - 1:
                self.cells[i][j - 1].has_bottom_wall = False
                self.cells[i][j].has_top_wall = False
            elif next_cell[1] == j + 1:
                self.cells[i][j + 1].has_top_wall = False
                self.cells[i][j].has_bottom_wall = False
            self.__break_walls_r(next_cell[0], next_cell[1])

    def __reset_cells_visited(self):
        for c in self.cells:
            for r in c:
                r.visited = False
    
    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if i == self.cols - 1 and j == self.rows - 1:
            return True
        # MOVE LEFT
        if (
            i > 0
            and not self.cells[i][j].has_left_wall
            and not self.cells[i - 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i - 1][j])
            if self.solve_r(i - 1, j) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i - 1][j], True)
        # MOVE RIGHT
        if (
            i < self.cols - 1
            and not self.cells[i][j].has_right_wall
            and not self.cells[i + 1][j].visited
        ):
            self.cells[i][j].draw_move(self.cells[i + 1][j])
            if self.solve_r(i + 1, j) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i + 1][j], True)
        # MOVE UP
        if (
            j > 0
            and not self.cells[i][j].has_top_wall
            and not self.cells[i][j - 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j - 1])
            if self.solve_r(i, j - 1) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j - 1], True)
         # MOVE DOWN
        if (
            j < self.rows - 1
            and not self.cells[i][j].has_bottom_wall
            and not self.cells[i][j + 1].visited
        ):
            self.cells[i][j].draw_move(self.cells[i][j + 1])
            if self.solve_r(i, j + 1) == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j + 1], True)
        return False

    def solve(self):
        return self.solve_r(0, 0)

    def animate(self):
        self.__win.redraw()
        time.sleep(0.01)