import time

from cell import Cell


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window

        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for col_index in range(self.__num_cols):
            col = []
            for row_index in range(self.__num_rows):
                col.append(Cell(self.__window))
            self.__cells.append(col)

        for col_index in range(self.__num_cols):
            for row_index in range(self.__num_rows):
                self.__draw_cell(col_index, row_index)

    def __draw_cell(self, colIndex, rowIndex):
        x1 = self.__x1 + (colIndex * self.__cell_size_x)
        x2 = self.__x1 + ((colIndex + 1) * self.__cell_size_x)
        y1 = self.__y1 + (rowIndex * self.__cell_size_y)
        y2 = self.__y1 + ((rowIndex + 1) * self.__cell_size_y)

        self.__cells[colIndex][rowIndex].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.__window.redraw()
        time.sleep(0.05)
