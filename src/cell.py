from graphics import Line, Point


class Cell():
    def __init__(self, window):
        self.__window = window
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__window.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__window.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__window.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__window.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        start_mid_x = (self.__x1 + self.__x2) / 2
        start_mid_y = (self.__y1 + self.__y2) / 2

        end_mid_x = (to_cell.__x1 + to_cell.__x2) / 2
        end_mid_y = (to_cell.__y1 + to_cell.__y2) / 2

        line = Line(Point(start_mid_x, start_mid_y), Point(end_mid_x, end_mid_y))

        self.__window.draw_line(line, fill_color)

