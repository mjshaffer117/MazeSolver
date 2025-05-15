from window import *
from cell import Cell

def main():
    win = MainWindow(800, 600)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(150, 150, 200, 200)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(250, 250, 300, 300)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(350, 350, 400, 400)

    win.wait_for_close()

main()