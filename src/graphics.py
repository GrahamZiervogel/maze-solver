from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width=1920, height=1080):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed.")
    
    def close(self):
        self.running = False


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        