from tkinter import Tk, BOTH, Canvas
import random

class MainWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="black", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.geometry(f"{width}x{height}+10+10") #POSITION WINDOW LOCATION ON SCREEN
        self.__rand_color = random.choice(["cyan", "magenta", "yellow"])
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def update_text(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        font = ("Ariel", 18, "bold")
        self.__canvas.create_text(x, y, text=text, font=font, fill=self.__rand_color)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="white"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running is True:
            self.redraw()

    def close(self):
        self.__running = False
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2

    def draw(self, canvas, fill_color="white"):
        self.canvas = canvas
        self.fill_color = fill_color
        canvas.create_line(
            self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2
        )