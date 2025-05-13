from window import *

def main():
    win = MainWindow(800, 600)

    line = Line(Point(10, 100), Point(500, 100))
    win.draw_line(line, "magenta")

    line = Line(Point(10, 300), Point(500, 300))
    win.draw_line(line, "cyan")

    line = Line(Point(10, 500), Point(500, 500))
    win.draw_line(line, "orange")

    win.wait_for_close()

main()