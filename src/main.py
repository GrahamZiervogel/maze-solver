from graphics import Window
from maze import Maze


def main(): 
    screen_x = 1920
    screen_y = 1080

    window = Window(screen_x, screen_y)

    num_rows = 12
    num_cols = 16
    margin = 50

    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    seed = 10
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window, seed)
    maze.solve()

    window.wait_for_close()


main()
