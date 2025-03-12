from window import Window, Line, Point

def main():
    root_window = Window(800, 600)
    left_top = Point(0, 0)
    right_bottom = Point(800, 600)
    cross_line = Line(left_top, right_bottom)
    root_window.draw_line(cross_line, 'black')
    root_window.wait_for_close()


if __name__ == "__main__":
    main()