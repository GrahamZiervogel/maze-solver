from graphics import Window, Point, Line


def main():
    width = 1920
    height = 1080

    window = Window(width, height)

    line1 = Line(Point(0, 0), Point(width, height))
    line2 = Line(Point(width, 0), Point(0, height))

    window.draw_line(line1, "red")
    window.draw_line(line2, "green")

    window.wait_for_close()


main()
