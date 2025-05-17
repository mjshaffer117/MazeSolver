from window import *
from cell import Cell

def main():
    win = MainWindow(800, 600)

    cell_1 = Cell(win)
    cell_1.has_right_wall = False
    cell_1.draw(50, 50, 100, 100)

    cell_2 = Cell(win)
    cell_2.has_left_wall = False
    cell_2.has_bottom_wall = False
    cell_2.draw(100, 50, 150, 100)

    cell_1.draw_move(cell_2)

    cell_3 = Cell(win)
    cell_3.has_top_wall = False
    cell_3.has_right_wall = False
    cell_3.draw(100, 100, 150, 150)

    cell_2.draw_move(cell_3)

    cell_4 = Cell(win)
    cell_4.has_left_wall = False
    cell_4.draw(150, 100, 200, 150)

    cell_3.draw_move(cell_4, True)

    win.wait_for_close()

main()