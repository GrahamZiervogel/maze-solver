from graphics import Line, Point


class Cell():
    def __init__(self, window=None):
        self.__window = window

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__window is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        left_line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__window.draw_line(left_line)
        else:
            self.__window.draw_line(left_line, "white")

        right_line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__window.draw_line(right_line)
        else:
            self.__window.draw_line(right_line, "white")

        top_line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__window.draw_line(top_line)
        else:
            self.__window.draw_line(top_line, "white")

        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__window.draw_line(bottom_line)
        else:
            self.__window.draw_line(bottom_line, "white")
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        start_mid_x = (self._x1 + self._x2) / 2
        start_mid_y = (self._y1 + self._y2) / 2

        end_mid_x = (to_cell._x1 + to_cell._x2) / 2
        end_mid_y = (to_cell._y1 + to_cell._y2) / 2

        line = Line(Point(start_mid_x, start_mid_y), Point(end_mid_x, end_mid_y))

        self.__window.draw_line(line, fill_color)

