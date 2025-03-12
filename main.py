from window import Window
from maze import Maze


def main():
    root_window = Window(1200, 800)

    a_maze = Maze(5, 5, 16, 16, 35, 35, root_window)
    a_maze.solve()

    root_window.wait_for_close()


if __name__ == "__main__":
    main()
