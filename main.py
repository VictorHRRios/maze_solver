from window import Window
from maze import Maze

def main():
    root_window = Window(800, 600)

    a_maze = Maze(5, 5, 12, 12, 50, 50, root_window)
    

    root_window.wait_for_close()


if __name__ == "__main__":
    main()