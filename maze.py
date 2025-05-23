from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, rows, cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.cols = cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win
        self.cells = []
        self.__win.update_text("CREATING GRID...", 160, 25)
        self.create_cells()
        self.__break_entrance_and_exit()

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
        self.__win.update_text("CREATING MAZE...", 400, 25)
        self.cells[0][0].has_top_wall = False
        self.draw_cell(0, 0)
        self.cells[self.cols - 1][self.rows - 1].has_bottom_wall = False
        self.draw_cell(self.cols - 1, self.rows - 1)

    def animate(self):
        self.__win.redraw()
        time.sleep(0.01)