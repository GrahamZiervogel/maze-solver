import time
import random

from cell import Cell


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y

        self.__window = window
        
        if seed is not None:
            random.seed(seed)

        self._cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_recursive(0, 0)

    def __create_cells(self):
        for col_index in range(self.__num_cols):
            col = []
            for row_index in range(self.__num_rows):
                col.append(Cell(self.__window))
            self._cells.append(col)

        for col_index in range(self.__num_cols):
            for row_index in range(self.__num_rows):
                self.__draw_cell(col_index, row_index)

    def __draw_cell(self, col_index, row_index):
        if self.__window is None:
            return

        x1 = self.__x1 + (col_index * self.__cell_size_x)
        x2 = self.__x1 + ((col_index + 1) * self.__cell_size_x)
        y1 = self.__y1 + (row_index * self.__cell_size_y)
        y2 = self.__y1 + ((row_index + 1) * self.__cell_size_y)

        self._cells[col_index][row_index].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__window is None:
            return
        
        self.__window.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_recursive(self, col_index, row_index):
        self._cells[col_index][row_index]._visited = True
        while True:
            cells_to_visit = []

            if col_index > 0 and not self._cells[col_index - 1][row_index]._visited:
                cells_to_visit.append((col_index - 1, row_index))
            if col_index < (self.__num_cols - 1) and not self._cells[col_index + 1][row_index]._visited:
                cells_to_visit.append((col_index + 1, row_index))
            if row_index > 0 and not self._cells[col_index][row_index - 1]._visited:
                cells_to_visit.append((col_index, row_index - 1))
            if row_index < (self.__num_rows - 1) and not self._cells[col_index][row_index + 1]._visited:
                cells_to_visit.append((col_index, row_index + 1))

            if len(cells_to_visit) == 0:
                self.__draw_cell(col_index, row_index)
                return

            dir_index = random.randrange(len(cells_to_visit))
            visit_indexes = cells_to_visit[dir_index]

            if visit_indexes[0] == col_index - 1:
                self._cells[col_index][row_index].has_top_wall = False
                self._cells[visit_indexes[0]][visit_indexes[1]].has_bottom_wall = False
            if visit_indexes[0] == col_index + 1:
                self._cells[col_index][row_index].has_bottom_wall = False
                self._cells[visit_indexes[0]][visit_indexes[1]].has_top_wall = False
            if visit_indexes[1] == row_index - 1:
                self._cells[col_index][row_index].has_left_wall = False
                self._cells[visit_indexes[0]][visit_indexes[1]].has_right_wall = False
            if visit_indexes[1] == row_index + 1:
                self._cells[col_index][row_index].has_right_wall = False
                self._cells[visit_indexes[0]][visit_indexes[1]].has_left_wall = False              

            self.__break_walls_recursive(visit_indexes[0], visit_indexes[1])
