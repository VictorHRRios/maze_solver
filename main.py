from window import Window, Cell

def main():
    root_window = Window(800, 600)
    first_cell = Cell(5, 5, 55, 55, root_window)
    first_cell.has_top_wall = True
    first_cell.has_bottom_wall = True
    first_cell.has_left_wall = True
    first_cell.draw('black')

    second_cell = Cell(55, 5, 105, 55, root_window)
    second_cell.has_top_wall = True
    second_cell.has_right_wall = True
    second_cell.draw('black')

    first_cell.draw_move(second_cell)

    third_cell = Cell(55, 55, 105, 105, root_window)
    third_cell.has_bottom_wall = True
    third_cell.has_left_wall = True
    third_cell.has_right_wall = True
    third_cell.draw('black')

    second_cell.draw_move(third_cell)

    root_window.wait_for_close()


if __name__ == "__main__":
    main()