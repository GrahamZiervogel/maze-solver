import unittest

from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 160
        num_rows = 120

        maze = Maze(123, 456, num_rows, num_cols, 100, 100)

        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(maze._cells[0][0].has_top_wall, False)
        self.assertEqual(maze._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()
